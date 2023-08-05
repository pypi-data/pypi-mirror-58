import copy
import glob
import io
import json
import os
import re
import requests
import sys

from bs4 import BeautifulSoup
import pandas as pd

from .. import _common
from .. import _config
from .. import _login
from .._common import DependencyNotFound
from .._common import Status

from seeq.base import system, util
from seeq.sdk import *
from seeq.sdk.rest import ApiException


class ItemJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Item):
            return o.definition
        else:
            return o


ORIGINAL_OWNER = '__original__'
FORCE_ME_AS_OWNER = '__me__'


def _replace_items(document, item_map):
    if document is None:
        return

    new_report = document
    for _id, _replacement in item_map.items():
        matches = re.finditer(_id, document, flags=re.IGNORECASE)
        for match in matches:
            new_report = re.sub(re.escape(match.group(0)), _replacement, new_report, flags=re.IGNORECASE)

    return new_report


def _get_canonical_server_url():
    url = _login.client.host.replace('/api', '').lower()  # type: str
    if url.startswith('http:') and url.endswith(':80'):
        url = url.replace(':80', '')
    if url.startswith('https:') and url.endswith(':443'):
        url = url.replace(':443', '')

    return url


class Item:
    def __init__(self, definition=None):
        self.definition = definition if definition else dict()

    def __contains__(self, key):
        return _common.present(self.definition, key)

    def __getitem__(self, key):
        return _common.get(self.definition, key)

    def __setitem__(self, key, val):
        self.definition[key] = val

    def __delitem__(self, key):
        del self.definition[key]

    def __repr__(self):
        return '%s "%s" (%s)' % (self.type, self.name, self.id)

    @property
    def id(self):
        return _common.get(self.definition, 'ID')

    @property
    def name(self):
        return _common.get(self.definition, 'Name')

    @name.setter
    def name(self, value):
        self.definition['Name'] = value

    @property
    def type(self):
        return _common.get(self.definition, 'Type')

    @staticmethod
    def _dict_from_id(item_id):
        items_api = ItemsApi(_login.client)
        item_output = items_api.get_item_and_all_properties(id=item_id)  # type: ItemOutputV1

        def _parse(val):
            if val == 'true':
                return True
            elif val == 'false':
                return False
            else:
                return val

        definition = {prop.name: _parse(prop.value) for prop in item_output.properties}
        definition['Name'] = item_output.name
        definition['Type'] = item_output.type

        if 'UIConfig' in definition:
            definition['UIConfig'] = json.loads(definition['UIConfig'])

        # For some reason, these are coming back as lower case, which makes things inconsistent
        if 'Scoped To' in definition and isinstance(definition['Scoped To'], str):
            definition['Scoped To'] = definition['Scoped To'].upper()

        if item_output.ancillaries:
            definition['Ancillaries'] = list()
            for item_ancillary_output in item_output.ancillaries:  # type: ItemAncillaryOutputV1
                item_ancillary_dict = Item._dict_via_attribute_map(item_ancillary_output, {
                    'data_id': 'Data ID',
                    'datasource_class': 'Datasource Class',
                    'datasource_id': 'Datasource ID',
                    'description': 'Description',
                    'id': 'ID',
                    'name': 'Name',
                    'scoped_to': 'Scoped To',
                    'type': 'Type'
                })

                if item_ancillary_output.items:
                    item_ancillary_dict['Items'] = list()
                    for ancillary_item_output in item_ancillary_output.items:  # type: AncillaryItemOutputV1
                        ancillary_item_dict = Item._dict_via_attribute_map(ancillary_item_output, {
                            'id': 'ID',
                            'name': 'Name',
                            'order': 'Order',
                            'type': 'Type'
                        })
                        item_ancillary_dict['Items'].append(ancillary_item_dict)

                definition['Ancillaries'].append(item_ancillary_dict)

        return definition

    @staticmethod
    def _dict_via_attribute_map(item, attribute_map):
        d = dict()
        for attr, prop in attribute_map.items():
            if hasattr(item, attr):
                d[prop] = getattr(item, attr)

        return d

    @staticmethod
    def _dict_from_scalar_value_output(scalar_value_output):
        """
        :type scalar_value_output: ScalarValueOutputV1
        """
        d = dict()
        d['Value'] = scalar_value_output.value
        d['Unit Of Measure'] = scalar_value_output.uom
        return d

    @staticmethod
    def _str_from_scalar_value_dict(scalar_value_dict):
        if isinstance(scalar_value_dict['Value'], str):
            return '%s' % scalar_value_dict['Value']
        elif isinstance(scalar_value_dict['Value'], int):
            return '%d %s' % (scalar_value_dict['Value'], scalar_value_dict['Unit Of Measure'])
        else:
            return '%f %s' % (scalar_value_dict['Value'], scalar_value_dict['Unit Of Measure'])

    @staticmethod
    def _property_input_from_scalar_str(scalar_str):
        match = re.fullmatch(r'([+\-\d.]+)(.*)', scalar_str)
        if not match:
            return None

        uom = match.group(2) if match.group(2) else None
        return PropertyInputV1(unit_of_measure=uom, value=float(match.group(1)))

    @staticmethod
    def _property_output_from_item_output(item_output, property_name):
        props = [p for p in item_output.properties if p.name == property_name]
        return props[0] if len(props) == 1 else None

    @staticmethod
    def formula_string_from_list(formula_list):
        return '\n'.join(formula_list) if isinstance(formula_list, list) else str(formula_list)

    @staticmethod
    def formula_list_from_string(formula_string):
        return formula_string.split('\n') if '\n' in formula_string else formula_string

    @staticmethod
    def _data_id_from_item_id(label, item_id):
        return '[%s] %s' % (label, item_id)

    @staticmethod
    def pull(item_id, *, allowed_types=None):
        definition = Item._dict_from_id(item_id)
        if allowed_types and definition['Type'] not in allowed_types:
            return None
        derived_class = getattr(sys.modules[__name__], definition['Type'])
        item = derived_class(definition)  # type: Item
        item._pull(item_id)
        return item

    def _pull(self, item_id):
        pass

    @staticmethod
    def load(definition):
        derived_class = getattr(sys.modules[__name__], definition['Type'])
        return derived_class(definition)

    def _pull_formula_based_item(self, calculated_item):
        self.definition['Formula'] = Item.formula_list_from_string(self.definition['Formula'])
        self.definition['Formula Parameters'] = dict()
        for parameter in calculated_item.parameters:  # type: FormulaParameterOutputV1
            if parameter.item:
                self.definition['Formula Parameters'][parameter.name] = parameter.item.id
            else:
                self.definition['Formula Parameters'][parameter.name] = parameter.formula

    def _scrape_auth_datasources(self):
        return set()


class ItemWithOwnerAndAcl(Item):
    def decide_owner(self, datasource_maps, item_map, *, owner=None, current_owner_id=None):
        requires_admin = True
        if _common.is_guid(owner):
            owner_id = owner
        elif owner is None:
            requires_admin = False
            if current_owner_id is None:
                owner_id = _login.user.id
            else:
                owner_id = current_owner_id
        elif owner == ORIGINAL_OWNER:
            owner_id = Workbook.find_identity(self['Owner'], datasource_maps=datasource_maps, item_map=item_map)
        elif owner == FORCE_ME_AS_OWNER:
            owner_id = _login.user.id
        else:
            raise ValueError('Invalid owner: %s' % owner)

        if current_owner_id is None or current_owner_id == owner_id:
            requires_admin = False

        if requires_admin and not _login.user.is_admin:
            raise RuntimeError("Logged in user must be an admin as a result of owner='%s'" % owner)

        return owner_id

    def _pull_owner_and_acl(self, owner_id):
        items_api = ItemsApi(_login.client)

        self['Owner'] = User.pull(owner_id).definition

        acl_output = items_api.get_access_control(id=self['ID'])  # type: AclOutputV1
        access_control = list()
        for ace_output in acl_output.acl:  # type: AceOutputV1
            ace_dict = Item._dict_via_attribute_map(ace_output, {
                'access_level': 'Access Level',
                'created_at': 'Created At',
                'id': 'ID'
            })

            if ace_output.identity.type == 'User':
                identity = User.pull(ace_output.identity.id)
            else:
                identity = UserGroup.pull(ace_output.identity.id)

            ace_dict['Identity'] = identity.definition
            access_control.append(ace_dict)

        self.definition['Access Control'] = access_control

    def _push_acl(self, pushed_id, datasource_maps, item_map, access_control):
        replace = False
        strict = False
        if access_control:
            treatment_parts = access_control.split(',')
            for treatment_part in treatment_parts:
                if treatment_part == 'add':
                    replace = False
                elif treatment_part == 'replace':
                    replace = True
                elif treatment_part == 'loose':
                    strict = False
                elif treatment_part == 'strict':
                    strict = True
                else:
                    raise RuntimeError("access_control argument must be 'add' or 'replace' comma 'loose' or 'strict'. "
                                       "For example: replace,strict")

        if 'Access Control' not in self:
            return

        items_api = ItemsApi(_login.client)
        acl_output = items_api.get_access_control(id=pushed_id)  # type: AclOutputV1
        for acl_to_push in self['Access Control']:
            found = False

            try:
                identity_id = Workbook.find_identity(acl_to_push['Identity'], datasource_maps, item_map)
            except _common.DependencyNotFound:
                if strict:
                    raise

                continue

            for existing_acl in acl_output.acl:  # type: AceOutputV1
                if existing_acl.access_level != acl_to_push['Access Level']:
                    continue

                if existing_acl.identity.id != identity_id:
                    continue

                found = True
                setattr(existing_acl, 'used', True)
                break

            if found:
                continue

            items_api.add_access_control_entry(id=pushed_id,
                                               body=AceInputV1(access_level=acl_to_push['Access Level'],
                                                               identity_id=identity_id))

        if replace:
            for existing_acl in acl_output.acl:  # type: AceOutputV1
                if hasattr(existing_acl, 'used') and getattr(existing_acl, 'used'):
                    continue

                items_api.remove_access_control_entry(id=pushed_id, ace_id=existing_acl.id)

    def _pull_ancestors(self, ancestors):
        if ancestors is None:
            return

        self.definition['Ancestors'] = [ancestor.id for ancestor in ancestors]

    def _scrape_auth_datasources(self):
        referenced_datasources = set()

        def _scrape_auth_datasource(d, key):
            if key in d and 'Datasource Class' in d[key] and 'Datasource ID' in d[key]:
                referenced_datasources.add((d[key]['Datasource Class'], d[key]['Datasource ID']))

        _scrape_auth_datasource(self, 'Owner')
        if 'Access Control' in self:
            for acl in self['Access Control']:
                _scrape_auth_datasource(acl, 'Identity')

        return referenced_datasources


class Folder(ItemWithOwnerAndAcl):
    def _pull(self, item_id):
        folders_api = FoldersApi(_login.client)
        folder_output = folders_api.get_folder(folder_id=item_id)  # type: FolderOutputV1
        self._pull_owner_and_acl(folder_output.owner.id)
        self._pull_ancestors(folder_output.ancestors)

    def push(self, parent_folder_id, datasource_maps, item_map, *, owner=None, label=None,
             access_control=None):
        items_api = ItemsApi(_login.client)
        folders_api = FoldersApi(_login.client)
        folder_item = Workbook.find_item(self.id, label)

        if not folder_item:
            folder_input = FolderInputV1()
            folder_input.name = self['Name']
            if 'Description' in self:
                folder_input.description = self['Description']
            folder_input.owner_id = self.decide_owner(datasource_maps, item_map, owner=owner)
            folder_input.parent_folder_id = parent_folder_id

            folder_output = folders_api.create_folder(body=folder_input)

            data_id = Workbook._data_id_from_item_id(label, self.definition['ID'])
            items_api.set_properties(id=folder_output.id, body=[
                ScalarPropertyV1(name='Datasource Class', value=_common.DEFAULT_DATASOURCE_CLASS),
                ScalarPropertyV1(name='Datasource ID', value=_common.DEFAULT_DATASOURCE_ID),
                ScalarPropertyV1(name='Data ID', value=data_id)])
        else:
            folder_output = folders_api.get_folder(folder_id=folder_item.id)  # type: FolderOutputV1

            props = [ScalarPropertyV1(name='Name', value=self['Name'])]
            if 'Description' in self:
                props.append(ScalarPropertyV1(name='Description', value=self['Description']))

            # If the folder happens to be archived, un-archive it. If you're pushing a new copy it seems likely
            # you're intending to revive it.
            props.append(ScalarPropertyV1(name='Archived', value=False))

            items_api.set_properties(id=folder_output.id, body=props)

            owner_id = self.decide_owner(
                datasource_maps, item_map, owner=owner, current_owner_id=folder_output.owner.id)

            if folder_output.owner.id != owner_id:
                items_api.change_owner(item_id=folder_output.id, new_owner_id=owner_id)

            if parent_folder_id is not None:
                folders_api.move_item_to_folder(folder_id=parent_folder_id, item_id=folder_output.id)
            elif folder_output.parent_folder_id is not None:
                folders_api.remove_item_from_folder(folder_id=folder_output.parent_folder_id,
                                                    item_id=folder_output.id)

        item_map[self.id.upper()] = folder_output.id.upper()

        if access_control:
            self._push_acl(folder_output.id, datasource_maps, item_map, access_control)

        return folder_output


class Workbook(ItemWithOwnerAndAcl):
    def __init__(self, definition=None, *, status=None):
        super().__init__(definition)

        self.status = Status.validate(status)
        self.item_inventory = dict()
        self.item_errors = set()
        self.worksheets = list()
        self.datasource_maps = list()
        self.scoped_items = list()
        self.datasource_inventory = dict()
        if 'Workbook Type' not in self.definition:
            self.definition['Workbook Type'] = _common.DEFAULT_WORKBOOK_TYPE
        if 'Data' not in self.definition:
            self.definition['Data'] = dict() if self['Workbook Type'] == 'Analysis' else {'isReportBinder': True}
        if 'Name' not in self.definition:
            self.definition['Name'] = _common.DEFAULT_WORKBOOK_NAME
        if 'ID' not in self.definition:
            self.definition['ID'] = _common.new_placeholder_guid()

    def __repr__(self):
        if 'Workbook Type' in self:
            return '%s %s "%s" (%s)' % (self['Workbook Type'], self.type, self.name, self.id)
        else:
            return super().__repr__()

    @property
    def url(self):
        if not self.definition['ID']:
            return
        url_parts = requests.utils.urlparse(_login.client.host)
        path = f'/workbook/{self.definition["ID"]}'
        if 'Folder ID' in self.definition and self.definition['Folder ID']:
            path = f'/{self.definition["Folder ID"]}' + path
        return requests.utils.urlunparse(url_parts._replace(path=path))

    @property
    def item_errors_str(self):
        return '\n'.join(['%s: %s' % (_item, _str) for _item, _str in self.item_errors])

    def update_status(self, result, count_increment):
        if self.status.current_df_index is None and len(self.status.df) == 0:
            self.status.df.at[0, :] = None
            self.status.current_df_index = 0
        current_count = self.status.get('Count') if \
            'Count' in self.status.df and self.status.get('Count') is not None else 0
        self.status.put('Count', current_count + count_increment)
        self.status.put('Time', self.status.get_timer())
        self.status.put('Result', result)

        self.status.update('[%d/%d] Processing %s "%s"' %
                           (len(self.status.df[self.status.df['Result'] != 'Queued']),
                            len(self.status.df), self['Workbook Type'], self['Name']),
                           Status.RUNNING)

    @staticmethod
    def pull(item_id, *, status=None, extra_workstep_tuples=None):
        definition = Item._dict_from_id(item_id)
        workbook = Workbook(definition, status=status)
        workbook._pull(workbook.id, extra_workstep_tuples=extra_workstep_tuples)
        return workbook

    def _pull(self, workbook_id=None, extra_workstep_tuples=None):
        if workbook_id is None:
            workbook_id = self.id
        workbooks_api = WorkbooksApi(_login.client)
        workbook_output = workbooks_api.get_workbook(id=workbook_id)  # type: WorkbookOutputV1

        self.definition['Path'] = ' >> '.join([a.name for a in workbook_output.ancestors])
        self.definition['Workbook Type'] = _common.get_workbook_type(workbook_output.data)

        self._pull_owner_and_acl(workbook_output.owner.id)
        self._pull_ancestors(workbook_output.ancestors)

        self.update_status('Pulling workbook', 1)

        self.definition['Data'] = json.loads(workbook_output.data)
        if 'workbookState' in self.definition:
            self.definition['workbookState'] = json.loads(self.definition['workbookState'])
        self.definition['Original Server URL'] = _get_canonical_server_url()

        self.worksheets = list()

        worksheet_ids = Workbook._pull_worksheet_ids(workbook_id)

        if extra_workstep_tuples:
            for workbook_id, worksheet_id, workstep_id in extra_workstep_tuples:
                if workbook_id == self.id and worksheet_id not in worksheet_ids:
                    worksheet_ids.append(worksheet_id)

        for worksheet_id in worksheet_ids:
            self.update_status('Pulling worksheets', 0)
            Worksheet.pull(worksheet_id, workbook=self, extra_workstep_tuples=extra_workstep_tuples)
            self.update_status('Pulling worksheets', 1)

        self._scrape_item_inventory()
        self._scrape_datasource_inventory()
        self._construct_default_datasource_maps()

    @staticmethod
    def _pull_worksheet_ids(workbook_id):
        workbooks_api = WorkbooksApi(_login.client)

        offset = 0
        limit = 1000
        worksheet_ids = list()
        while True:
            worksheet_output_list = workbooks_api.get_worksheets(
                workbook_id=workbook_id,
                offset=offset,
                limit=limit)  # type: WorksheetOutputListV1

            for worksheet_output in worksheet_output_list.worksheets:  # type: WorksheetOutputV1
                worksheet_ids.append(worksheet_output.id)

            if len(worksheet_output_list.worksheets) < limit:
                break

            offset = offset + limit

        return worksheet_ids

    def push(self, *, owner=None, folder_id=None, item_map=None, label=None,
             access_control=None, override_max_interp=False, status=None):
        self.status = Status.validate(status)

        workbook_item = Workbook.find_item(self.id, label)

        workbooks_api = WorkbooksApi(_login.client)
        items_api = ItemsApi(_login.client)
        datasources_api = DatasourcesApi(_login.client)
        folders_api = FoldersApi(_login.client)

        datasource_input = _common.get_data_lab_datasource_input()
        datasources_api.create_datasource(body=datasource_input)

        props = list()
        existing_worksheet_data_ids = dict()

        if not workbook_item:
            workbook_input = WorkbookInputV1()
            workbook_input.name = self.definition['Name']
            workbook_input.description = _common.get(self.definition, 'Description')
            workbook_input.folder_id = folder_id
            workbook_input.owner_id = self.decide_owner(self.datasource_maps, item_map, owner=owner)
            if 'Data' in self.definition:
                workbook_input.data = json.dumps(self.definition['Data'])
            elif self['Workbook Type'] == 'Topic':
                workbook_input.data = '{"isReportBinder":true}'
            else:
                workbook_input.data = '{}'
            workbook_input.branch_from = _common.get(self.definition, 'Branch From')
            workbook_output = workbooks_api.create_workbook(body=workbook_input)  # type: WorkbookOutputV1

            data_id = Workbook._data_id_from_item_id(label, self.id)
            items_api.set_properties(id=workbook_output.id, body=[
                ScalarPropertyV1(name='Datasource Class', value=_common.DEFAULT_DATASOURCE_CLASS),
                ScalarPropertyV1(name='Datasource ID', value=_common.DEFAULT_DATASOURCE_ID),
                ScalarPropertyV1(name='Data ID', value=data_id),
                ScalarPropertyV1(name='workbookState', value=_common.DEFAULT_WORKBOOK_STATE)])

        else:
            workbook_output = workbooks_api.get_workbook(id=workbook_item.id)  # type: WorkbookOutputV1

            # If the workbook happens to be archived, un-archive it. If you're pushing a new copy it seems likely
            # you're intending to revive it.
            items_api.set_properties(id=workbook_output.id, body=[ScalarPropertyV1(name='Archived', value=False)])

            for is_archived in [False, True]:
                offset = 0
                limit = 1000
                while True:
                    worksheet_output_list = workbooks_api.get_worksheets(workbook_id=workbook_output.id,
                                                                         is_archived=is_archived,
                                                                         offset=offset,
                                                                         limit=limit)  # type: WorksheetOutputListV1

                    for worksheet_output in worksheet_output_list.worksheets:  # type: WorksheetOutputV1
                        item_output = items_api.get_item_and_all_properties(
                            id=worksheet_output.id)  # type: ItemOutputV1
                        data_id = [p.value for p in item_output.properties if p.name == 'Data ID']
                        if len(data_id) == 0:
                            continue

                        existing_worksheet_data_ids[data_id[0]] = worksheet_output.id

                    if len(worksheet_output_list.worksheets) < limit:
                        break

                    offset = offset + limit

            owner_id = self.decide_owner(self.datasource_maps, item_map, owner=owner,
                                         current_owner_id=workbook_output.owner.id)

            if workbook_output.owner.id != owner_id:
                items_api.change_owner(item_id=workbook_output.id, new_owner_id=owner_id)

            if folder_id is not None:
                folders_api.move_item_to_folder(folder_id=folder_id, item_id=workbook_output.id)
            elif workbook_output.parent_folder_id is not None:
                folders_api.remove_item_from_folder(folder_id=workbook_output.parent_folder_id,
                                                    item_id=workbook_output.id)

        self.status.put('Pushed Workbook ID', workbook_output.id)

        if item_map is None:
            item_map = dict()

        item_map[self.id.upper()] = workbook_output.id.upper()

        if access_control:
            self._push_acl(workbook_output.id, self.datasource_maps, item_map, access_control)

        remaining_inventory = dict(self.item_inventory)
        while len(remaining_inventory) > 0:
            at_least_one_thing_pushed = False
            dependencies_not_found = list()
            dict_iterator = dict(remaining_inventory)
            for item_id, item in dict_iterator.items():
                if item['Type'] in ['Folder']:
                    at_least_one_thing_pushed = True
                    del remaining_inventory[item_id]
                    continue

                try:
                    item.push(self.datasource_maps,
                              pushed_workbook_id=workbook_output.id, item_map=item_map,
                              label=label, override_max_interp=override_max_interp)
                    self.update_status('Pushing item inventory', 1)
                    at_least_one_thing_pushed = True
                    del remaining_inventory[item_id]
                except DependencyNotFound as e:
                    dependencies_not_found.append(e.identifier)
                except KeyboardInterrupt:
                    raise
                except BaseException as e:
                    self.item_errors.add((item, _common.format_exception(e)))

            if not at_least_one_thing_pushed:
                for dependency_not_found in dependencies_not_found:
                    self.item_errors.add((dependency_not_found, 'Dependency not found'))
                for remaining_item in remaining_inventory.values():
                    self.item_errors.add((remaining_item, 'Not able to push'))
                break

        props.append(ScalarPropertyV1(name='Name', value=self.definition['Name']))
        if _common.present(self.definition, 'Description'):
            props.append(ScalarPropertyV1(name='Description', value=self.definition['Description']))
        if _common.present(self.definition, 'Data'):
            props.append(ScalarPropertyV1(name='Data', value=json.dumps(self.definition['Data'])))
        if _common.present(self.definition, 'workbookState'):
            props.append(ScalarPropertyV1(name='workbookState', value=json.dumps(self.definition['workbookState'])))

        items_api.set_properties(id=workbook_output.id, body=props)

        if len(set(self.worksheets)) != len(self.worksheets):
            raise ValueError('Worksheet list within Workbook "%s" is not unique: %s' % (self, self.worksheets))

        first_worksheet_id = None
        for worksheet in self.worksheets:
            self.update_status('Pushing worksheet', 1)
            worksheet_output = worksheet.push(workbook_output.id, item_map, existing_worksheet_data_ids, label=label)
            if first_worksheet_id is None:
                first_worksheet_id = worksheet_output.id

        # Pull the set of worksheets and re-order them
        remaining_pushed_worksheet_ids = Workbook._pull_worksheet_ids(workbook_output.id)
        next_worksheet_id = None
        for worksheet in reversed(self.worksheets):
            pushed_worksheet_id = item_map[worksheet.id]
            if next_worksheet_id is None:
                workbooks_api.move_worksheet(workbook_id=workbook_output.id, worksheet_id=pushed_worksheet_id)
            else:
                workbooks_api.move_worksheet(workbook_id=workbook_output.id, worksheet_id=pushed_worksheet_id,
                                             next_worksheet_id=item_map[next_worksheet_id])

            if pushed_worksheet_id in remaining_pushed_worksheet_ids:
                remaining_pushed_worksheet_ids.remove(pushed_worksheet_id)

            next_worksheet_id = worksheet.id

        # Archive any worksheets that are no longer active
        for remaining_pushed_worksheet_id in remaining_pushed_worksheet_ids:
            items_api.set_property(id=remaining_pushed_worksheet_id, property_name='Archived',
                                   body=PropertyInputV1(value=True))

        # Now go back through all the worksheets to see if any worksteps weren't resolved
        dependencies_not_found = set()
        for worksheet in self.worksheets:
            for workstep_tuple in worksheet.referenced_worksteps:
                referenced_workbook_id, referenced_worksheet_id, referenced_workstep_id = workstep_tuple
                if referenced_workstep_id not in item_map:
                    dependencies_not_found.add(
                        'Workbook %s, Worksheet %s, Workstep %s' % (
                            referenced_workbook_id, referenced_worksheet_id, referenced_workstep_id))

        if first_worksheet_id is not None:
            link_url = '%s/%sworkbook/%s/worksheet/%s' % (
                _config.get_api_url().replace('/api', ''),
                (folder_id + '/') if folder_id is not None else '',
                workbook_output.id,
                first_worksheet_id
            )
            self.status.put('Link', link_url)

        if len(dependencies_not_found) > 0:
            raise DependencyNotFound(None, '\n'.join(dependencies_not_found))

        self.status.update('Success', Status.SUCCESS)
        return workbook_output

    def push_containing_folders(self, item_map, use_full_path, parent_folder_id, owner, label, access_control):
        if 'Ancestors' not in self:
            return parent_folder_id

        create_folders_now = False
        if use_full_path or 'Search Folder ID' not in self:
            create_folders_now = True

        for ancestor_id in self['Ancestors']:
            if create_folders_now:
                folder = self.item_inventory[ancestor_id]  # type: Folder
                parent_folder = folder.push(parent_folder_id, self.datasource_maps, item_map,
                                            owner=owner, label=label, access_control=access_control)
                parent_folder_id = parent_folder.id
            elif self['Search Folder ID'] == ancestor_id:
                create_folders_now = True

        return parent_folder_id

    @staticmethod
    def find_identity(identity_dict, datasource_maps, item_map):
        # type: (...) -> str
        if identity_dict['ID'] in item_map:
            return item_map[identity_dict['ID']]

        if identity_dict['Type'] == 'User':
            identity = User(identity_dict)
        else:
            identity = UserGroup(identity_dict)

        pushed_identity = identity.push(datasource_maps=datasource_maps, item_map=item_map)

        return pushed_identity.id

    @staticmethod
    def find_item(item_id, label):
        """
        :rtype: ItemSearchPreviewV1
        """
        items_api = ItemsApi(_login.client)

        if not label:
            try:
                item_output = items_api.get_item_and_all_properties(id=item_id)  # type: ItemOutputV1
                return item_output
            except ApiException:
                # Fall through to looking via Data ID
                pass

        data_id = Workbook._data_id_from_item_id(label, item_id)
        _filters = [
            'Datasource Class==%s && Datasource ID==%s && Data ID==%s' % (
                _common.DEFAULT_DATASOURCE_CLASS, _common.DEFAULT_DATASOURCE_ID, data_id),
            '@includeUnsearchable']

        search_results = items_api.search_items(
            filters=_filters,
            offset=0,
            limit=2)  # type: ItemSearchPreviewPaginatedListV1

        if len(search_results.items) == 0:
            return None

        if len(search_results.items) > 1:
            raise RuntimeError('Multiple workbook/worksheet/workstep items found with Data ID of "%s"', data_id)

        return search_results.items[0]

    @property
    def referenced_items(self):
        referenced_items = list()
        for worksheet in self.worksheets:
            referenced_items.extend(worksheet.referenced_items)

        referenced_items.extend(self.scoped_items)

        return referenced_items

    @property
    def referenced_workbooks(self):
        references = dict()
        for worksheet in self.worksheets:
            for (workbook_id, worksheet_id, workstep_id) in worksheet.referenced_worksteps:
                if workbook_id not in references:
                    references[workbook_id] = set()

                references[workbook_id].add((workbook_id, worksheet_id, workstep_id))

        return references

    def find_workbook_links(self):
        # This should only be called during a pull operation, because it requires a connection to the original
        # database in order to resolve the workbook in a view-only link. (See Annotation class.)
        links = dict()
        for worksheet in self.worksheets:
            links.update(worksheet.find_workbook_links())

        return links

    def push_fixed_up_workbook_links(self, item_map):
        for worksheet in self.worksheets:
            worksheet.push_fixed_up_workbook_links(item_map)

    def _get_default_workbook_folder(self):
        return os.path.join(os.getcwd(), 'Workbook_%s' % self.id)

    @staticmethod
    def _get_workbook_json_file(workbook_folder):
        return os.path.join(workbook_folder, 'Workbook.json')

    @staticmethod
    def _get_items_json_file(workbook_folder):
        return os.path.join(workbook_folder, 'Items.json')

    @staticmethod
    def _get_datasources_json_file(workbook_folder):
        return os.path.join(workbook_folder, 'Datasources.json')

    @staticmethod
    def _get_datasource_map_json_file(workbook_folder, datasource_map):
        return os.path.join(
            workbook_folder, system.cleanse_filename(
                'Datasource_Map_%s_%s_%s.json' % (datasource_map['Datasource Class'],
                                                  datasource_map['Datasource ID'],
                                                  datasource_map['Datasource Name'])))

    def save(self, workbook_folder=None, overwrite=False):
        if not workbook_folder:
            workbook_folder = self._get_default_workbook_folder()

        if os.path.exists(workbook_folder):
            if overwrite:
                system.removetree(workbook_folder, keep_top_folder=True)
            else:
                raise RuntimeError('"%s" folder exists, use clean=True argument to overwrite it' %
                                   workbook_folder)

        os.makedirs(workbook_folder, exist_ok=True)

        workbook_json_file = Workbook._get_workbook_json_file(workbook_folder)

        definition_dict = dict(self.definition)
        definition_dict['Worksheets'] = list()
        for worksheet in self.worksheets:
            worksheet.save(workbook_folder)
            definition_dict['Worksheets'].append(worksheet.id)

        with open(workbook_json_file, 'w', encoding='utf-8') as f:
            json.dump(definition_dict, f, indent=4)

        items_json_file = Workbook._get_items_json_file(workbook_folder)
        with open(items_json_file, 'w', encoding='utf-8') as f:
            json.dump(self.item_inventory, f, indent=4, sort_keys=True, cls=ItemJSONEncoder)

        datasources_json_file = Workbook._get_datasources_json_file(workbook_folder)
        with open(datasources_json_file, 'w', encoding='utf-8') as f:
            json.dump(self.datasource_inventory, f, indent=4, sort_keys=True, cls=ItemJSONEncoder)

        for datasource_map in self.datasource_maps:
            datasource_map_file = Workbook._get_datasource_map_json_file(workbook_folder, datasource_map)
            with open(datasource_map_file, 'w', encoding='utf-8') as f:
                json.dump(datasource_map, f, indent=4)

    def _load(self, workbook_folder):
        if not os.path.exists(workbook_folder):
            raise RuntimeError('Workbook folder "%s" does not exist' % workbook_folder)

        workbook_json_file = Workbook._get_workbook_json_file(workbook_folder)
        if not os.path.exists(workbook_json_file):
            raise RuntimeError('Workbook JSON file "%s" does not exist' % workbook_json_file)

        with open(workbook_json_file, 'r', encoding='utf-8') as f:
            self.definition = json.load(f)

        self.worksheets = list()
        for worksheet_id in self.definition['Worksheets']:
            Worksheet.load_from_workbook_folder(self, workbook_folder, worksheet_id)

        del self.definition['Worksheets']

        self.item_inventory = Workbook._load_inventory(Workbook._get_items_json_file(workbook_folder))
        self.datasource_inventory = Workbook._load_inventory(Workbook._get_datasources_json_file(workbook_folder))
        self.datasource_maps = Workbook.load_datasource_maps(workbook_folder)

    @staticmethod
    def load_datasource_maps(folder):
        if not os.path.exists(folder):
            raise ValueError('Datasource map folder "%s" does not exist' % folder)

        datasource_map_files = glob.glob(os.path.join(folder, 'Datasource_Map_*.json'))
        datasource_maps = list()
        for datasource_map_file in datasource_map_files:
            with open(datasource_map_file, 'r', encoding='utf-8') as f:
                datasource_maps.append(json.load(f))

        return datasource_maps

    @staticmethod
    def _load_inventory(file_name):
        with open(file_name, 'r', encoding='utf-8') as f:
            loaded_inventory = json.load(f)

        inventory_dict = dict()
        for item_id, item in loaded_inventory.items():
            inventory_dict[item_id] = Item.load(item)

        return inventory_dict

    @staticmethod
    def load(workbook_folder):
        workbook = Workbook()
        workbook._load(workbook_folder)
        return workbook

    def _scrape_datasource_inventory(self):
        referenced_datasources = self._scrape_auth_datasources()
        for item in self.item_inventory.values():  # type: Item
            referenced_datasources.update(item._scrape_auth_datasources())
            if 'Datasource Class' in item and 'Datasource ID' in item:
                referenced_datasources.add((item['Datasource Class'], item['Datasource ID']))

        self.datasource_inventory = dict()
        for datasource_class, datasource_id in referenced_datasources:
            datasource = Datasource.from_datasource_id(datasource_class, datasource_id)
            self.datasource_inventory[datasource.id] = datasource

        return self.datasource_inventory

    def _construct_default_datasource_maps(self):
        self.datasource_maps = list()
        for _id, datasource in self.datasource_inventory.items():
            datasource_map = {
                'Datasource Class': datasource['Datasource Class'],
                'Datasource ID': datasource['Datasource ID'],
                'Datasource Name': datasource['Name'],
                'Tag-Level Map Files': list(),
                'RegEx-Based Maps': [
                    {
                        'Old': {
                            'Type': r'(?<type>.*)',
                            'Datasource Class': datasource['Datasource Class'],
                            'Datasource Name': datasource['Name']
                        },
                        'New': {
                            'Type': '${type}',
                            'Datasource Class': datasource['Datasource Class'],
                            'Datasource Name': datasource['Name']
                        }
                    }
                ]
            }

            if datasource['Datasource Class'] in ['Auth', 'Windows Auth', 'LDAP', 'OAuth 2.0']:
                datasource_map['RegEx-Based Maps'].append(copy.deepcopy(datasource_map['RegEx-Based Maps'][0]))

                datasource_map['RegEx-Based Maps'][0]['Old']['Type'] = 'User'
                datasource_map['RegEx-Based Maps'][0]['Old']['Username'] = r'(?<username>.*)'
                datasource_map['RegEx-Based Maps'][0]['New']['Type'] = 'User'
                datasource_map['RegEx-Based Maps'][0]['New']['Username'] = '${username}'

                datasource_map['RegEx-Based Maps'][1]['Old']['Type'] = 'UserGroup'
                datasource_map['RegEx-Based Maps'][1]['Old']['Name'] = r'(?<name>.*)'
                datasource_map['RegEx-Based Maps'][1]['New']['Type'] = 'UserGroup'
                datasource_map['RegEx-Based Maps'][1]['New']['Name'] = '${name}'
            else:
                datasource_map['RegEx-Based Maps'][0]['Old']['Data ID'] = r'(?<data_id>.*)'
                datasource_map['RegEx-Based Maps'][0]['New']['Data ID'] = '${data_id}'

            self.datasource_maps.append(datasource_map)

    def _scrape_item_inventory(self):
        self._scrape_references_from_scope()

        self.item_inventory = dict()
        if 'Ancestors' in self:
            for ancestor_id in self['Ancestors']:
                self.update_status('Scraping folders', 0)

                try:
                    item = Item.pull(ancestor_id, allowed_types=['Folder'])
                except ApiException as e:
                    if e.status == 404:
                        continue

                    raise

                if item is None:
                    continue

                self.update_status('Scraping folders', 1)

                self.item_inventory[ancestor_id] = item

        for reference in self.referenced_items:
            self._scrape_inventory_from_item(reference.id)

        self._scrape_inventory_from_ancillaries()

    def _scrape_inventory_from_item(self, item_id):
        if item_id in self.item_inventory:
            return

        allowed_types = [
            'StoredSignal',
            'CalculatedSignal',
            'StoredCondition',
            'CalculatedCondition',
            'CalculatedScalar',
            'Chart',
            'ThresholdMetric',
            'TableDatasource'
        ]

        self.update_status('Scraping item inventory', 0)

        try:
            item = Item.pull(item_id, allowed_types=allowed_types)
        except ApiException as e:
            if e.status == 404:
                return

            raise

        if item is None:
            return

        if 'Is Generated' in item and item['Is Generated']:
            return

        self.update_status('Scraping item inventory', 1)

        self.item_inventory[item_id] = item

        dependencies = self._scrape_references_from_dependencies(item_id)

        for dependency in dependencies:
            if dependency.id in self.item_inventory:
                continue

            self.update_status('Scraping item dependency', 0)

            try:
                dep_item = Item.pull(dependency.id, allowed_types=allowed_types)
            except ApiException as e:
                if e.status == 404:
                    continue

                raise

            if dep_item is None:
                continue

            if 'Is Generated' in dep_item and dep_item['Is Generated']:
                continue

            self.update_status('Scraping item dependency', 1)

            self.item_inventory[dependency.id] = dep_item

    def _scrape_references_from_scope(self):
        items_api = ItemsApi(_login.client)

        self.update_status('Scraping scope references', 0)

        self.scoped_items = list()
        offset = 0
        while True:
            search_results = items_api.search_items(
                filters=['', '@excludeGloballyScoped'],
                scope=self.id,
                offset=offset,
                limit=_common.DEFAULT_SEARCH_PAGE_SIZE,
            )  # type: ItemSearchPreviewPaginatedListV1

            self.scoped_items.extend([Reference(item.id, Reference.SCOPED) for item in search_results.items])

            if len(search_results.items) < search_results.limit:
                break

            offset += search_results.limit

        return self.scoped_items

    def _scrape_references_from_dependencies(self, item_id):
        items_api = ItemsApi(_login.client)
        referenced_items = list()

        self.update_status('Scraping dependencies', 0)

        try:
            dependencies = items_api.get_formula_dependencies(id=item_id)  # type: ItemDependencyOutputV1
        except ApiException as e:
            if e.status == 404:
                # For some reason, the item_id is unknown. We've seen this at Exxon, so just skip it.
                return referenced_items

            raise

        for dependency in dependencies.dependencies:  # type: ItemParameterOfOutputV1
            referenced_items.append(Reference(
                dependency.id,
                Reference.DEPENDENCY
            ))

        return referenced_items

    def _scrape_inventory_from_ancillaries(self):
        self.update_status('Scraping ancillaries', 0)

        current_inventory = list(self.item_inventory.values())
        for item in current_inventory:
            if 'Ancillaries' not in item:
                continue

            for ancillary_dict in item['Ancillaries']:
                if 'Items' not in ancillary_dict:
                    continue

                for ancillary_item_dict in ancillary_dict['Items']:
                    self._scrape_inventory_from_item(_common.get(ancillary_item_dict, 'ID'))


class Worksheet(Item):
    def __init__(self, workbook, definition=None):
        super().__init__(definition)

        if workbook is None or not isinstance(workbook, Workbook):
            raise ValueError("A Workbook is required to create a Worksheet")

        self.workbook = workbook  # type: Workbook
        self.workbook.worksheets.append(self)

        if self.workbook:
            if self.workbook['Workbook Type'] == 'Analysis':
                self.document = Journal(self)
            else:
                self.document = Report(self)
        else:
            self.document = None

        self.worksteps = dict()
        workstep = Workstep(self)
        self.definition['Current Workstep ID'] = workstep['ID']
        if 'ID' not in self.definition:
            self.definition['ID'] = _common.new_placeholder_guid()

    @property
    def url(self):
        if 'ID' not in self.definition or not self.definition['ID'] or not self.workbook:
            return
        url_parts = requests.utils.urlparse(_login.client.host)
        workbook_id = self.workbook.definition['ID']
        worksheet_id = self.definition['ID']
        path = f'/workbook/{workbook_id}/worksheet/{worksheet_id}'
        if 'Folder ID' in self.workbook.definition and self.workbook.definition['Folder ID']:
            path = f'/{self.workbook.definition["Folder ID"]}' + path
        return requests.utils.urlunparse(url_parts._replace(path=path))

    @property
    def display_items(self):
        if self.workbook['Workbook Type'] == 'Topic':
            self.workbook.status('Displayed Items are only valid for Analyses, not Topics', Status.CANCELED)
            return
        return self._get_display_items()

    @display_items.setter
    def display_items(self, value):
        if self.workbook['Workbook Type'] == 'Topic':
            self.workbook.status('Displayed Items are only valid for Analyses, not Topics', Status.CANCELED)
            return
        self._set_display_items(items_df=value)

    @property
    def view(self):
        if self.workbook['Workbook Type'] == 'Topic':
            self.workbook.status('Worksheet View is only valid for Analyses, not Topics', Status.CANCELED)
            return
        return self._get_worksheet_view()

    @view.setter
    def view(self, value):
        if self.workbook['Workbook Type'] == 'Topic':
            self.workbook.status('Worksheet View is only valid for Analyses, not Topics', Status.CANCELED)
            return
        self._set_worksheet_view(value)

    @property
    def display_range(self):
        if self.workbook['Workbook Type'] == 'Topic':
            self.workbook.status('Display Range is only valid for Analyses, not Topics', Status.CANCELED)
            return
        return self._get_display_range()

    @display_range.setter
    def display_range(self, value):
        if self.workbook['Workbook Type'] == 'Topic':
            self.workbook.status('Display Range is only valid for Analyses, not Topics', Status.CANCELED)
            return
        self._set_display_range(value)

    @property
    def investigate_range(self):
        if self.workbook['Workbook Type'] == 'Topic':
            self.workbook.status('Investigate Range is only valid for Analyses, not Topics', Status.CANCELED)
            return
        return self._get_investigate_range()

    @investigate_range.setter
    def investigate_range(self, value):
        if self.workbook['Workbook Type'] == 'Topic':
            self.workbook.status('Investigate Range is only valid for Analyses, not Topics', Status.CANCELED)
            return
        self._set_investigate_range(value)

    @property
    def date_ranges(self):
        if self.workbook['Workbook Type'] != 'Topic':
            self.workbook.status('Date Ranges are only valid for Topics, not Analyses', Status.CANCELED)
            return
        return self._get_date_ranges()

    @date_ranges.setter
    def date_ranges(self, value):
        if self.workbook['Workbook Type'] != 'Topic':
            self.workbook.status('Date Ranges are only valid for Topics, not Analyses', Status.CANCELED)
            return
        self._set_date_ranges(value)

    @staticmethod
    def pull(item_id, *, workbook=None, extra_workstep_tuples=None):
        if workbook is None:
            raise ValueError('workbook argument is None -- must be a valid Workbook object')

        definition = Item._dict_from_id(item_id)
        worksheet = Worksheet(workbook, definition)
        worksheet._pull(item_id, extra_workstep_tuples=extra_workstep_tuples)
        return worksheet

    def _pull(self, worksheet_id, extra_workstep_tuples=None):
        workbooks_api = WorkbooksApi(_login.client)
        worksheet_output = workbooks_api.get_worksheet(
            workbook_id=self.workbook.id, worksheet_id=worksheet_id)  # type: WorksheetOutputV1

        self.document.pull()

        current_workstep_id = Worksheet._get_current_workstep_id(worksheet_output.workstep)

        workstep_tuples_to_pull = set()
        if current_workstep_id is not None:
            workstep_tuples_to_pull.add((self.workbook.id, self.id, current_workstep_id))
            self.definition['Current Workstep ID'] = current_workstep_id

        for workbook_id, worksheet_id, workstep_id in self.document.referenced_worksteps:
            if isinstance(self.document, Journal) or worksheet_id == self.id:
                workstep_tuples_to_pull.add((workbook_id, worksheet_id, workstep_id))

        if extra_workstep_tuples:
            for workbook_id, worksheet_id, workstep_id in extra_workstep_tuples:
                if workbook_id == self.workbook.id and worksheet_id == self.id and workstep_id is not None:
                    workstep_tuples_to_pull.add((workbook_id, worksheet_id, workstep_id))

        self._pull_worksteps(workstep_tuples_to_pull)
        if not self.worksteps:
            workstep = Workstep(self)
            self.definition['Current Workstep ID'] = workstep['ID']

    def _pull_worksteps(self, workstep_tuples):
        for workstep_tuple in workstep_tuples:
            workbook_id, worksheet_id, workstep_id = workstep_tuple
            if workstep_id not in self.worksteps:
                self.workbook.update_status('Pulling worksteps', 0)
                self.worksteps[workstep_id] = Workstep.pull(workstep_tuple, worksheet=self)
                self.workbook.update_status('Pulling worksteps', 1)

    def push(self, pushed_workbook_id, item_map, existing_worksheet_data_ids, label=None):
        # After Integrated Security was introduced, we can no longer search for Worksheets using Data ID,
        # so we use the passed-in dictionary that the Workbook created to find existing worksheets.
        data_id = Workbook._data_id_from_item_id(label, self.id)

        workbooks_api = WorkbooksApi(_login.client)
        items_api = ItemsApi(_login.client)
        props = list()
        if data_id not in existing_worksheet_data_ids:
            worksheet_input = WorksheetInputV1()
            worksheet_input.name = self.definition['Name']
            worksheet_output = workbooks_api.create_worksheet(
                workbook_id=pushed_workbook_id, body=worksheet_input)  # type: WorksheetOutputV1

            data_id = Workbook._data_id_from_item_id(label, self.id)
            props = [ScalarPropertyV1(name='Datasource Class', value=_common.DEFAULT_DATASOURCE_CLASS),
                     ScalarPropertyV1(name='Datasource ID', value=_common.DEFAULT_DATASOURCE_ID),
                     ScalarPropertyV1(name='Data ID', value=data_id)]

            pushed_worksheet_id = worksheet_output.id
        else:
            worksheet_output = workbooks_api.get_worksheet(workbook_id=pushed_workbook_id,
                                                           worksheet_id=existing_worksheet_data_ids[data_id])
            props.append(ScalarPropertyV1(name='Name', value=self.definition['Name']))
            pushed_worksheet_id = worksheet_output.id

        item_map[self.id.upper()] = pushed_worksheet_id.upper()

        props.append(ScalarPropertyV1(name='Archived', value=_common.get(self, 'Archived', False)))
        items_api.set_properties(id=pushed_worksheet_id, body=props)

        pushed_current_workstep_id = None
        for workstep_id, workstep in self.worksteps.items():
            self.workbook.update_status('Pushing worksteps', 0)
            pushed_workstep_id = workstep.push_to_specific_worksheet(pushed_workbook_id, pushed_worksheet_id, item_map)
            self.workbook.update_status('Pushing worksteps', 1)
            item_map[workstep_id.upper()] = pushed_workstep_id.upper()

            if workstep_id == self.definition['Current Workstep ID']:
                pushed_current_workstep_id = pushed_workstep_id

        if not pushed_current_workstep_id:
            raise RuntimeError("Workstep for worksheet's 'Current Workstep ID' not found")

        # We have to do this at the end otherwise the other pushed worksheets will take precedence
        workbooks_api.set_current_workstep(workbook_id=pushed_workbook_id,
                                           worksheet_id=pushed_worksheet_id,
                                           workstep_id=pushed_current_workstep_id)

        self.document.push(pushed_workbook_id, pushed_worksheet_id, item_map, push_images=True)

        return worksheet_output

    @property
    def referenced_items(self):
        referenced_items = list()
        for workstep_id, workstep in self.worksteps.items():  # type: Workstep
            referenced_items.extend(workstep.referenced_items)

        referenced_items.extend(self.document.referenced_items)

        return referenced_items

    @property
    def referenced_worksteps(self):
        return self.document.referenced_worksteps

    def find_workbook_links(self):
        return self.document.find_workbook_links()

    def push_fixed_up_workbook_links(self, item_map):
        if self.workbook.id not in item_map or self.id not in item_map:
            return

        self.document.push(item_map[self.workbook.id], item_map[self.id], item_map, push_images=False)

    @staticmethod
    def _get_current_workstep_id(workstep):
        if not workstep:
            return None

        return workstep.split('/')[-1]

    @staticmethod
    def _get_worksheet_json_file(workbook_folder, worksheet_id):
        return os.path.join(workbook_folder, 'Worksheet_%s.json' % worksheet_id)

    def save(self, workbook_folder):
        worksheet_json_file = Worksheet._get_worksheet_json_file(workbook_folder, self.id)

        with open(worksheet_json_file, 'w', encoding='utf-8') as f:
            json.dump(self.definition, f, indent=4)

        self.document.save(workbook_folder)

        for workstep_id, workstep in self.worksteps.items():
            workstep.save(workbook_folder)

    def _load(self, workbook_folder, worksheet_id):
        worksheet_json_file = Worksheet._get_worksheet_json_file(workbook_folder, worksheet_id)

        with open(worksheet_json_file, 'r', encoding='utf-8') as f:
            self.definition = json.load(f)

        if self.workbook['Workbook Type'] == 'Analysis':
            self.document = Journal.load(self, workbook_folder)
        else:
            self.document = Report.load(self, workbook_folder)

        self.worksteps = dict()
        workstep_files = glob.glob(os.path.join(workbook_folder, 'Worksheet_%s_Workstep_*.json' % worksheet_id))
        for workstep_file in workstep_files:
            match = re.match(r'.*?Worksheet_.*?_Workstep_(.*?).json$', workstep_file)
            workstep_id = match.group(1)
            self.worksteps[workstep_id] = Workstep.load_from_workbook_folder(self, workbook_folder, workstep_id)

    @staticmethod
    def load_from_workbook_folder(workbook, workbook_folder, worksheet_id):
        worksheet = Worksheet(workbook)
        worksheet._load(workbook_folder, worksheet_id)
        return worksheet

    def _get_display_range(self):
        # type: () -> (pd.DataFrame, None)
        """
        Get the display range of the current workstep of the worksheet.

        Returns
        -------
        {pandas.DataFrame, None}
            A pandas DataFrame with the current display range in ISO8601 text
            in columns of 'Start' and 'End'
        """
        return pd.DataFrame(self.worksteps[self.definition['Current Workstep ID']].display_range)

    def _set_display_range(self, display_range):
        # type: (pd.DataFrame) -> None
        """
        Set the display range on the current workstep of the worksheet

        Parameters
        ----------
        display_range : {pandas.DataFrame, pandas.Series, dict}
            The display range as a single row DataFrame, Series or dict with
            columns of 'Start' and 'End' containing the datetime objects or
            ISO8601 text of the times.
        """
        new_workstep = self._branch_current_workstep()
        new_workstep.display_range = display_range
        new_workstep_id = _common.new_placeholder_guid()
        self.worksteps[new_workstep_id] = new_workstep
        self.definition['Current Workstep ID'] = new_workstep_id

    def _get_investigate_range(self):
        # type: () -> (pd.DataFrame, None)
        """
        Get the investigate range of the current workstep

        Returns
        -------
        {pandas.DataFrame, None}
            A pandas DataFrame with the current investigate range in ISO8601
            text in columns of 'Start' and 'End'
        """
        return pd.DataFrame(self.worksteps[self.definition['Current Workstep ID']].investigate_range)

    def _set_investigate_range(self, investigate_range):
        # type: (pd.DataFrame) -> None
        """
        Set the investigate range on the current workstep of the worksheet

        Parameters
        ----------
        investigate_range : {pandas.DataFrame, pandas.Series, dict}
            The investigate range as a single row DataFrame, Series or dict
            with columns of 'Start' and 'End' containing the datetime objects
            or ISO8601 text of the times
        """
        new_workstep = self._branch_current_workstep()
        new_workstep.investigate_range = investigate_range
        new_workstep_id = _common.new_placeholder_guid()
        self.worksteps[new_workstep_id] = new_workstep
        self.definition['Current Workstep ID'] = new_workstep_id

    def _get_date_ranges(self):
        """
        Get the date ranges in the current workstep

        Returns
        -------
        pandas.DataFrame
            A pandas DataFrame with one row per date range
        """
        return self.worksteps[self.definition['Current Workstep ID']].date_ranges

    def _set_date_ranges(self, date_ranges):
        """
        Apply a date range DataFrames as a date ranges in a new workstep

        Parameters
        ----------
        date_ranges : pd.DataFrame
            A DataFrame with rows of date ranges and columns of attributes.
            Valid attributes are

            ===================== =============================================
            Input Column          Date Range Attribute
            ===================== =============================================
            ID                    The id of the date range. If not provided one
                                  will be generated
            Name                  The name of the date range. Eg "Date Range 1"
            Start                 The ISO 8601 string or datetime object start
                                  of the date range
            End                   The ISO 8601 string or datetime object end of
                                  the date range
            Auto Enabled          Boolean if automatic update is enabled
            Auto Duration         The duration of the automatic update sliding
                                  window. Eg, 10min, 1hr, 1d, etc
            Auto Offset           The offset of the automatic update sliding
                                  window. Eg, 10min, 1day, etc
            Auto Offset Direction The direction of the offset. Either 'Past' or
                                  'Future'. Default 'Past'
            Auto Refresh Rate     The automatic refresh rate. Eg, 3s, 1wk, etc
            Condition ID          If using a condition capsule in the time
                                  window, the ID of the condition
            Condition Name        The name of the condition
            Condition Strategy    The for capsule selection. Either "Offset
                                  By" or "Closest To"
            Condition Reference   The reference for the strategy. Either
                                  "Start" or "End"
            Condition Offset      The number of capsules to offset if Condition
                                  Strategy is "Offset By"
        """
        new_workstep = self._branch_current_workstep()
        new_workstep.date_ranges = date_ranges
        new_workstep_id = _common.new_placeholder_guid()
        self.worksteps[new_workstep_id] = new_workstep
        self.definition['Current Workstep ID'] = new_workstep_id

    def _branch_current_workstep(self):
        if 'Current Workstep ID' in self.definition and self.definition['Current Workstep ID']:
            return Workstep(self, definition={'Data': self.worksteps[self.definition['Current Workstep ID']].data})
        else:
            return Workstep(self)

    def _get_display_items(self):
        # type: () -> (pd.DataFrame, None)
        """
        Get the items of a given type displayed on the worksheet at the current workstep, regardless of the worksheet
        view

        Returns
        -------
        {pandas.DataFrame None}
            A list of the items present on the worksheet at the current workstep, or None if there is no current
            workstep ID or the current workstep has no data
        """
        return self.worksteps[self.definition['Current Workstep ID']].display_items

    def _set_display_items(self, items_df):
        # type: (pd.DataFrame) -> None
        """
        Add items to the display pane, optionally removing the current items.
        Items in the input data frame that do not have a known store will be
        skipped.

        Parameters
        ----------
        items_df : {dict, pd.DataFrame, pd.Series}
            A pandas DataFrame with the items to be added to the display. It
            must minimally have an 'ID' column. Display attributes should be
            in named columns as described below

            Type Key:
            Si = Signal, Sc = Scalar, C = Condition, M = Metric, T = Table

            ================= =================================== =============
            Display Attribute Description                         Applicability
            ================= =================================== =============
            Color             A 3-part RGB hexadecimal color spec
                              starting with "#".  E.g. #CE561B    All
            Axis Auto Scale   Boolean if the axis should auto
                              scale                               Si, Sc, M
            Axis Limits       A dict of {'min': float,
                              'max': float} to specify the axis
                              limits. Ignored if Auto Axis Scale
                              is True.                            Si, Sc, M
            Axis Group        An identifier to specify shared
                              axes                                Si, Sc, M
            Lane              The lane a trend is plotted in      Si, Sc, M
            Right Axis        Boolean indicating if the y-axis
                              should be on the right              Si, Sc, M
            Line              The trend line style. Options are
                              ['Solid', 'Dot', 'Short Dash',
                               'Long Dash', 'Short Dash-Dot',
                               'Short Dash-Dot-Dot',
                               'Long Dash-Dot',
                               'Long Dash-Dot-Dot', 'Dash-Dot']   Si, Sc, M
            Line Width        The width of the line.              Si, Sc, M
            Samples           The sample display style. Options
                              are
                              ['Line', 'Line and Sample',
                               'Samples', 'Bars']                 Si
            Stack             Boolean indicating if bars should
                              be stacked                          T
        """

        new_workstep = self._branch_current_workstep()
        new_workstep.display_items = items_df
        temp_id = _common.new_placeholder_guid()
        self.worksteps[temp_id] = new_workstep
        self.definition['Current Workstep ID'] = temp_id

    def _set_worksheet_view(self, view_key='Trend'):
        """
        Set the view of the workstep.

        Parameters
        ----------
        view_key: {'Trend', 'Scorecard', 'Treemap', 'Scatter Plot'}, default 'Trend'
            The desired view for the workstep. Valid values are

            ============ =========================================
            View         Result
            ============ =========================================
            Trend        Show the time-series trend view (default)
            Scatter Plot Show the scatter plot view
            Treemap      Show the treemap view
            Scorecard    Show the scorecard view
            ============ =========================================
        """
        new_workstep = self._branch_current_workstep()
        new_workstep.view = view_key
        temp_id = _common.new_placeholder_guid()
        self.worksteps[temp_id] = new_workstep
        self.definition['Current Workstep ID'] = temp_id

    def _get_worksheet_view(self):
        return self.worksteps[self.definition['Current Workstep ID']].view

    @staticmethod
    def add_display_columns(df, inplace=True):
        """
        Add the display attribute columns to a pandas.DataFrame

        Parameters
        ----------
        df : pandas.DataFrame
            The DataFrame that will have the columns added

        inplace : boolean, default True
            If True, the columns of the DataFrame passed in will be modified and
            None will be returned. If False a copy of df with the new columns
            will be returned

        Returns
        -------
        {None, pandas.DataFrame}
            None if inplace == True. A pandas.DataFrame deep copy with the
            display attribute columns added if inplace == False
        """
        return Workstep._add_display_columns(df, inplace)


class Annotation:
    def __init__(self, worksheet, annotation_type):
        """
        :type worksheet: Worksheet
        """
        self.annotation_type = annotation_type
        self.worksheet = worksheet
        self._html = ''
        self.images = dict()

    def _find_image_references(self):
        if not self.html:
            return list()

        matches = re.finditer(r'src="/api(/annotations/(.*?)/images/(.*?))"', self.html)
        return [(match.group(1), match.group(2), match.group(3)) for match in matches]

    @property
    def html(self):
        return self._html

    @html.setter
    def html(self, value):
        self._set_html(value)

    def _set_html(self, value):
        if value is None:
            self._html = ''
        else:
            self._html = value

    @property
    def referenced_items(self):
        return list()

    @property
    def referenced_worksteps(self):
        return self._find_workstep_references()

    def _find_workstep_references(self):
        return set()

    def find_workbook_links(self):
        if not self.html:
            return dict()

        url = _common.get(self.worksheet.workbook, 'Original Server URL')
        if not url:
            return dict()

        # TODO can this be converted to use the _common.workbook_worksheet_url_regex methods?
        edit_link_no_folder_regex = \
            r'%s/workbook/(?P<workbook>%s)/worksheet/(?P<worksheet>%s)' % (url,
                                                                           _common.GUID_REGEX,
                                                                           _common.GUID_REGEX)

        edit_link_with_folder_regex = \
            r'%s/%s/workbook/(?P<workbook>%s)/worksheet/(?P<worksheet>%s)' % (url,
                                                                              _common.GUID_REGEX,
                                                                              _common.GUID_REGEX,
                                                                              _common.GUID_REGEX)

        view_link_regex = \
            r'%s/view/(?P<worksheet>%s)' % (url, _common.GUID_REGEX)

        present_link_regex = \
            r'%s/present/worksheet/(?P<workbook>%s)/(?P<worksheet>%s)' % (url,
                                                                          _common.GUID_REGEX,
                                                                          _common.GUID_REGEX)

        workstep_tuples = dict()
        for regex in [edit_link_no_folder_regex, edit_link_with_folder_regex, view_link_regex, present_link_regex]:
            matches = re.finditer(regex, self.html, re.IGNORECASE)

            for match in matches:
                group_dict = dict(match.groupdict())
                if 'workbook' not in group_dict:
                    items_api = ItemsApi(_login.client)
                    item_output = items_api.get_item_and_all_properties(
                        id=group_dict['worksheet'])  # type: ItemOutputV1
                    href_regex = r'/workbooks/(?P<workbook>%s)/worksheets/(?P<worksheet>%s)' % (_common.GUID_REGEX,
                                                                                                _common.GUID_REGEX)
                    group_dict['workbook'] = re.fullmatch(href_regex, item_output.href).group('workbook')

                if group_dict['workbook'].upper() not in workstep_tuples:
                    workstep_tuples[group_dict['workbook'].upper()] = set()

                workstep_tuples[group_dict['workbook'].upper()].add(
                    (group_dict['workbook'].upper(), group_dict['worksheet'].upper(), None))

        return workstep_tuples

    def pull(self):
        self.images = dict()
        annotations_api = AnnotationsApi(_login.client)
        annotations = annotations_api.get_annotations(
            annotates=[self.worksheet.id])  # type: AnnotationListOutputV1

        for annotation_item in annotations.items:  # type: AnnotationOutputV1
            annotation_output = annotations_api.get_annotation(id=annotation_item.id)  # AnnotationOutputV1
            if annotation_output.type != self.annotation_type:
                continue

            self._set_html(annotation_output.document)

            image_references = self._find_image_references()
            for query_params, annotation_id, image_id in image_references:
                if (annotation_id, image_id) in self.images:
                    continue

                self.worksheet.workbook.update_status('Pulling image', 1)

                api_client_url = _config.get_api_url()
                request_url = api_client_url + query_params
                response = requests.get(request_url, headers={
                    "Accept": "application/vnd.seeq.v1+json",
                    "x-sq-auth": _login.client.auth_token
                }, verify=_login.https_verify_ssl)

                self.images[(annotation_id, image_id)] = response.content

    def push(self, pushed_workbook_id, pushed_worksheet_id, item_map, push_images):
        annotations_api = AnnotationsApi(_login.client)

        annotations = annotations_api.get_annotations(
            annotates=[pushed_worksheet_id])  # type: AnnotationListOutputV1

        bs = BeautifulSoup(self.html, features='html.parser')
        find_result = bs.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'title'])
        name = 'Unnamed'
        description = None

        if len(find_result) > 0:
            name = ' '.join(re.split(r'[\s\n]+', find_result[0].get_text().strip())[:20])
        if len(find_result) > 1:
            description = ' '.join(re.split(r'[\s\n]+', find_result[1].get_text().strip())[:50])

        new_annotation = AnnotationInputV1()
        new_annotation.document = ''
        new_annotation.name = name if len(name.strip()) > 0 else 'Unnamed'
        new_annotation.description = description
        new_annotation.type = self.annotation_type

        relevant_annotations = [a for a in annotations.items if a.type == self.annotation_type]
        if len(relevant_annotations) == 0:
            new_annotation.interests = [
                AnnotationInterestInputV1(interest_id=pushed_workbook_id),
                AnnotationInterestInputV1(interest_id=pushed_worksheet_id)
            ]

            relevant_annotation = annotations_api.create_annotation(body=new_annotation)  # type: AnnotationOutputV1
        else:
            relevant_annotation = relevant_annotations[0]

        if push_images:
            for query_params, annotation_id, image_id in self._find_image_references():
                api_client_url = _config.get_api_url()
                request_url = api_client_url + '/annotations/%s/images' % relevant_annotation.id

                self.worksheet.workbook.update_status('Pushing image', 1)

                response = requests.post(url=request_url,
                                         files={
                                             "file": (image_id, io.BytesIO(self.images[(annotation_id, image_id)]))
                                         },
                                         headers={
                                             "Accept": "application/vnd.seeq.v1+json",
                                             "x-sq-auth": _login.client.auth_token
                                         },
                                         verify=_login.https_verify_ssl)

                if response.status_code != 201:
                    raise RuntimeError(
                        'Could not upload image file %s for worksheet %d' % (image_id, pushed_worksheet_id))

                link_json = json.loads(response.content)

                item_map['src="/api/annotations/%s/images/%s"' % (annotation_id, image_id)] = \
                    'src="%s"' % link_json['link']

        doc = _replace_items(self.html, item_map)

        # When a workbook is duplicated via the Workbench UI, the workstep links within Journals actually refer to
        # the original workbook. This works in the UI because workstep content has no real dependency on the
        # workbook/worksheet they're associated with. When pulling, we accommodate this by pulling a Workstep and
        # associating it with the "proper" Worksheet object, but then during push we have to fix up the links in case
        # the "original" workbook/worksheet wasn't included in the workbooks to be pushed.
        workstep_link_regex = r'links\?type%sworkstep&amp;workbook%s(%s)&amp;worksheet%s(%s)&amp;' % (
            _common.HTML_EQUALS_REGEX, _common.HTML_EQUALS_REGEX, _common.GUID_REGEX,
            _common.HTML_EQUALS_REGEX, _common.GUID_REGEX)

        workstep_link_replacement = r'links?type=workstep&amp;workbook=%s&amp;worksheet=%s&amp;' % (
            pushed_workbook_id, pushed_worksheet_id
        )

        doc = re.sub(workstep_link_regex, workstep_link_replacement, doc, flags=re.IGNORECASE)

        original_server_url = _common.get(self.worksheet.workbook, 'Original Server URL')
        new_server_url = _get_canonical_server_url()
        if len(doc) > 0 and original_server_url:
            doc = doc.replace(original_server_url, new_server_url)

        new_annotation.document = doc
        new_annotation.interests = list()
        for interest in relevant_annotation.interests:  # type: AnnotationInterestOutputV1
            interest_item = interest.item  # type: ItemPreviewV1
            # At Chevron, we encountered a case where there were multiple interests returned with the same ID, which
            # caused Appserver to choke when updating the annotation. So filter those out.
            if any(interest_item.id == i.interest_id for i in new_annotation.interests):
                continue
            new_interest = AnnotationInterestInputV1()
            new_interest.interest_id = interest_item.id
            new_interest.detail_id = interest.capsule
            new_annotation.interests.append(new_interest)
        new_annotation.created_by_id = relevant_annotation.created_by.id

        return annotations_api.update_annotation(
            id=relevant_annotation.id, body=new_annotation)  # type: AnnotationOutputV1

    def _get_annotation_html_file(self, workbook_folder):
        return os.path.join(workbook_folder, '%s_%s.html' % (self.annotation_type, self.worksheet.id))

    @staticmethod
    def _get_image_file(workbook_folder, image_id_tuple):
        return os.path.join(workbook_folder, 'Image_%s_%s' % image_id_tuple)

    @staticmethod
    def _get_html_attr(fragment, attribute):
        attr_match = re.findall(r'\s+%s="(.*?)"' % attribute, fragment)
        return attr_match[0] if len(attr_match) > 0 else None

    def save(self, workbook_folder):
        journal_html_file = self._get_annotation_html_file(workbook_folder)
        with open(journal_html_file, 'w', encoding='utf-8') as f:
            if self.html:
                if options.pretty_print_html:
                    html_to_save = BeautifulSoup(self.html, features='html.parser').prettify()
                    # If we don't trim the spaces within <a> tags, you'll get extra spaces underlined in the UI
                    html_to_save = re.sub(r'(<a .*?>)[\s\n]+(.*?)[\s\n]+(</a>)', r'\1\2\3', html_to_save)
                else:
                    html_to_save = self.html

                f.write(html_to_save)

        for image_id_tuple, content in self.images.items():
            image_file = Journal._get_image_file(workbook_folder, image_id_tuple)
            with open(image_file, 'wb') as f:
                f.write(content)

    def _load(self, workbook_folder):
        journal_html_file = self._get_annotation_html_file(workbook_folder)

        with open(journal_html_file, 'r', encoding='utf-8') as f:
            self.html = f.read()

        matches = re.finditer(r'src="/api(/annotations/(.*?)/images/(.*?))"', self.html)
        for match in matches:
            image_id_tuple = (match.group(2), match.group(3))
            image_file = Journal._get_image_file(workbook_folder, image_id_tuple)

            with open(image_file, 'rb') as f:
                self.images[image_id_tuple] = f.read()

    def add_image(self, image_path, placement='end'):
        """
        Add an image to the annotation.

        Parameters
        ----------
        image_path: str
            The full path to the image file
        placement : {'end', 'beginning'}, default 'end'
            The location to add the image to an existing document. If the
            placement is not understood, the default will be used.
        """
        html = self.html
        placeholder_id = _common.new_placeholder_guid()
        image_name = os.path.basename(image_path)
        image_html = f'<img src="/api/annotations/{placeholder_id}/images/{image_name}">'
        if placement == 'beginning':
            html = image_html + html
        else:
            html += image_html
        self._set_html(html)
        with open(image_path, 'rb') as img:
            self.images[(placeholder_id, image_name)] = img.read()


class Journal(Annotation):
    def __init__(self, worksheet):
        super().__init__(worksheet, 'Journal')

    @staticmethod
    def load(worksheet, workbook_folder):
        journal = Journal(worksheet)
        journal._load(workbook_folder)
        return journal

    @property
    def referenced_items(self):
        referenced_items = list()
        if self.html:
            matches = re.finditer(r'item%s(%s)' % (_common.HTML_EQUALS_REGEX, _common.GUID_REGEX), self.html,
                                  re.IGNORECASE)
            for match in matches:
                referenced_items.append(Reference(match.group(1).upper(), Reference.JOURNAL, self.worksheet))

        return referenced_items

    def _find_workstep_references(self):
        if not self.html:
            return set()

        workstep_references = set()
        regex = r'workbook%s(%s)&amp;worksheet%s(%s)&amp;workstep%s(%s)' % (
            _common.HTML_EQUALS_REGEX, _common.GUID_REGEX,
            _common.HTML_EQUALS_REGEX, _common.GUID_REGEX,
            _common.HTML_EQUALS_REGEX, _common.GUID_REGEX)
        matches = re.finditer(regex, self.html, re.IGNORECASE)

        for match in matches:
            workstep_references.add((match.group(1).upper(), match.group(2).upper(), match.group(3).upper()))

        return workstep_references


class Report(Annotation):
    def __init__(self, worksheet):
        super().__init__(worksheet, 'Report')

    @staticmethod
    def load(worksheet, workbook_folder):
        report = Report(worksheet)
        report._load(workbook_folder)
        return report

    def _find_workstep_references(self):
        if not self.html:
            return set()

        workstep_references = set()
        link_matches = re.finditer(r'<a .*?</a>', self.html, re.IGNORECASE)
        for link_match in link_matches:
            link_html = link_match.group(0)
            href_regex = r'.*href="\/view\/worksheet\/(%s)\/(%s)\?workstepId%s(%s).*?".*' % (
                _common.GUID_REGEX, _common.GUID_REGEX, _common.HTML_EQUALS_REGEX, _common.GUID_REGEX)
            href_match = re.match(href_regex, link_html)
            if href_match:
                workstep_references.add((href_match.group(1).upper(),
                                         href_match.group(2).upper(),
                                         href_match.group(3).upper()))

        img_matches = re.finditer(r'<img .*?>', self.html, re.IGNORECASE)
        for img_match in img_matches:
            img_html = img_match.group(0)
            data_seeq_workbookid = Annotation._get_html_attr(img_html, 'data-seeq-workbookid')
            data_seeq_worksheetid = Annotation._get_html_attr(img_html, 'data-seeq-worksheetid')
            data_seeq_workstepid = Annotation._get_html_attr(img_html, 'data-seeq-workstepid')
            if data_seeq_workbookid and data_seeq_worksheetid and data_seeq_workstepid:
                workstep_references.add((data_seeq_workbookid.upper(),
                                         data_seeq_worksheetid.upper(),
                                         data_seeq_workstepid.upper()))

        return workstep_references


class Reference:
    JOURNAL = 'Journal'
    DETAILS = 'Details'
    SCOPED = 'Scoped'
    DEPENDENCY = 'Dependency'
    ANCILLARY = 'Ancillary'
    EMBEDDED_CONTENT = 'Embedded Content'

    def __init__(self, _id, _provenance, worksheet=None):
        """
        :type _id: str
        :type _provenance: str
        :type worksheet: Worksheet
        """
        self.id = _id
        self.provenance = _provenance
        self.worksheet = worksheet

    def __repr__(self):
        if self.worksheet is not None:
            return '%s reference on "%s" (%s)' % (self.provenance, self.worksheet.name, self.id)
        else:
            return '%s (%s)' % (self.provenance, self.id)


class Workstep(Item):
    def __init__(self, worksheet, definition=None):
        super().__init__(definition)

        self.worksheet = worksheet
        if 'ID' not in self.definition:
            self.definition['ID'] = _common.new_placeholder_guid()
            self.worksheet.worksteps[self.definition['ID']] = self
        if 'Data' not in self.definition:
            self.definition['Data'] = json.loads(_common.DEFAULT_WORKBOOK_STATE)

        # initialize displayed items
        if self.display_items.empty:
            display_items_stores = self._store_map_from_type('all')
            stores = self.get_workstep_stores()
            for store in display_items_stores:
                current_store = _common.get(stores, store, default=dict(), assign_default=True)
                current_store['items'] = []

        # initialize the display and investigate ranges
        if self.display_range is None:
            self._set_display_range(pd.DataFrame([{'Start': pd.datetime.now() - pd.Timedelta(days=1),
                                                   'End': pd.datetime.now()}]))
        if self.investigate_range is None:
            self._set_investigate_range(pd.DataFrame([{'Start': pd.datetime.now() - pd.Timedelta(days=7),
                                                       'End': pd.datetime.now()}]))
        # initialize the view
        if self.view is None:
            self._set_view_key()

    @staticmethod
    def pull(workstep_tuple, *, worksheet=None):
        # Note that worksteps from other workbooks/worksheets can be referenced in Journals due to copy/paste
        # operations, so we can't assume that this workstep's self.worksheet actually represents the one to pull.
        workbook_id, worksheet_id, workstep_id = workstep_tuple
        workstep = Workstep(worksheet, {'ID': workstep_id})
        workstep._pull(workstep_tuple)
        return workstep

    def _pull(self, workstep_tuple):
        workbook_id, worksheet_id, workstep_id = workstep_tuple
        workbooks_api = WorkbooksApi(_login.client)
        workstep_output = workbooks_api.get_workstep(workbook_id=workbook_id,
                                                     worksheet_id=worksheet_id,
                                                     workstep_id=workstep_id)  # type: WorkstepOutputV1

        self.definition['Data'] = json.loads(workstep_output.data)

    def push_to_specific_worksheet(self, pushed_workbook_id, pushed_worksheet_id, item_map):
        workbooks_api = WorkbooksApi(_login.client)

        item_map = item_map if item_map is not None else dict()

        workstep_input = WorkstepInputV1()
        if self.data:
            workstep_input.data = _replace_items(json.dumps(self.data), item_map)

        workstep_output = workbooks_api.create_workstep(
            workbook_id=pushed_workbook_id, worksheet_id=pushed_worksheet_id,
            body=workstep_input)  # type: WorkstepOutputV1

        item_map[self.id.upper()] = workstep_output.id.upper()

        # Look at all referenced items on this workstep to see if there ancillaries and if so, push them. Note that
        # we only push ancillaries that are actually referenced by a workstep so that we conserve on how many
        # StoredSignals we actually touch.
        for referenced_item in self.referenced_items:  # type: Reference
            if referenced_item.id not in self.worksheet.workbook.item_inventory:
                # There are lots of IDs in a workstep that may not be relevant items for export
                continue

            item = self.worksheet.workbook.item_inventory[referenced_item.id]
            if 'Ancillaries' in item:
                if isinstance(item, StoredOrCalculatedItem):
                    try:
                        item.push_ancillaries(self.worksheet.workbook.id, pushed_workbook_id, item_map)
                    except KeyboardInterrupt:
                        raise
                    except BaseException as e:
                        self.worksheet.workbook.item_errors.add((item, _common.format_exception(e)))

        return workstep_output.id

    @property
    def data(self):
        return _common.get(self.definition, 'Data', default=dict())

    @property
    def referenced_items(self):
        referenced_items = list()

        matches = re.finditer(_common.GUID_REGEX, json.dumps(self.data), re.IGNORECASE)

        for match in matches:
            referenced_items.append(Reference(match.group(0).upper(), Reference.DETAILS, self.worksheet))

        return referenced_items

    @property
    def display_items(self):
        return self._get_display_items()

    @display_items.setter
    def display_items(self, value):
        self._set_display_items(value)

    @property
    def display_range(self):
        return self._get_display_range()

    @display_range.setter
    def display_range(self, value):
        self._set_display_range(value)

    @property
    def investigate_range(self):
        return self._get_investigate_range()

    @investigate_range.setter
    def investigate_range(self, value):
        self._set_investigate_range(value)

    @property
    def date_ranges(self):
        return self._get_date_ranges()

    @date_ranges.setter
    def date_ranges(self, value):
        self._set_date_ranges(value)

    @property
    def view(self):
        return self._get_view_key()

    @view.setter
    def view(self, value):
        self._set_view_key(value)

    def get_workstep_stores(self):
        workstep_data = _common.get(self.definition, 'Data', default=dict(), assign_default=True)
        workstep_state = _common.get(workstep_data, 'state', default=dict(), assign_default=True)
        return _common.get(workstep_state, 'stores', default=dict(), assign_default=True)

    @staticmethod
    def _get_workstep_json_file(workbook_folder, worksheet_id, workstep_id):
        return os.path.join(workbook_folder, 'Worksheet_%s_Workstep_%s.json' % (worksheet_id, workstep_id))

    def save(self, workbook_folder):
        workstep_json_file = Workstep._get_workstep_json_file(workbook_folder, self.worksheet.id, self.id)
        with open(workstep_json_file, 'w', encoding='utf-8') as f:
            json.dump(self.definition, f, indent=4)

    def _load(self, workbook_folder, workstep_id):
        workstep_json_file = Workstep._get_workstep_json_file(workbook_folder, self.worksheet.id, workstep_id)

        with open(workstep_json_file, 'r', encoding='utf-8') as f:
            self.definition = json.load(f)

    @staticmethod
    def load_from_workbook_folder(worksheet, workbook_folder, workstep_id):
        workstep = Workstep(worksheet)
        workstep._load(workbook_folder, workstep_id)
        return workstep

    def _get_store(self, store_name):
        workstep_stores = self.get_workstep_stores()
        return _common.get(workstep_stores, store_name, default=dict(), assign_default=True)

    def _get_display_range(self):
        duration_store = self._get_store('sqDurationStore')
        display_range = _common.get(duration_store, 'displayRange', default=dict())
        if not display_range:
            return None
        start = pd.datetime.fromtimestamp(display_range['start'] / 1000)
        end = pd.datetime.fromtimestamp(display_range['end'] / 1000)
        return pd.DataFrame([{'Start': start.isoformat(), 'End': end.isoformat()}])

    def _set_display_range(self, display_start_end):
        if isinstance(display_start_end, pd.DataFrame):
            if len(display_start_end) > 1:
                raise RuntimeError('Display Range DataFrames are limited to one row')
            display_start_end = display_start_end.squeeze()
        start_ts = display_start_end['Start']
        end_ts = display_start_end['End']

        if isinstance(start_ts, str):
            start_ts = pd.datetime.fromisoformat(start_ts).timestamp() * 1000
        else:
            start_ts = start_ts.timestamp() * 1000
        if isinstance(end_ts, str):
            end_ts = pd.datetime.fromisoformat(end_ts).timestamp() * 1000
        else:
            end_ts = end_ts.timestamp() * 1000

        duration_store = self._get_store('sqDurationStore')

        auto_update = _common.get(duration_store, 'autoUpdate', default=dict(), assign_default=True)
        auto_update['offset'] = end_ts - pd.datetime.now().timestamp() * 1000

        display_range = _common.get(duration_store, 'displayRange', default=dict(), assign_default=True)
        display_range['start'] = start_ts
        display_range['end'] = end_ts

    def _get_investigate_range(self):
        duration_store = self._get_store('sqDurationStore')
        investigate_range = _common.get(duration_store, 'investigateRange', default=None)
        if investigate_range is None:
            return None
        start = pd.datetime.fromtimestamp(investigate_range['start'] / 1000).isoformat()
        end = pd.datetime.fromtimestamp(investigate_range['end'] / 1000).isoformat()
        return pd.DataFrame([{'Start': start, 'End': end}])

    def _set_investigate_range(self, investigate_start_end):
        if isinstance(investigate_start_end, pd.DataFrame):
            if len(investigate_start_end) > 1:
                raise RuntimeError('Investigate Range DataFrames are limited to one row ')
            investigate_start_end = investigate_start_end.squeeze()
        start_ts = investigate_start_end['Start']
        end_ts = investigate_start_end['End']

        if isinstance(start_ts, str):
            start_ts = pd.datetime.fromisoformat(start_ts).timestamp() * 1000
        else:
            start_ts = start_ts.timestamp() * 1000
        if isinstance(end_ts, str):
            end_ts = pd.datetime.fromisoformat(end_ts).timestamp() * 1000
        else:
            end_ts = end_ts.timestamp() * 1000

        duration_store = self._get_store('sqDurationStore')
        duration_store['investigateRange'] = {'start': start_ts, 'end': end_ts}

    def _get_date_ranges(self):
        report_store = self._get_store('sqReportStore')
        date_variables = _common.get(report_store, 'dateVariables', default=None)
        if date_variables is None:
            return None
        output_dates = [Workstep._date_range_workstep_to_user(d) for d in date_variables]
        return pd.DataFrame(output_dates)

    @staticmethod
    def _date_range_workstep_to_user(date_range):
        dr_columns = ['ID', 'Name', 'Start', 'End', 'Auto Enabled', 'Auto Duration', 'Auto Offset',
                      'Auto Offset Direction', 'Auto Refresh Rate', 'Condition ID', 'Condition Name',
                      'Condition Strategy', 'Condition Reference', 'Condition Offset']
        dr = {c: pd.np.nan for c in dr_columns}

        dr['ID'] = date_range['id']
        dr['Name'] = date_range['name']
        if 'range' in date_range:
            _common.test_and_set(dr, 'Start', date_range['range'], 'start')
            _common.test_and_set(dr, 'End', date_range['range'], 'end')
        if 'auto' in date_range:
            _common.test_and_set(dr, 'Auto Enabled', date_range['auto'], 'enabled')
            _common.test_and_set(dr, 'Auto Duration', date_range['auto'], 'duration', lambda x: str(x / 1000) + 's')
            if 'offset' in date_range['auto']:
                _offset = date_range['auto']['offset']
                if 'value' in _offset and 'units' in _offset:
                    dr['Auto Offset'] = str(_offset['value']) + _offset['units']
            _common.test_and_set(dr, 'Auto Offset Direction', date_range['auto'], 'offsetDirection',
                                 lambda x: str.capitalize(x))
            if 'rate' in date_range['auto']:
                _rate = date_range['auto']['rate']
                if 'value' in _rate and 'units' in _rate:
                    dr['Auto Refresh Rate'] = str(_rate['value']) + _rate['units']
        if 'condition' in date_range:
            _common.test_and_set(dr, 'Condition ID', date_range['condition'], 'id')
            _common.test_and_set(dr, 'Condition Name', date_range['condition'], 'name')
            if 'strategy' in date_range['condition']:
                if date_range['condition']['strategy'] == 'closestTo':
                    dr['Condition Strategy'] = 'Closest To'
                elif date_range['condition']['strategy'] == 'offsetBy':
                    dr['Condition Strategy'] = 'Offset By'
            _common.test_and_set(dr, 'Condition Reference', date_range['condition'], 'reference',
                                 lambda x: str.capitalize(x))
            _common.test_and_set(dr, 'Condition Offset', date_range['condition'], 'offset')
        return dr

    def _set_date_ranges(self, date_ranges):
        date_range_list = list()
        for _, d in date_ranges.iterrows():
            Workstep._validate_user_date_range(d)
            date_range_list.append(Workstep._date_range_user_to_workstep(d))
        report_store = self._get_store('sqReportStore')
        report_store['dateVariables'] = date_range_list

    @staticmethod
    def _date_range_user_to_workstep(date_range):
        """
        Converts a user specified date range to a dict for inclusion in the workstep. See _set_date_ranges
        for parameter explanation
        :param date_range: dict, single row pd.DataFrame, pd.Series
        :return: dict workstep daterange
        """

        # convert DataFrames and Series to a dict
        if isinstance(date_range, pd.DataFrame):
            if len(date_range) > 1:
                raise RuntimeError('This method can only accept one row of a DataFrame at a time')
            date_range = date_range.squeeze()
        if isinstance(date_range, pd.Series):
            date_range = date_range.to_dict()

        # defaults for the different aspects of the date range
        def _defaults(c_dr):
            _common.test_and_set(c_dr, 'id', date_range, 'ID', default_value=_common.new_placeholder_guid(),
                                 retain_target=False)
            c_dr['name'] = date_range['Name']

        def _range_defaults(c_dr):
            _range = _common.get(c_dr, 'range', default=dict(), assign_default=True)
            _range['start'] = (pd.datetime.now() - pd.Timedelta(days=1)).timestamp() * 1000
            _range['end'] = pd.datetime.now().timestamp() * 1000

        def _auto_defaults(c_dr):
            _auto = _common.get(c_dr, 'auto', default=dict(), assign_default=True)
            _auto['enabled'] = False
            _auto['duration'] = pd.Timedelta(days=1).total_seconds() * 1000
            _auto['offset'] = dict()
            _auto['offset']['value'] = 0
            _auto['offset']['units'] = 'min'
            _auto['offsetDirection'] = 'past'
            _auto['rate'] = dict()
            _auto['rate']['value'] = 5
            _auto['rate']['units'] = 'min'

        def _condition_defaults(c_dr):
            _condition = _common.get(c_dr, 'condition', default=dict(), assign_default=True)
            _condition['strategy'] = 'closestTo'
            _condition['reference'] = 'end'
            _condition['offset'] = 1

        dr = dict()
        _defaults(dr)
        _range_defaults(dr)
        _auto_defaults(dr)
        _condition_defaults(dr)
        _common.test_and_set(dr['range'], 'start', date_range, 'Start')
        _common.test_and_set(dr['range'], 'end', date_range, 'End')
        _common.test_and_set(dr['auto'], 'enabled', date_range, 'Auto Enabled', )
        _common.test_and_set(dr['auto'], 'duration', date_range, 'Auto Duration',
                             lambda x: _common.parse_str_time_to_ms(x)[2])
        _common.test_and_set(dr['auto']['offset'], 'value', date_range, 'Auto Offset',
                             lambda x: _common.parse_str_time_to_ms(x)[0])
        _common.test_and_set(dr['auto']['offset'], 'units', date_range, 'Auto Offset',
                             lambda x: _common.parse_str_time_to_ms(x)[1])
        _common.test_and_set(dr['auto'], 'offsetDirection', date_range, 'Auto Offset Direction', lambda x: str.lower(x))
        _common.test_and_set(dr['auto']['rate'], 'value', date_range, 'Auto Refresh Rate',
                             lambda x: _common.parse_str_time_to_ms(x)[0])
        _common.test_and_set(dr['auto']['rate'], 'units', date_range, 'Auto Refresh Rate',
                             lambda x: _common.parse_str_time_to_ms(x)[1])
        _common.test_and_set(dr['condition'], 'offset', date_range, 'Condition Offset', lambda x: str.lower(x))
        _common.test_and_set(dr['condition'], 'strategy', date_range, 'Condition Strategy', lambda x: str.lower(x))
        _common.test_and_set(dr['condition'], 'reference', date_range, 'Condition Reference', lambda x: str.lower(x))
        _common.test_and_set(dr['condition'], 'id', date_range, 'Condition ID')
        _common.test_and_set(dr['condition'], 'name', date_range, 'Condition Name')
        return dr

    @staticmethod
    def _validate_user_date_range(date_range):
        errors = []
        if 'Name' not in date_range:
            raise RuntimeError('All date ranges require a "Name"')
        # if auto enabled is defined, all the other auto fields must be defined.
        if 'Auto Enabled' in date_range and date_range['Auto Enabled']:
            if 'Auto Offset' not in date_range:
                errors.append('"Auto Offset" is required if "Auto Enabled" is True')
            if 'Auto Duration' not in date_range:
                errors.append('"Auto Duration" is required if "Auto Enabled" is True')
            if 'Auto Offset Direction' not in date_range:
                errors.append('"Auto Offset Direction" is required if "Auto Enabled" is True')
        if 'Condition ID' in date_range or 'Condition Name' in date_range:
            if 'Condition ID' not in date_range:
                errors.append('"Condition ID" must be supplied with "Condition Name"')
            if 'Condition Name' not in date_range:
                errors.append('"Condition Name" must be supplied with "Condition ID"')
            if 'Condition Strategy' not in date_range:
                errors.append('"Condition Strategy" must be supplied with "Condition Name" and "Condition ID"')
            if 'Condition Offset' not in date_range:
                errors.append('"Condition Offset" must be supplied with "Condition Name" and "Condition ID"')
            if 'Condition Reference' not in date_range:
                errors.append('"Condition Reference" must be supplied with "Condition Name" and "Condition ID"')
        if errors:
            msg = f'There was 1 error ' if len(errors) == 1 else f'There were {len(errors)} errors '
            msg += f'detected in date range "{date_range["Name"]}": {errors}'
            raise RuntimeError(msg)

    @staticmethod
    def _validate_input(df):
        if any(df.duplicated(['ID'])):
            return False
        return True

    def _set_display_items(self, items_df):
        if not Workstep._validate_input(items_df):
            raise RuntimeError("The items set as display items are not valid. Was an item repeated?")
        workstep_stores = self.get_workstep_stores()

        # get the axes identifiers and convert them to the canonical "A", "B", "C"...
        axis_map = dict()
        if _common.present(items_df, 'Axis Group'):
            axis_map = Workstep._generate_axis_map(items_df['Axis Group'])

        # clear all items from the workstep
        for store_name in self._store_map_from_type('all'):
            store = _common.get(workstep_stores, store_name, default=dict(), assign_default=True)
            store['items'] = []

        lanes = set()
        axes = set()
        for _, item in items_df.iterrows():
            store_name = self._store_map_from_type(item['Type'])
            if not store_name:
                continue
            store_items = _common.get(workstep_stores, store_name)['items']
            store_items.append(dict())
            store_items[-1]['name'] = item['Name']
            store_items[-1]['id'] = item['ID']
            for column in item.keys():
                if column in self._workstep_display_user_to_workstep:
                    value = _common.get(item, column)
                    if pd.notna(value):
                        if column == 'Line':
                            value = self._workstep_dashStyle_user_to_workstep[value]
                        elif column == 'Samples':
                            value = self._workstep_sampleDisplay_user_to_workstep[value]
                        elif column == 'Axis Group':
                            value = axis_map[value]
                            axes.add(value)
                        elif column == 'Lane':
                            value = int(value) if int(value) > 0 else 1
                            lanes.add(value)
                        elif column == 'Line Width':
                            value = value if value > 0 else 1
                        store_items[-1][self._workstep_display_user_to_workstep[column]] = value
            if 'lane' not in store_items[-1]:
                if lanes:
                    store_items[-1]['lane'] = max(lanes) + 1
                else:
                    store_items[-1]['lane'] = 1
                lanes.add(store_items[-1]['lane'])
            if 'axisAlign' not in store_items[-1]:
                if axes:
                    max_axis_number = max(list(map(lambda x: Workstep.axes_number_from_identifier(x), list(axes))))
                    store_items[-1]['axisAlign'] = Workstep.axes_identifier_from_number(max_axis_number + 1)
                else:
                    store_items[-1]['axisAlign'] = 'A'
                axes.add(store_items[-1]['axisAlign'])

    def _get_display_items(self, item_type='all'):
        """
        Get the items of a given type displayed in the workstep, regardless of the worksheet view.

        Parameters
        ----------
        item_type : {'all', 'signals', 'conditions', 'scalars', 'metrics', 'tables'}, default 'all'
            The type of items to return.

        Returns
        -------
        {pandas.DataFrame, None}
            A list of the items present in the workstep or None if there is not workstep.data
        """
        if not self.data:
            return

        stores = list()
        if item_type in ['all', 'signals']:
            stores.append('sqTrendSeriesStore')
        if item_type in ['all', 'conditions']:
            stores.append('sqTrendCapsuleSetStore')
        if item_type in ['all', 'scalars']:
            stores.append('sqTrendScalarStore')
        if item_type in ['all', 'metrics']:
            stores.append('sqTrendMetricStore')
        if item_type in ['all', 'tables']:
            stores.append('sqTrendTableStore')

        workstep_stores = self.get_workstep_stores()
        items = list()
        for store in stores:
            workstep_store = self._get_store(store)
            for item in _common.get(workstep_store, 'items', default=list(), assign_default=True):
                output_item = dict()
                output_item['Name'] = item['name']
                output_item['ID'] = item['id']
                output_item['Type'] = Workstep._type_from_store_name(store)
                for k in self._workstep_display_workstep_to_user.keys():
                    if k in item:
                        value = item[k]
                        if k == 'dashStyle':
                            output_item[self._workstep_display_workstep_to_user[k]] = \
                                self._workstep_dashStyle_workstep_to_user[value]
                        elif k == 'sampleDisplayOption':
                            output_item[self._workstep_display_workstep_to_user[k]] = \
                                self._workstep_sampleDisplay_workstep_to_user[value]
                        else:
                            output_item[self._workstep_display_workstep_to_user[k]] = value
                items.append(output_item)
        return pd.DataFrame(items)

    @staticmethod
    def _store_map_from_type(item_type):
        """
        Return a list with the name of the workstep store corresponding to the item type give.
        :param item_type: The string type of the item. If 'all' all stores will be returned
        :return: str store name, for all item_types except 'all'. If item_type == 'all', a tuple of all the store
        names. If item_type is not recognized, returns None.
        """
        if not item_type or not isinstance(item_type, str):
            return None

        if 'Signal' in item_type:
            return 'sqTrendSeriesStore'
        if 'Condition' in item_type:
            return 'sqTrendCapsuleSetStore'
        if 'Scalar' in item_type:
            return 'sqTrendScalarStore'
        if 'Metric' in item_type:
            return 'sqTrendMetricStore'
        if 'Table' in item_type:
            return 'sqTrendTableStore'
        if item_type == 'all':
            return ('sqTrendSeriesStore', 'sqTrendCapsuleSetStore', 'sqTrendScalarStore', 'sqTrendMetricStore',
                    'sqTrendTableStore')
        else:
            return None

    @staticmethod
    def _type_from_store_name(store_name):
        """
        Return the type of an item that is stored in a given data store
        Parameters
        ----------
        store_name : str
            The name of the data store

        Returns
        -------
        str
            The item type
        """
        if not store_name or not isinstance(store_name, str):
            return None

        store_map = {
            'sqTrendSeriesStore': 'Signal',
            'sqTrendCapsuleSetStore': 'Condition',
            'sqTrendScalarStore': 'Scalar',
            'sqTrendMetricStore': 'Metric',
            'sqTrendTableStore': 'Table'
        }

        if store_name not in store_map:
            return None

        return store_map[store_name]

    _workstep_display_user_to_workstep = {
        'Color': 'color',
        'Line': 'dashStyle',
        'Line Width': 'lineWidth',
        'Lane': 'lane',
        'Axis': 'axisAlign',
        'Samples': 'sampleDisplayOption',
        'Axis Auto Scale': 'axisAutoScale',
        'Axis Limits': 'yAxisConfig',
        'Right Axis': 'rightAxis',
        'Axis Group': 'axisAlign',
        'Stack': 'stack'
    }

    _workstep_display_workstep_to_user = dict((v, k) for k, v in _workstep_display_user_to_workstep.items())

    _workstep_sampleDisplay_user_to_workstep = {
        'Line': 'line',
        'Line and Sample': 'lineAndSample',
        'Samples': 'sample',
        'Bars': 'bar'
    }

    _workstep_sampleDisplay_workstep_to_user = dict((v, k) for k, v in _workstep_sampleDisplay_user_to_workstep.items())

    _workstep_dashStyle_user_to_workstep = {
        'Solid': 'Solid',
        'Short Dash': 'ShortDash',
        'Short Dash-Dot': 'ShortDashDot',
        'Short Dash-Dot-Dot': 'ShortDashDotDot',
        'Dot': 'Dot',
        'Dash': 'Dash',
        'Long Dash': 'LongDash',
        'Dash-Dot': 'DashDot',
        'Long Dash-Dot': 'LongDashDot',
        'Long Dash-Dot-Dot': 'LongDashDotDot'
    }

    _workstep_dashStyle_workstep_to_user = dict((v, k) for k, v in _workstep_dashStyle_user_to_workstep.items())

    @staticmethod
    def _generate_axis_map(axis_group):
        specified_axes = axis_group.dropna().drop_duplicates().to_list()
        canonical_axes = list(Workstep.axes_identifier_list_from_number(len(specified_axes)))
        axis_map = dict()
        for ax in specified_axes:
            if ax in canonical_axes:
                axis_map[ax] = ax
                canonical_axes.remove(ax)
                continue
            else:
                axis_map[ax] = canonical_axes[0]
                del canonical_axes[0]
        return axis_map

    @staticmethod
    def axes_identifier_list_from_number(n):
        """
        A Generator that produces a canonical list of axes identifiers of the
        form "A", "B", "C",..., "AA", "AB", "AC",...
        Parameters
        ----------
        n : integer
            The number of identifiers required.

        Returns
        -------
        str
            The string for the current axis identifier.
        """
        generated = 0

        while generated < n:
            yield Workstep.axes_identifier_from_number(generated)
            generated += 1

    @staticmethod
    def axes_identifier_from_number(number):
        decimal_a, number_letters = 65, 26

        if number >= number_letters:
            return Workstep.axes_identifier_from_number(number // number_letters - 1) + \
                   chr(number % number_letters + decimal_a)
        else:
            return chr(number % number_letters + decimal_a)

    @staticmethod
    def axes_number_from_identifier(axis_id):
        """
        Converts from an alpha axis identifier, eg "A", "B",...,"AA", "AB",...
        to a decimal, essentially doing a conversion from base 26 to base 10.

        Parameters
        ----------
        axis_id: str
            The alpha identifier

        Returns
        -------
        int
            Integer base 10 equivalent
        """
        decimal_a, number_letters = 65, 26
        base_26_multipliers = [ord(i) + 1 - decimal_a for i in axis_id]
        base_10_components = \
            [b26 * number_letters ** (len(base_26_multipliers) - 1 - i) for i, b26 in enumerate(base_26_multipliers)]
        return sum(base_10_components)

    @staticmethod
    def _add_display_columns(df, inplace):
        """
        See documentation for Worksheet.add_display_attribute_columns
        """
        working_df = df.copy(deep=True) if not inplace else df

        for attribute in Workstep._workstep_display_user_to_workstep.keys():
            if attribute not in working_df:
                working_df[attribute] = pd.np.nan

        return None if inplace else working_df

    def _get_view_key(self):
        """
        Get the view of the current workstep. If no view key is found the default value is returned
        :return: str view key
        """
        workstep_stores = self.get_workstep_stores()
        worksheet_store = _common.get(workstep_stores, 'sqWorksheetStore', default=dict(), assign_default=True)
        if 'viewKey' in workstep_stores:
            return self._view_key_workstep_to_user[worksheet_store['viewKey']]
        else:
            return None

    def _set_view_key(self, view='Trend'):
        if view not in self._view_key_user_to_workstep.keys():
            raise RuntimeError(f'The view key "{view}" is not recognized. Valid values are '
                               f'{self._view_key_user_to_workstep.keys()}')

        workstep_stores = self.get_workstep_stores()
        worksheet_store = _common.get(workstep_stores, 'sqWorksheetStore', default=dict(), assign_default=True)
        worksheet_store['viewKey'] = self._view_key_user_to_workstep[view]

    _view_key_user_to_workstep = {
        'Scorecard': 'SCORECARD',
        'Treemap': 'TREEMAP',
        'Scatter Plot': 'SCATTER',
        'Trend': 'TREND'
    }
    _view_key_workstep_to_user = dict((v, k) for k, v in _view_key_user_to_workstep.items())


class StoredOrCalculatedItem(Item):
    def push(self, datasource_maps, *, pushed_workbook_id=None, item_map=None, label=None, override_max_interp=False):
        raise RuntimeError('Pushed called but StoredOrCalculatedItem.push() not overloaded')

    def push_ancillaries(self, original_workbook_id, pushed_workbook_id, item_map):
        if 'Ancillaries' not in self:
            return

        items_api = ItemsApi(_login.client)
        pushed_item = items_api.get_item_and_all_properties(id=item_map[self.id])  # type: ItemOutputV1

        ancillaries_api = AncillariesApi(_login.client)

        for ancillary_dict in self['Ancillaries']:
            if _common.get(ancillary_dict, 'Scoped To') not in [None, original_workbook_id]:
                continue

            found_item_ancillary_output = None
            for item_ancillary_output in pushed_item.ancillaries:  # type: ItemAncillaryOutputV1
                if item_ancillary_output.name == ancillary_dict['Name'] and \
                        item_ancillary_output.scoped_to == pushed_workbook_id:
                    found_item_ancillary_output = item_ancillary_output
                    break

            ancillary_input = AncillaryInputV1()
            ancillary_input.name = ancillary_dict['Name']
            ancillary_input.scoped_to = pushed_workbook_id
            ancillary_input.item_id = pushed_item.id

            ancillary_input.ancillaries = list()
            for ancillary_item_dict in ancillary_dict['Items']:
                ancillary_item_input = AncillaryItemInputV1()
                if ancillary_item_dict['ID'] not in item_map:
                    raise DependencyNotFound(ancillary_item_dict['ID'])

                ancillary_item_input.id = item_map[ancillary_item_dict['ID']]
                ancillary_item_input.name = ancillary_item_dict['Name']
                ancillary_item_input.order = ancillary_item_dict['Order']
                ancillary_input.ancillaries.append(ancillary_item_input)

            if found_item_ancillary_output is None:
                ancillaries_api.create_ancillary(body=ancillary_input)
            else:
                ancillaries_api.update_ancillary(id=found_item_ancillary_output.id,
                                                 body=ancillary_input)

    @staticmethod
    def _find_datasource_name(datasource_class, datasource_id, datasource_maps):
        for datasource_map in datasource_maps:
            if datasource_map['Datasource Class'] == datasource_class and \
                    datasource_map['Datasource ID'] == datasource_id:
                return datasource_map['Datasource Name']

        raise RuntimeError('Could not find Datasource Class "%s" and Datasource ID "%s" in datasource maps' %
                           (datasource_class, datasource_id))

    @staticmethod
    def _execute_regex_map(old_definition, regex_map, *, allow_missing_properties=False):
        capture_groups = dict()
        for prop, regex in regex_map['Old'].items():
            if prop not in StoredItem.SEARCHABLE_PROPS:
                raise RuntimeError('Datasource map contains an unsearchable property "%s". Searchable properties:\n%s',
                                   '\n'.join(StoredItem.SEARCHABLE_PROPS))

            if prop not in old_definition:
                if allow_missing_properties:
                    continue
                else:
                    return None

            regex = util.pythonize_regex_capture_group_names(regex)
            match = re.fullmatch(regex, old_definition[prop])
            if not match:
                return None

            capture_groups.update(match.groupdict())

        new_definition = dict()
        for prop, regex in regex_map['New'].items():
            new_definition[prop] = util.replace_tokens_in_regex(regex, capture_groups, escape=False)

        return new_definition

    def _lookup_item_via_datasource_map(self, datasource_maps):
        logging = list()
        items_api = ItemsApi(_login.client)

        # First, we process the "overrides". These are the cases where, even if the item with the ID exists in the
        # destination, we still want to map to something else. Useful for swapping datasources on the same server.
        item = self._lookup_in_datasource_map(
            [m for m in datasource_maps if _common.get(m, 'Override', default=False)], logging)

        if item is not None:
            return item

        # Second, we just try to look the item up by its ID. This case will occur when the user pulls a workbook,
        # makes a change, and pushes it back.
        try:
            item = items_api.get_item_and_all_properties(id=self.id)  # type: ItemOutputV1
        except ApiException:
            logging.append('ID %s not found directly' % self.id)

        if item is not None:
            return item

        # Finally, we try to use the non-override maps to find the item. This case will occur mostly when
        # transferring workbooks between servers.
        item = self._lookup_in_datasource_map(
            [m for m in datasource_maps if not _common.get(m, 'Override', default=False)], logging)

        if item is None:
            raise _common.DependencyNotFound(
                str(self), 'No match for item with ID %s:\n%s' % (self.id, '\n'.join(logging)))

        return item

    def _lookup_in_datasource_map(self, datasource_maps, logging):
        items_api = ItemsApi(_login.client)
        item = None
        for i in range(0, len(datasource_maps)):
            if item is not None:
                break

            datasource_map = datasource_maps[i]
            if 'RegEx-Based Maps' in datasource_map:
                new_definition = None
                for regex_map in datasource_map['RegEx-Based Maps']:
                    old_definition = dict(self.definition)
                    if 'Datasource Class' in old_definition and 'Datasource ID' in old_definition:
                        old_definition['Datasource Name'] = \
                            StoredOrCalculatedItem._find_datasource_name(old_definition['Datasource Class'],
                                                                         old_definition['Datasource ID'],
                                                                         datasource_maps)

                    new_definition = StoredOrCalculatedItem._execute_regex_map(
                        old_definition, regex_map, allow_missing_properties=self.type.endswith('Datasource'))

                    if new_definition is not None:
                        break

                if new_definition is None:
                    logging.append('RegEx-Based Map %d did not match %s for "Old" values' % (i, self))
                    continue

                if 'Datasource Name' in new_definition:
                    if 'Datasource ID' not in new_definition:
                        if 'Datasource Class' not in new_definition:
                            raise RuntimeError('"Datasource Class" required with "Datasource Name" in map:\n%s' %
                                               json.dumps(new_definition))

                        datasource_results = items_api.search_items(
                            filters=['Datasource Class==%s&&Name==%s' % (new_definition['Datasource Class'],
                                                                         new_definition['Datasource Name']),
                                     '@includeUnsearchable'],
                            types=['Datasource'],
                            limit=2)  # type: ItemSearchPreviewPaginatedListV1

                        if len(datasource_results.items) > 1:
                            raise RuntimeError(
                                new_definition['Datasource Name'],
                                'Multiple datasources found that match "%s"' % new_definition['Datasource Name'])
                        elif len(datasource_results.items) == 0:
                            raise RuntimeError(
                                new_definition['Datasource Name'],
                                'No datasource found that matches "%s"' % new_definition['Datasource Name'])

                        new_datasource = datasource_results.items[0]  # type: ItemSearchPreviewV1
                        new_definition['Datasource ID'] = items_api.get_property(
                            id=new_datasource.id, property_name='Datasource ID').value
                    del new_definition['Datasource Name']

                if new_definition['Type'] not in ['User', 'UserGroup']:
                    filters = ' && '.join(
                        '%s~=/^%s$/' % (prop, re.escape(val)) for prop, val in new_definition.items())
                    search_results = items_api.search_items(filters=[filters, '@includeUnsearchable'],
                                                            limit=2)  # type: ItemSearchPreviewPaginatedListV1
                    if len(search_results.items) == 0:
                        logging.append('RegEx-Based Map %d did not match %s filters:\n%s' % (i, self, filters))
                    elif len(search_results.items) > 1:
                        logging.append('RegEx-Based Map %d multiple matches %s filters:\n%s' % (i, self, filters))
                    else:
                        item = items_api.get_item_and_all_properties(
                            id=search_results.items[0].id)
                else:
                    if new_definition['Type'] == 'User':
                        try:
                            users_api = UsersApi(_login.client)
                            item = users_api.get_user_from_username(
                                auth_datasource_class=new_definition['Datasource Class'],
                                auth_datasource_id=new_definition['Datasource ID'],
                                username=new_definition['Username'])
                        except ApiException:
                            # Fall through, item not found
                            pass
                    else:
                        user_groups_api = UserGroupsApi(_login.client)
                        user_groups = user_groups_api.get_user_groups()  # type: ItemPreviewListV1
                        for user_group in user_groups.items:  # type: ItemPreviewV1
                            if user_group.name == new_definition['Name']:
                                item = user_group
                                break
        return item


class StoredItem(StoredOrCalculatedItem):
    SEARCHABLE_PROPS = ['Datasource Class', 'Datasource ID', 'Datasource Name', 'Data ID',
                        'Type', 'Name', 'Description', 'Username']

    def push(self, datasource_maps, *, pushed_workbook_id=None, item_map=None, label=None, override_max_interp=False):
        item = self._lookup_item_via_datasource_map(datasource_maps)

        item_map[self.id.upper()] = item.id.upper()

        if item.type not in ['User', 'UserGroup']:
            # We need to exclude Example Data, because it is set explicitly by the connector
            datasource_class_prop = Item._property_output_from_item_output(item, 'Datasource Class')
            datasource_id_prop = Item._property_output_from_item_output(item, 'Datasource ID')
            is_example_data = (datasource_class_prop and datasource_class_prop.value == 'Time Series CSV Files' and
                               datasource_id_prop and datasource_id_prop.value == 'Example Data')

            if override_max_interp and item.type == 'StoredSignal' and not is_example_data and \
                    'Maximum Interpolation' in self:
                src_max_interp = Item._property_input_from_scalar_str(self['Maximum Interpolation'])
                dst_max_interp_prop = Item._property_output_from_item_output(item, 'Maximum Interpolation')
                if dst_max_interp_prop:
                    dst_max_interp = Item._property_input_from_scalar_str(dst_max_interp_prop.value)
                    if src_max_interp.unit_of_measure != dst_max_interp.unit_of_measure or \
                            src_max_interp.value != dst_max_interp.value:
                        items_api = ItemsApi(_login.client)
                        items_api.set_property(id=item.id,
                                               property_name='Override Maximum Interpolation',
                                               body=src_max_interp)

        return item


class Datasource(StoredItem):
    @staticmethod
    def from_datasource_id(datasource_class, datasource_id):
        _filters = ['Datasource Class==' + datasource_class,
                    'Datasource ID==' + datasource_id]

        filters_arg = [' && '.join(_filters), '@includeUnsearchable']

        items_api = ItemsApi(_login.client)
        item_search_list = items_api.search_items(
            types=['Datasource'],
            filters=filters_arg,
            limit=1)  # type: ItemSearchPreviewPaginatedListV1

        if len(item_search_list.items) != 1:
            raise RuntimeError(
                'Datasource Class "%s" and Datasource ID "%s" not found' % (datasource_class, datasource_id))

        return Item.pull(item_search_list.items[0].id)


class TableDatasource(Datasource):
    pass


class CalculatedItem(StoredOrCalculatedItem):
    def _check_for_reference_item(self, datasource_maps, item_map):
        if _common.get(self, 'Datasource Class') == 'Tree File' or _common.get(self, 'Reference', False):
            item = self._lookup_item_via_datasource_map(datasource_maps)
            item_map[self.id.upper()] = item.id.upper()
            return item

        return None


class StoredSignal(StoredItem):
    pass


class CalculatedSignal(CalculatedItem):
    def _pull(self, item_id):
        signals_api = SignalsApi(_login.client)
        signal_output = signals_api.get_signal(id=item_id)  # type: SignalOutputV1
        self._pull_formula_based_item(signal_output)

    def push(self, datasource_maps, *, pushed_workbook_id=None, item_map=None, label=None, override_max_interp=False):
        item = self._check_for_reference_item(datasource_maps, item_map)
        if item:
            return item

        signals_api = SignalsApi(_login.client)
        items_api = ItemsApi(_login.client)

        data_id = Workbook._data_id_from_item_id(label, self.definition['ID'])

        signal_input = SignalInputV1()
        signal_input.name = self.definition['Name']
        if 'Description' in self.definition:
            signal_input.description = self.definition['Description']
        signal_input.formula = Item.formula_string_from_list(self.definition['Formula'])

        signal_input.formula_parameters = list()
        for parameter_name, parameter_id in self.definition['Formula Parameters'].items():
            if parameter_id not in item_map:
                raise DependencyNotFound(parameter_id)

            signal_input.formula_parameters.append('%s=%s' % (parameter_name, item_map[parameter_id.upper()]))

        if 'Number Format' in self.definition:
            signal_input.number_format = self.definition['Number Format']

        signal_input.scoped_to = pushed_workbook_id

        signal_output = signals_api.put_signal_by_data_id(datasource_class=_common.DEFAULT_DATASOURCE_CLASS,
                                                          datasource_id=_common.DEFAULT_DATASOURCE_ID,
                                                          data_id=data_id,
                                                          body=signal_input)  # type: SignalOutputV1

        if 'UIConfig' in self.definition:
            items_api.set_property(id=signal_output.id,
                                   property_name='UIConfig',
                                   body=PropertyInputV1(value=json.dumps(self.definition['UIConfig'])))

        item_map[self.id.upper()] = signal_output.id.upper()

        return signal_output


class StoredCondition(StoredItem):
    pass


class CalculatedCondition(CalculatedItem):
    def _pull(self, item_id):
        conditions_api = ConditionsApi(_login.client)
        condition_output = conditions_api.get_condition(id=item_id)  # type: ConditionOutputV1
        self._pull_formula_based_item(condition_output)

    def push(self, datasource_maps, *, pushed_workbook_id=None, item_map=None, label=None, override_max_interp=False):
        item = self._check_for_reference_item(datasource_maps, item_map)
        if item:
            return item

        conditions_api = ConditionsApi(_login.client)
        items_api = ItemsApi(_login.client)

        data_id = Workbook._data_id_from_item_id(label, self.definition['ID'])

        condition_input = ConditionInputV1()
        condition_input.name = self.definition['Name']
        if 'Description' in self.definition:
            condition_input.description = self.definition['Description']
        condition_input.formula = Item.formula_string_from_list(self.definition['Formula'])

        condition_input.parameters = list()
        for parameter_name, parameter_id in self.definition['Formula Parameters'].items():
            if parameter_id not in item_map:
                raise DependencyNotFound(parameter_id)

            condition_input.parameters.append('%s=%s' % (parameter_name, item_map[parameter_id.upper()]))

        if 'Number Format' in self.definition:
            condition_input.number_format = self.definition['Number Format']

        condition_input.additional_properties = list()
        if 'UIConfig' in self.definition:
            condition_input.additional_properties.append(
                ScalarPropertyV1(name='UIConfig', value=json.dumps(self.definition['UIConfig'])))

        condition_input.scoped_to = pushed_workbook_id

        condition_input.datasource_class = _common.DEFAULT_DATASOURCE_CLASS
        condition_input.datasource_id = _common.DEFAULT_DATASOURCE_ID
        condition_input.data_id = data_id

        item_batch_output = conditions_api.put_conditions(
            body=ConditionBatchInputV1(conditions=[condition_input]))  # type: ItemBatchOutputV1

        item_update_output = item_batch_output.item_updates[0]  # type: ItemUpdateOutputV1
        if item_update_output.error_message is not None:
            raise RuntimeError('Could not push condition "%s": %s' %
                               (self.definition['Name'], item_update_output.error_message))

        # Due to CRAB-18217, the additional_properties part of the put_conditions call doesn't work
        if len(condition_input.additional_properties) > 0:
            items_api.set_properties(id=item_update_output.item.id, body=condition_input.additional_properties)

        item_map[self.id.upper()] = item_update_output.item.id.upper()

        return item_update_output.item


class CalculatedScalar(CalculatedItem):
    def _pull(self, item_id):
        scalars_api = ScalarsApi(_login.client)
        calculated_item_output = scalars_api.get_scalar(id=item_id)  # type: CalculatedItemOutputV1
        self._pull_formula_based_item(calculated_item_output)

    def push(self, datasource_maps, *, pushed_workbook_id=None, item_map=None, label=None, override_max_interp=False):
        item = self._check_for_reference_item(datasource_maps, item_map)
        if item:
            return item

        scalars_api = ScalarsApi(_login.client)

        data_id = Workbook._data_id_from_item_id(label, self.definition['ID'])

        scalar_input = ScalarInputV1()
        scalar_input.name = self.definition['Name']
        if 'Description' in self.definition:
            scalar_input.description = self.definition['Description']
        scalar_input.formula = Item.formula_string_from_list(self.definition['Formula'])

        scalar_input.parameters = list()
        for parameter_name, parameter_id in self.definition['Formula Parameters'].items():
            if parameter_id not in item_map:
                raise DependencyNotFound(parameter_id)

            scalar_input.parameters.append('%s=%s' % (parameter_name, item_map[parameter_id.upper()]))

        if 'Number Format' in self.definition:
            scalar_input.number_format = self.definition['Number Format']

        scalar_input.additional_properties = list()
        if 'UIConfig' in self.definition:
            scalar_input.additional_properties.append(
                ScalarPropertyV1(name='UIConfig', value=json.dumps(self.definition['UIConfig'])))

        scalar_input.scoped_to = pushed_workbook_id

        scalar_input.data_id = data_id

        item_batch_output = scalars_api.put_scalars(
            body=PutScalarsInputV1(datasource_class=_common.DEFAULT_DATASOURCE_CLASS,
                                   datasource_id=_common.DEFAULT_DATASOURCE_ID,
                                   scalars=[scalar_input]))  # type: ItemBatchOutputV1

        item_update_output = item_batch_output.item_updates[0]  # type: ItemUpdateOutputV1
        if item_update_output.error_message is not None:
            raise RuntimeError('Could not push scalar "%s": %s' %
                               (self.definition['Name'], item_update_output.error_message))

        item_map[self.id.upper()] = item_update_output.item.id.upper()

        return item_update_output.item


class Chart(CalculatedItem):
    def _pull(self, item_id):
        formulas_api = FormulasApi(_login.client)
        calculated_item_output = formulas_api.get_function(id=item_id)  # type: CalculatedItemOutputV1

        self._pull_formula_based_item(calculated_item_output)

        if 'FormulaParameters' in self.definition:
            # Charts have these superfluous properties
            del self.definition['FormulaParameters']

    def push(self, datasource_maps, *, pushed_workbook_id=None, item_map=None, label=None,
             override_max_interp=False):

        formulas_api = FormulasApi(_login.client)
        items_api = ItemsApi(_login.client)

        data_id = Workbook._data_id_from_item_id(label, self.definition['ID'])
        item = Workbook.find_item(self.definition['ID'], label)

        function_input = FunctionInputV1()
        function_input.name = self.definition['Name']
        function_input.type = self.definition['Type']
        function_input.formula = Item.formula_string_from_list(self.definition['Formula'])
        function_input.parameters = list()
        for parameter_name, parameter_id in self.definition['Formula Parameters'].items():
            if _common.is_guid(parameter_id):
                if parameter_id not in item_map:
                    raise DependencyNotFound(parameter_id)

                function_input.parameters.append(FormulaParameterInputV1(name=parameter_name,
                                                                         id=item_map[parameter_id.upper()]))
            else:
                function_input.parameters.append(FormulaParameterInputV1(name=parameter_name,
                                                                         formula=parameter_id,
                                                                         unbound=True))

        if 'Description' in self.definition:
            function_input.description = self.definition['Description']

        function_input.scoped_to = pushed_workbook_id
        function_input.data_id = data_id

        if item is None:
            calculated_item_output = formulas_api.create_function(body=function_input)  # type: CalculatedItemOutputV1

            items_api.set_properties(
                id=calculated_item_output.id,
                body=[ScalarPropertyV1(name='Datasource Class', value=_common.DEFAULT_DATASOURCE_CLASS),
                      ScalarPropertyV1(name='Datasource ID', value=_common.DEFAULT_DATASOURCE_ID),
                      ScalarPropertyV1(name='Data ID', value=data_id)])
        else:
            calculated_item_output = formulas_api.update_function(id=item.id,
                                                                  body=function_input)  # type: CalculatedItemOutputV1

        if 'UIConfig' in self.definition:
            items_api.set_properties(
                id=calculated_item_output.id,
                body=[ScalarPropertyV1(name='UIConfig', value=json.dumps(self.definition['UIConfig']))])

        item_map[self.id.upper()] = calculated_item_output.id.upper()

        return calculated_item_output


class ThresholdMetric(CalculatedItem):
    def _pull(self, item_id):
        metrics_api = MetricsApi(_login.client)
        metric = metrics_api.get_metric(id=item_id)  # type: ThresholdMetricOutputV1

        formula_parameters = dict()
        if metric.aggregation_function is not None:
            formula_parameters['Aggregation Function'] = metric.aggregation_function
        if metric.bounding_condition is not None:
            formula_parameters['Bounding Condition'] = metric.bounding_condition.id
        if metric.bounding_condition_maximum_duration is not None:
            formula_parameters['Bounding Condition Maximum Duration'] = \
                Item._dict_from_scalar_value_output(metric.bounding_condition_maximum_duration)
        if metric.duration is not None:
            formula_parameters['Duration'] = Item._dict_from_scalar_value_output(metric.duration)
        if metric.measured_item is not None:
            formula_parameters['Measured Item'] = metric.measured_item.id
        if metric.measured_item_maximum_duration is not None:
            formula_parameters['Measured Item Maximum Duration'] = \
                Item._dict_from_scalar_value_output(metric.measured_item_maximum_duration)
        if hasattr(metric, 'number_format') and metric.number_format is not None:
            formula_parameters['Number Format'] = metric.number_format
        if metric.period is not None:
            formula_parameters['Period'] = Item._dict_from_scalar_value_output(metric.period)
        if metric.process_type is not None:
            formula_parameters['Process Type'] = metric.process_type

        def _add_thresholds(_thresholds_name, _threshold_output_list):
            formula_parameters[_thresholds_name] = list()
            for threshold in _threshold_output_list:  # type: ThresholdOutputV1
                threshold_dict = dict()
                if threshold.priority is not None:
                    priority = threshold.priority  # type: PriorityV1
                    threshold_dict['Priority'] = {
                        'Name': priority.name,
                        'Level': priority.level,
                        'Color': priority.color
                    }

                if not threshold.is_generated and threshold.item:
                    threshold_dict['Item ID'] = threshold.item.id

                if threshold.value is not None:
                    if isinstance(threshold.value, ScalarValueOutputV1):
                        threshold_dict['Value'] = Item._dict_from_scalar_value_output(threshold.value)
                    else:
                        threshold_dict['Value'] = threshold.value

                formula_parameters[_thresholds_name].append(threshold_dict)

        if metric.thresholds:
            _add_thresholds('Thresholds', metric.thresholds)

        # These properties come through in the GET /items/{id} call, and for clarity's sake we remove them
        for ugly_duplicate_property in ['AggregationFunction', 'BoundingConditionMaximumDuration',
                                        'MeasuredItemMaximumDuration']:
            if ugly_duplicate_property in self.definition:
                del self.definition[ugly_duplicate_property]

        self.definition['Formula'] = '<ThresholdMetric>'
        self.definition['Formula Parameters'] = formula_parameters

    def push(self, datasource_maps, *, pushed_workbook_id=None, item_map=None, label=None, override_max_interp=False):
        items_api = ItemsApi(_login.client)
        metrics_api = MetricsApi(_login.client)

        parameters = self['Formula Parameters']

        new_item = ThresholdMetricInputV1()
        new_item.name = self.name
        new_item.scoped_to = pushed_workbook_id

        def _add_scalar_value(_attr, _key):
            if _common.present(parameters, _key):
                setattr(new_item, _attr, Item._str_from_scalar_value_dict(parameters[_key]))

        def _add_mapped_item(_attr, _key):
            if _common.present(parameters, _key):
                if parameters[_key] not in item_map:
                    raise DependencyNotFound(parameters[_key])

                setattr(new_item, _attr, item_map[parameters[_key].upper()])

        def _add_thresholds(_list, _key):
            if not _common.present(parameters, _key):
                return

            for threshold_dict in parameters[_key]:
                threshold_value = _common.get(threshold_dict, 'Value')
                if threshold_value is not None:
                    if isinstance(threshold_value, dict):
                        _list.append('%s=%s' % (threshold_dict['Priority']['Level'],
                                                Item._str_from_scalar_value_dict(threshold_value)))
                    else:
                        _list.append('%s=%s' % (threshold_dict['Priority']['Level'], threshold_value))
                elif _common.present(threshold_dict, 'Item ID'):
                    if threshold_dict['Item ID'] not in item_map:
                        raise DependencyNotFound(threshold_dict['Item ID'])

                    _list.append('%s=%s' % (threshold_dict['Priority']['Level'],
                                            item_map[threshold_dict['Item ID'].upper()]))

        new_item.aggregation_function = _common.get(parameters, 'Aggregation Function')

        _add_mapped_item('bounding_condition', 'Bounding Condition')
        _add_scalar_value('bounding_condition_maximum_duration', 'Bounding Condition Maximum Duration')
        _add_scalar_value('duration', 'Duration')
        _add_mapped_item('measured_item', 'Measured Item')
        _add_scalar_value('measured_item_maximum_duration', 'Measured Item Maximum Duration')
        new_item.number_format = _common.get(parameters, 'Number Format')
        _add_scalar_value('period', 'Period')

        new_item.thresholds = list()
        _add_thresholds(new_item.thresholds, 'Thresholds')

        data_id = Workbook._data_id_from_item_id(label, self.definition['ID'])
        item = Workbook.find_item(self.definition['ID'], label)

        while True:
            try:
                if item is None:
                    threshold_metric_output = metrics_api.create_threshold_metric(
                        body=new_item)  # type: ThresholdMetricOutputV1

                    items_api.set_properties(
                        id=threshold_metric_output.id,
                        body=[ScalarPropertyV1(name='Datasource Class', value=_common.DEFAULT_DATASOURCE_CLASS),
                              ScalarPropertyV1(name='Datasource ID', value=_common.DEFAULT_DATASOURCE_ID),
                              ScalarPropertyV1(name='Data ID', value=data_id)])
                else:
                    threshold_metric_output = metrics_api.put_threshold_metric(
                        id=item.id,
                        body=new_item)  # type: ThresholdMetricOutputV1

                break

            except ApiException as e:
                # We have to handle a case where a condition on which a metric depends has been changed from bounded
                # to unbounded. In the UI, it automatically fills in the default of 40h when you edit such a metric,
                # so we do roughly the same thing here. This is tested by test_push.test_bad_metric().
                exception_text = _common.format_exception(e)
                if 'Maximum Capsule Duration for Measured Item must be provided' in exception_text:
                    new_item.measured_item_maximum_duration = '40h'
                elif 'Maximum Capsule Duration for Bounding Condition must be provided' in exception_text:
                    new_item.bounding_condition_maximum_duration = '40h'
                else:
                    raise

        if 'UIConfig' in self.definition:
            items_api.set_properties(
                id=threshold_metric_output.id,
                body=[ScalarPropertyV1(name='UIConfig', value=json.dumps(self.definition['UIConfig']))])

        item_map[self.id.upper()] = threshold_metric_output.id.upper()

        return threshold_metric_output


class Identity(StoredItem):
    def pull_datasource(self, identity):
        # noinspection PyBroadException
        try:
            if identity.type == 'User':
                auth_api = AuthApi(_login.client)
                auth_providers_output = auth_api.get_auth_providers()  # type: AuthProvidersOutputV1
                users_api = UsersApi(_login.client)
                user_output = users_api.get_user(id=identity.id)  # type: UserOutputV1

                for auth_provider in auth_providers_output.auth_providers:  # DatasourceOutputV1
                    if auth_provider.name == user_output.datasource_name:
                        self['Datasource Class'] = auth_provider.datasource_class
                        self['Datasource ID'] = auth_provider.datasource_id
                        self['Datasource Name'] = auth_provider.name
                        break
            else:
                # In .45, groups will come from different datasources. For now, hard-code it.
                # user_groups_api = UserGroupsApi(_login.client)
                # user_group_output = user_groups_api.get_user_group(id=identity.id)  # type: UserGroupOutputV1
                self['Datasource Class'] = 'Auth'
                self['Datasource ID'] = 'Seeq'
                self['Datasource Name'] = 'Seeq'
        except KeyboardInterrupt:
            raise
        except BaseException:
            # If we can't get extra data on the user, that's OK
            pass


class User(Identity):
    @staticmethod
    def pull(item_id, *, allowed_types=None, status=None):
        users_api = UsersApi(_login.client)
        user_output = users_api.get_user(id=item_id)  # type: UserOutputV1

        item = User({
            'ID': user_output.id,
            'Type': user_output.type,
            'Name': user_output.name,
            'Username': user_output.username,
            'First Name': user_output.first_name,
            'Last Name': user_output.last_name,
            'Email': user_output.email,
            'Is Admin': user_output.is_admin
        })

        item.pull_datasource(user_output)
        return item


class UserGroup(Identity):
    @staticmethod
    def pull(item_id, *, allowed_types=None, status=None):
        usergroups_api = UserGroupsApi(_login.client)
        usergroup_output = usergroups_api.get_user_group(user_group_id=item_id)  # type: UserGroupOutputV1

        item = UserGroup({
            'ID': usergroup_output.id,
            'Type': usergroup_output.type,
            'Name': usergroup_output.name
        })

        item.pull_datasource(usergroup_output)
        return item


class Options:
    def __init__(self):
        self.pretty_print_html = False


options = Options()

# coding: utf-8

"""
    Seeq REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 0.44.04
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ItemAncillaryOutputV1(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'data_id': 'str',
        'datasource_class': 'str',
        'datasource_id': 'str',
        'description': 'str',
        'href': 'str',
        'id': 'str',
        'is_archived': 'bool',
        'items': 'list[AncillaryItemOutputV1]',
        'name': 'str',
        'scoped_to': 'str',
        'status_message': 'str',
        'type': 'str'
    }

    attribute_map = {
        'data_id': 'dataId',
        'datasource_class': 'datasourceClass',
        'datasource_id': 'datasourceId',
        'description': 'description',
        'href': 'href',
        'id': 'id',
        'is_archived': 'isArchived',
        'items': 'items',
        'name': 'name',
        'scoped_to': 'scopedTo',
        'status_message': 'statusMessage',
        'type': 'type'
    }

    def __init__(self, data_id=None, datasource_class=None, datasource_id=None, description=None, href=None, id=None, is_archived=False, items=None, name=None, scoped_to=None, status_message=None, type=None):
        """
        ItemAncillaryOutputV1 - a model defined in Swagger
        """

        self._data_id = None
        self._datasource_class = None
        self._datasource_id = None
        self._description = None
        self._href = None
        self._id = None
        self._is_archived = None
        self._items = None
        self._name = None
        self._scoped_to = None
        self._status_message = None
        self._type = None

        if data_id is not None:
          self.data_id = data_id
        if datasource_class is not None:
          self.datasource_class = datasource_class
        if datasource_id is not None:
          self.datasource_id = datasource_id
        if description is not None:
          self.description = description
        if href is not None:
          self.href = href
        if id is not None:
          self.id = id
        if is_archived is not None:
          self.is_archived = is_archived
        if items is not None:
          self.items = items
        if name is not None:
          self.name = name
        if scoped_to is not None:
          self.scoped_to = scoped_to
        if status_message is not None:
          self.status_message = status_message
        if type is not None:
          self.type = type

    @property
    def data_id(self):
        """
        Gets the data_id of this ItemAncillaryOutputV1.
        The data ID of this asset. Note: This is not the Seeq ID, but the unique identifier that the remote datasource uses.

        :return: The data_id of this ItemAncillaryOutputV1.
        :rtype: str
        """
        return self._data_id

    @data_id.setter
    def data_id(self, data_id):
        """
        Sets the data_id of this ItemAncillaryOutputV1.
        The data ID of this asset. Note: This is not the Seeq ID, but the unique identifier that the remote datasource uses.

        :param data_id: The data_id of this ItemAncillaryOutputV1.
        :type: str
        """

        self._data_id = data_id

    @property
    def datasource_class(self):
        """
        Gets the datasource_class of this ItemAncillaryOutputV1.
        The datasource class, which is the type of system holding the item, such as OSIsoft PI

        :return: The datasource_class of this ItemAncillaryOutputV1.
        :rtype: str
        """
        return self._datasource_class

    @datasource_class.setter
    def datasource_class(self, datasource_class):
        """
        Sets the datasource_class of this ItemAncillaryOutputV1.
        The datasource class, which is the type of system holding the item, such as OSIsoft PI

        :param datasource_class: The datasource_class of this ItemAncillaryOutputV1.
        :type: str
        """

        self._datasource_class = datasource_class

    @property
    def datasource_id(self):
        """
        Gets the datasource_id of this ItemAncillaryOutputV1.
        The datasource identifier, which is how the datasource holding this item identifies itself

        :return: The datasource_id of this ItemAncillaryOutputV1.
        :rtype: str
        """
        return self._datasource_id

    @datasource_id.setter
    def datasource_id(self, datasource_id):
        """
        Sets the datasource_id of this ItemAncillaryOutputV1.
        The datasource identifier, which is how the datasource holding this item identifies itself

        :param datasource_id: The datasource_id of this ItemAncillaryOutputV1.
        :type: str
        """

        self._datasource_id = datasource_id

    @property
    def description(self):
        """
        Gets the description of this ItemAncillaryOutputV1.
        Clarifying information or other plain language description of this item

        :return: The description of this ItemAncillaryOutputV1.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ItemAncillaryOutputV1.
        Clarifying information or other plain language description of this item

        :param description: The description of this ItemAncillaryOutputV1.
        :type: str
        """

        self._description = description

    @property
    def href(self):
        """
        Gets the href of this ItemAncillaryOutputV1.
        The href that can be used to interact with the item

        :return: The href of this ItemAncillaryOutputV1.
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """
        Sets the href of this ItemAncillaryOutputV1.
        The href that can be used to interact with the item

        :param href: The href of this ItemAncillaryOutputV1.
        :type: str
        """
        if href is None:
            raise ValueError("Invalid value for `href`, must not be `None`")

        self._href = href

    @property
    def id(self):
        """
        Gets the id of this ItemAncillaryOutputV1.
        The ID that can be used to interact with the item

        :return: The id of this ItemAncillaryOutputV1.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ItemAncillaryOutputV1.
        The ID that can be used to interact with the item

        :param id: The id of this ItemAncillaryOutputV1.
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def is_archived(self):
        """
        Gets the is_archived of this ItemAncillaryOutputV1.
        Whether item is isArchived

        :return: The is_archived of this ItemAncillaryOutputV1.
        :rtype: bool
        """
        return self._is_archived

    @is_archived.setter
    def is_archived(self, is_archived):
        """
        Sets the is_archived of this ItemAncillaryOutputV1.
        Whether item is isArchived

        :param is_archived: The is_archived of this ItemAncillaryOutputV1.
        :type: bool
        """

        self._is_archived = is_archived

    @property
    def items(self):
        """
        Gets the items of this ItemAncillaryOutputV1.
        The list of the ancillaries for the item

        :return: The items of this ItemAncillaryOutputV1.
        :rtype: list[AncillaryItemOutputV1]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this ItemAncillaryOutputV1.
        The list of the ancillaries for the item

        :param items: The items of this ItemAncillaryOutputV1.
        :type: list[AncillaryItemOutputV1]
        """

        self._items = items

    @property
    def name(self):
        """
        Gets the name of this ItemAncillaryOutputV1.
        The human readable name

        :return: The name of this ItemAncillaryOutputV1.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ItemAncillaryOutputV1.
        The human readable name

        :param name: The name of this ItemAncillaryOutputV1.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def scoped_to(self):
        """
        Gets the scoped_to of this ItemAncillaryOutputV1.
        The ID of the workbook to which this item is scoped or null if it is in the global scope.

        :return: The scoped_to of this ItemAncillaryOutputV1.
        :rtype: str
        """
        return self._scoped_to

    @scoped_to.setter
    def scoped_to(self, scoped_to):
        """
        Sets the scoped_to of this ItemAncillaryOutputV1.
        The ID of the workbook to which this item is scoped or null if it is in the global scope.

        :param scoped_to: The scoped_to of this ItemAncillaryOutputV1.
        :type: str
        """

        self._scoped_to = scoped_to

    @property
    def status_message(self):
        """
        Gets the status_message of this ItemAncillaryOutputV1.
        A plain language status message with information about any issues that may have been encountered during an operation

        :return: The status_message of this ItemAncillaryOutputV1.
        :rtype: str
        """
        return self._status_message

    @status_message.setter
    def status_message(self, status_message):
        """
        Sets the status_message of this ItemAncillaryOutputV1.
        A plain language status message with information about any issues that may have been encountered during an operation

        :param status_message: The status_message of this ItemAncillaryOutputV1.
        :type: str
        """

        self._status_message = status_message

    @property
    def type(self):
        """
        Gets the type of this ItemAncillaryOutputV1.
        The type of the item

        :return: The type of this ItemAncillaryOutputV1.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ItemAncillaryOutputV1.
        The type of the item

        :param type: The type of this ItemAncillaryOutputV1.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, ItemAncillaryOutputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

import os
from enum import Enum
import configparser

from seeq.base import system

file_config = None


class Setting(Enum):
    CONFIG_FOLDER = {'env': 'SEEQ_SPY_CONFIG_FOLDER', 'ini': None}
    CONFIG_FILENAME = {'env': 'SEEQ_SPY_CONFIG_FILENAME', 'ini': None}
    SEEQ_URL = {'env': 'SEEQ_SERVER_URL', 'ini': 'seeq_server_url'}
    SEEQ_CERT_PATH = {'env': 'SEEQ_CERT_PATH', 'ini': 'seeq_cert_path'}
    SEEQ_KEY_PATH = {'env': 'SEEQ_KEY_PATH', 'ini': 'seeq_key_path'}
    AGENT_KEY_PATH = {'env': 'AGENT_KEY_PATH', 'ini': 'agent_key_path'}

    def get_env_name(self):
        return self.value['env']

    def get_ini_name(self):
        return self.value['ini']

    def get(self):
        setting = os.environ.get(self.get_env_name())
        if not setting and self.get_ini_name():
            config = get_file_config()
            setting = config.get('spy', self.get_ini_name(), fallback=None)
        return setting

    def set(self, value):
        os.environ[self.get_env_name()] = value

    def unset(self):
        del os.environ[self.get_env_name()]


def get_config_folder():
    """
    This is the config folder for the Spy library, which is where any additional configuration files for Spy must be
    stored. The default location is the same as the Seeq global folder.
    :return: Location of the config folder
    """
    config_folder = Setting.CONFIG_FOLDER.get()
    if not config_folder:
        if system.is_windows():
            config_folder = os.path.join(os.environ["ProgramData"], 'Seeq')
        else:
            config_folder = os.path.join(system.get_home_dir(), '.seeq')

    system.create_folder_if_necessary_with_correct_permissions(config_folder)

    return config_folder


def set_config_folder(path):
    Setting.CONFIG_FOLDER.set(path)


def get_config_filename():
    filename = Setting.CONFIG_FILENAME.get()
    return filename if filename else "spy.ini"


def get_config_path():
    return os.path.join(get_config_folder(), get_config_filename())


def get_seeq_url():
    url = Setting.SEEQ_URL.get()
    return url if url else 'http://localhost:34216'


def set_seeq_url(url):
    Setting.SEEQ_URL.set(url)


def unset_seeq_url():
    Setting.SEEQ_URL.unset()


def get_api_url():
    return '{0}/api'.format(get_seeq_url())


def get_seeq_cert_path():
    path = Setting.SEEQ_CERT_PATH.get()
    return path if path else os.path.join(get_config_folder(), 'seeq-cert.pem')


def get_seeq_key_path():
    path = Setting.SEEQ_KEY_PATH.get()
    return path if path else os.path.join(get_config_folder(), 'seeq-key.pem')


def get_file_config():
    global file_config
    if not file_config:
        file_config = configparser.ConfigParser()
        file_config.read(get_config_path())
    return file_config

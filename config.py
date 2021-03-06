import configparser
import os
import re


class Config:
    def __init__(self, path):
        if not os.path.exists(path):
            raise FileExistsError
        self.configuration = configparser.RawConfigParser()
        self.configuration.read(path, encoding='1251')

    def get_setting(self, section, setting):
        return self.configuration.get(section, setting)

    def get_section(self, section):
        return self.configuration.options(section)

    def set_setting(self, section, setting, value):
        self.configuration.set(section=section, option=setting, value=value)

    def has_section(self, name):
        return self.configuration.has_section(name)

    def has_option(self, section, option):
        return self.configuration.has_option(section, option)

    def get_dict_from_dbf(self, dbf_file_name: str):
        field_dict = {}
        if dbf_file_name.startswith('SC'):
            section_list = re.findall('\d+', dbf_file_name.split('.')[0])
            section = ''.join(section_list)
        elif dbf_file_name == '1SJOURN.DBF':
            section = 'Journal'
        else:
            section = dbf_file_name.split('.')[0]
        keys = self.configuration.options(section=section)
        for k in keys:
            field_dict[k] = self.configuration.get(section, k).split()[0]
        return field_dict

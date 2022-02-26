import configparser
import os


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

    def has_section(self, name):
        return self.configuration.has_section(name)

    def get_dict_from_dbf(self, section):
        field_dict = {}
        keys = self.configuration.options(section=section)
        for k in keys:
            field_dict[k] = self.configuration.get(section, k).split()[0]
        return field_dict

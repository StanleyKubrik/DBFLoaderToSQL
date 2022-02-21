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

    def sqlconfig(self):
        creds = {}
        sqlcrededtional = self.configuration.options('SQL')
        for name in sqlcrededtional:
            creds[name] = self.get_setting('SQL', name)
        return creds

    def has_section(self, name):
        return self.configuration.has_section(name)
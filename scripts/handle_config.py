from configparser import ConfigParser

from configs.constants import CONFIG_FILE_PATH


class HandleConfig(ConfigParser):

    def __init__(self, file_name):
        super().__init__()
        self.file_name = file_name
        self.read(self.file_name, encoding='utf-8')

    def get_value(self, section, option):
        return self.get(section, option)

    def get_int(self, section, option):
        return self.getint(section, option)

    def get_float(self, section, option):
        return self.getfloat(section, option)

    def get_bool(self, section, option):
        return self.getboolean(section, option)


if __name__ == '__main__':
    config = HandleConfig(CONFIG_FILE_PATH)
    actual_col = config.get_int('excel', 'actual_col')
    print(actual_col)


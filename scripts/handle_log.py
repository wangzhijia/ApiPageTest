import logging
from logging.handlers import RotatingFileHandler
import os

from concurrent_log_handler import ConcurrentRotatingFileHandler

from scripts.handle_config import HandleConfig
from configs.constants import CONFIG_FILE_PATH, LOG_DIR


class HandleLog:

    def __init__(self):
        config = HandleConfig(CONFIG_FILE_PATH)
        self.case_log = logging.getLogger(config.get_value('log', 'logger_name'))
        self.case_log.setLevel(config.get_value('log', 'logger_level'))
        console_handle = logging.StreamHandler()
        file_handle = ConcurrentRotatingFileHandler(
            filename=os.path.join(LOG_DIR, config.get_value('log', 'log_filename')),
            maxBytes=config.get_int('log', 'maxBytes'),
            backupCount=config.get_int('log', 'backupCount'),
            encoding='utf-8')
        console_handle.setLevel(config.get_value('log', 'console_level'))
        file_handle.setLevel(config.get_value('log', 'file_level'))
        simple_formatter = logging.Formatter(config.get_value('log', 'simple_formatter'))
        verbose_formatter = logging.Formatter(config.get_value('log', 'verbose_formatter'))
        console_handle.setFormatter(simple_formatter)
        file_handle.setFormatter(verbose_formatter)
        self.case_log.addHandler(console_handle)
        self.case_log.addHandler(file_handle)

    def get_log(self):
        return self.case_log


if __name__ == '__main__':
    case_log = HandleLog().get_log()
    case_log.error('这是error日志')




import os.path
import unittest
import time

import HTMLTestRunner

from configs.constants import CASES_DIR, REPORTS_DIR, CONFIG_FILE_PATH
from scripts.handle_config import HandleConfig


config = HandleConfig(CONFIG_FILE_PATH)
one_suite = unittest.defaultTestLoader.discover(CASES_DIR)

report_html_name = os.path.join(REPORTS_DIR, config.get_value('report', 'report_html_name'))
report_html_name_full = report_html_name + "_" + time.strftime("%Y%m%d%H%M%S", time.localtime(time.time())) + ".html"
with open(report_html_name_full, mode='wb') as save_to_file:
    one_runner = HTMLTestRunner.HTMLTestRunner(stream=save_to_file,
                                               title=config.get_value("report", "title"),
                                               verbosity=config.get_int("report", "verbosity"),
                                               description=config.get_value("report", "description"))
    one_runner.run(one_suite)

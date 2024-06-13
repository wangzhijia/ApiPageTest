import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATAS_DIR = os.path.join(BASE_DIR, 'datas')
CONFIGS_DIR = os.path.join(BASE_DIR, 'configs')
LOG_DIR = os.path.join(BASE_DIR, 'log')
CASES_DIR = os.path.join(BASE_DIR, 'api_cases')
REPORTS_DIR = os.path.join(BASE_DIR, 'reports')
IMG_DIR = os.path.join(BASE_DIR, 'screenshot')

CASES_FILE_PATH = os.path.join(DATAS_DIR, 'api_cases.xlsx')
CONFIG_FILE_PATH = os.path.join(CONFIGS_DIR, 'testcase.conf')

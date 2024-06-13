import unittest

from lib.ddt import ddt, data

from scripts.handle_excel import HandleExcel
from scripts.handle_request import HandleRequest
from scripts.handle_log import HandleLog
from configs.constants import CASES_FILE_PATH


@ddt
class TestTouTiaoIndex(unittest.TestCase):

    handle_excel = HandleExcel(CASES_FILE_PATH, sheet_name='toutiao_index')
    cases_list = handle_excel.get_cases()
    case_log = HandleLog().get_log()

    @classmethod
    def setUpClass(cls):
        cls.handle_request = HandleRequest()
        cls.case_log.info("\n{:=^40s}".format("开始执行注册功能用例"))

    @classmethod
    def tearDownClass(cls):
        cls.handle_request.request_session_close()
        cls.case_log.info("\n{:=^40s}".format("注册功能用例执行结束"))

    @data(*cases_list)
    def test_toutiao_index(self, data_namedtuple):

        response = self.handle_request(
            method=data_namedtuple.method,
            url=data_namedtuple.url,
            data=data_namedtuple.parameter,
            headers=data_namedtuple.header)

        try:
            self.assertIn(data_namedtuple.expect, response.text, msg="测试【{}】失败".
                             format(data_namedtuple.title))
        except AssertionError as e:
            self.case_log.error("具体异常为：{}".format(e))
            self.handle_excel.write_cases(row=data_namedtuple.id + 1,
                                  actual=response.text,
                                  result=False)
            raise e
        else:
            self.handle_excel.write_cases(row=data_namedtuple.id + 1,
                                  actual=response.text,
                                  result=True)


if __name__ == '__main__':
    unittest.main()

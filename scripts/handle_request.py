import json

import requests

from scripts.handle_log import HandleLog


class HandleRequest:

    def __init__(self):
        self.request_session = requests.Session()
        self.handle_log = HandleLog()

    def __call__(self, method, url, data=None, is_json=False, headers=None, **kwargs):

        method = method.lower()

        if isinstance(data, str):
            try:
                data = json.loads(data)
            except Exception as e:
                self.handle_log.get_log().error("将json转换为Python类型时，出现异常：{}".format(e))
                data = eval(data)

        if isinstance(headers, str):
            try:
                headers = json.loads(headers)
            except Exception as e:
                self.handle_log.get_log().error("将json转换为Python类型时，出现异常：{}".format(e))
                headers = eval(headers)

        if method == 'get':
            res = self.request_session.get(url=url, params=data, headers=headers, **kwargs)
        elif method == 'post':
            if is_json:
                res = self.request_session.post(url=url, json=data, headers=headers, **kwargs)
            else:
                res = self.request_session.post(url=url, data=data, headers=headers, **kwargs)
        else:
            res = None
        return res

    def request_session_close(self):
        self.request_session.close()


if __name__ == '__main__':
    url = 'http://v.juhe.cn/toutiao/index'
    data = '{"key": "32da4a294dc05c11f2dd8b6407c27013", "type": "top", "pages": "1", "page_size": "10", "is_filter": "1"}'
    headers = '{"Content-Type": "application/x-www-form-urlencoded"}'
    method = 'post'
    handle_request = HandleRequest()
    res = handle_request(method=method, url=url, data=data, headers=headers, is_json=False)
    print(res.json())

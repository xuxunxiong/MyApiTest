import requests
from base import apiserverUnittest


class test_apiserver(apiserverUnittest):

    def setUp(self):
        # 首先找到test的父类（比如是类A），然后把类test的对象self转换为类A的对象，然后“被转换”的类A对象调用自己的__init__函数
        super(test_apiserver, self).setUp()
        self.host = '127.0.0.1:5000'
        # 话对象让你能够跨请求保持某些参数。它也会在同一个
        # Session
        # 实例发出的所有请求之间保持
        # cookie
        self.api_client = requests.Session()

    def tearDown(self):
        super(test_apiserver, self).tearDown()

    def test_create_user_not_existed(self):

        url = "%s/api/users/%d" % (self.host, 1000)
        data = {
            "name": "user1",
            "password": "123456"
        }
        resp = self.api_client.post(url, json=data)

        self.assertEqual(201, resp.status_code)
        self.assertEqual(True, resp.json()["success"])

if __name__ == '__main__':
    test_apiserver.test_create_user_not_existed()
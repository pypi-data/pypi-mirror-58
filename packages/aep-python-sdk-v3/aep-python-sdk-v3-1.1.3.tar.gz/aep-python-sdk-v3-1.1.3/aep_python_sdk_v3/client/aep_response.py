try:
    import json
except ImportError:
    import simplejson as json

"""
AEP Response module.

Created on 2018-09-13

@author: Enzo Liang
"""


class AepResponse:
    def __init__(self):
        self.msg = ''
        self.code = ''
        self.data = ''
        # self.sign = ''
        self.status = 200


    def success(self, data=None):
        """
        响应成功设置
        :param data:
        :return:
        """
        self.code = 1
        self.msg = "ok"
        self.data = data
        return self

    def failure(self, message=None, data=None, httpStatus=400):
        """
        响应失败设置
        :param message:
        :param data:
        :param httpStatus:
        :return:
        """
        self.code = 0
        self.msg = message
        self.data = data
        self.status = httpStatus
        return self

    def getCode(self):
        return self.code

    def setCode(self, code):
        self.code = code
        return self

    def getMsg(self):
        return self.msg

    def setMsg(self, msg):
        self.msg = msg
        return self

    def getData(self):
        return self.data

    def setData(self, data):
        self.data = data
        return self

    def getStatus(self):
        return self.status

    def setStatus(self, status):
        self.status = status
        return self

    def getSign(self):
        return self.sign

    def setSign(self, sign):
        self.sign = sign
        return self

    def toString(self):
        """
        将返回结果转换为字符串
        :return:
        """
        response_dict = {"code": self.code, "msg": self.msg, "data": self.data, "status": self.status}
        return json.dumps(response_dict, ensure_ascii=False)
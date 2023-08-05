import base64
import hashlib
import hmac
import uuid
from urllib.parse import quote, unquote

import time

from aep_python_sdk_v3.https import method_type as mt
from aep_python_sdk_v3.utils.aep_utils import AepUtils
from aep_python_sdk_v3.https import format_type

"""
AEP Request module.

Created on 2018-09-10

@author: Enzo Liang
"""


class AepRequest:

    def __init__(self, method=mt.POST):
        self.params = {}
        self.method = method
        self.headers = {}
        self.apiUrl = ''
        self.bodyFormat = format_type.APPLICATION_FORM
        self.httpContentType = format_type.FORM

    def addParam(self, key, value):
        """
        添加请求参数
        :param key:
        :param value:
        :return:
        """
        self.params[key] = value

    def getParams(self):
        return self.params

    def setApiUrl(self, apiUrl):
        """
        设置待访问的api的URL地址
        :param apiUrl:
        :return:
        """
        self.apiUrl = apiUrl

    def getApiUrl(self):
        return self.apiUrl

    def getHttpContentType(self):
        return self.httpContentType

    def setHttpContentType(self, httpContentType):
        self.httpContentType = httpContentType

    def getHeader(self):
        return self.headers

    def setHeader(self, key, value):
        self.headers[key] = value

    def setMethod(self, method):
        self.method = method

    def getMethod(self):
        return self.method

    def getBodyFormat(self):
        return self.bodyFormat

    def setBodyFormat(self, bodyFormat):
        self.bodyFormat = bodyFormat

    def getSignature(self, key):
        """
        将Header公共参数进行加密
        :param key:
        :return: 返回签名
        """
        sortedParams = sorted(self.headers.items(), key=lambda d: d[0])
        content = ''
        for k, v in sortedParams:
            content += k+"="+v+"&"
        signature = hmac.new(key.encode('utf-8'), msg=content[:-1].encode('utf-8'), digestmod=hashlib.sha256).hexdigest()
        return str(signature)

    def urlEncode(self, url):
        """
        编码带url的参数
        :param url:
        :return:
        """
        return quote(url, 'utf-8')

    def urlDecode(self, url):
        """
        解码带url的参数
        :param url:
        :return:
        """
        return unquote(url, 'utf-8')

    def imagEncodeBase64(self, image):
        """
        将图片参数进行bs64编码
        :param image:
        :return:
        """
        return base64.b64encode(image)

    def imagDecodeBase64(self, image):
        """
        将图片进行bs64解码
        :param image:
        :return:
        """
        return base64.b64decode(image)


if __name__ == '__main__':
    m = AepRequest()
    apiKey = "436121194580803585"
    m.setHeader(AepUtils.AEP_NONCE, str(uuid.uuid1()))
    m.setHeader(AepUtils.AEP_APIKEY, apiKey)
    m.setHeader(AepUtils.AEP_TIMESTAMP, str(round(time.time() * 1000)))
    m.setHeader(AepUtils.AEP_SIGNATURE, m.getSignature(apiKey))
    print(m.getHeader())
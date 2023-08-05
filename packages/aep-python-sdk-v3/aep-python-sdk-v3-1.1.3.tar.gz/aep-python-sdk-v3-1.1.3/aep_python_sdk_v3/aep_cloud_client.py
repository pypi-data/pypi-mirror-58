# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

# coding=utf-8

import requests
import time
import uuid

from requests import Response

try:
    import json
except ImportError:
    import simplejson as json
from aep_python_sdk_v3.error import error_msg, error_code
from aep_python_sdk_v3.https import method_type as mt
from aep_python_sdk_v3.error.client_exception import ClientException
from aep_python_sdk_v3.error.aep_api_exception import AepApiException
from aep_python_sdk_v3.aep_request import AepRequest
from aep_python_sdk_v3.utils.aep_utils import AepUtils
from aep_python_sdk_v3.client.aep_response import AepResponse
import traceback
from aep_python_sdk_v3.https import format_type
"""
Aep client module.

Created on 2018-09-07

@author: Enzo Liang
"""
DEFAULT_SDK_CONNECTION_TIMEOUT_IN_SECONDS = 5

class AepCloudClinet:
    def __init__(self,
                 serverUrl='',
                 apiKey=None,
                 appKey=None,
                 appSecret=None,
                 format="json",
                 aepPublicKey=None,
                 isLocal=False,
                 requesteTimeout=DEFAULT_SDK_CONNECTION_TIMEOUT_IN_SECONDS,
                 max_retry_num=3):
        """
        :param serverUrl: 服务器地址(默认为空)
        :param apiKey: API Key
        :param appKey: 应用Key
        :param appSecret: 应用Secret
        :param format: 结果格式，模式JSON
        :param aepPublicKey: 开发者秘钥（保留没使用）
        :param isLocal: 是否本地服务
        :param requesteTimeout: 请求超时设置（秒）
        :param max_retry_num: 最大尝试次数
        """
        self.charset = "UTF-8"
        self.signType = "MD5"
        self.encryptType = "AES"
        self.serverUrl = serverUrl
        self.format = format
        self.apiKey = apiKey
        self.appKey = appKey
        self.appSecret = appSecret
        self.format = format
        self.aepPublicKey = aepPublicKey
        self.requesteTimeout = requesteTimeout
        self.isLocal = isLocal
        self.max_retry_num = max_retry_num


    def getServerUrl(self):
        return self.server_url

    def setServerUrl(self, server_url):
        self.server_url = server_url

    def getApiKey(self):
        return self.apiKey

    def setApiKey(self, apiKey):
        self.apiKey = apiKey

    def getAppKey(self):
        return self.appKey

    def setAppKey(self, appKey):
        self.appKey = appKey

    def getAppSecret(self):
        return self.appSecret

    def setAppSecret(self, appSecret):
        self.appSecret = appSecret

    def isLocal(self):
        return self.isLocal

    def setLocal(self, isLocal):
        self.isLocal = isLocal

    def getRequestTimeout(self):
        return self.request_timeout

    def setRequestTimeout(self, requesteTimeout):
        self.requesteTimeout = requesteTimeout

    def get_max_retry_num(self):
        """

        :return: Number
        """
        return self.max_retry_num

    def set_max_retry_num(self, num):
        """
        set auto retry number
        :param num: Numbers
        :return: None
        """
        self.max_retry_num = num

    def aepParamCheck(self, request):
        """
        关键参数校验
        :param request:
        :return:
        """
        if self.isLocal is False:
            # 赋能网
            if self.apiKey:
                # raise AepApiException(msg="apiKey参数不能为空")
                request.setHeader(AepUtils.AEP_NONCE, str(uuid.uuid1()))
                request.setHeader(AepUtils.AEP_APIKEY, self.apiKey)
                request.setHeader(AepUtils.AEP_TIMESTAMP, str(round(time.time() * 1000)))
                request.setHeader(AepUtils.AEP_SIGNATURE, request.getSignature(self.apiKey))
            else:
                # 赋能平台
                if self.appKey is None:
                    raise AepApiException(msg="appKey参数不能为空")
                if self.appSecret is None:
                    raise AepApiException(msg="appSecret密钥不能为空")
                request.setHeader(AepUtils.AEP_NONCE, str(uuid.uuid1()))
                request.setHeader(AepUtils.AEP_APPKEY, self.appKey)
                request.setHeader(AepUtils.AEP_TIMESTAMP, str(round(time.time() * 1000)))
                request.setHeader(AepUtils.AEP_SIGNATURE, request.getSignature(self.appSecret))

    def implementation_of_do_action(self, request):
        """
        利用requests模块实现访问请求
        :param request:
        :return:
        """
        if not isinstance(request, AepRequest):
            raise ClientException(
                error_code.SDK_INVALID_REQUEST,
                error_msg.get_msg('SDK_INVALID_REQUEST'))
        else:
            self.aepParamCheck(request)
            params = request.getParams()
            apiUrl = request.getApiUrl()
            method = request.getMethod()
            headers = request.getHeader()
            if self.serverUrl:
                url = self.serverUrl + '/' + apiUrl
            else:
                url = apiUrl
            try:
                if method.upper() == mt.GET:
                    if request.bodyFormat == 'application/json':
                        response = requests.get(url, data=json.dumps(params), headers=headers, timeout=self.requesteTimeout)
                        return response
                    elif request.bodyFormat == 'application/x-www-form-urlencoded':
                        response = requests.get(url, data=params, headers=headers, timeout=self.requesteTimeout)
                        return response
                    else:
                        raise AepApiException(msg="only support 'application/json' or 'application/x-www-form-urlencoded'")
                elif method.upper() == mt.POST:
                    if request.bodyFormat == 'application/json':
                        response = requests.post(url, data=json.dumps(params), headers=headers, timeout=self.requesteTimeout)
                        return response
                    elif request.bodyFormat == 'application/x-www-form-urlencoded':
                        response = requests.post(url, data=params, headers=headers, timeout=self.requesteTimeout)
                        return response
                    else:
                        raise AepApiException(msg="only support 'application/json' or 'application/x-www-form-urlencoded'")
                else:
                    raise AepApiException(msg= "The param 'method' is not correct")
            except requests.exceptions.Timeout:
                raise AepApiException(msg="Api request timeout")


    def execute(self, aep_request):
        """
        接受请求参数并进行请求操作
        :param aep_request:
        :return:
        """
        i = 0
        aep = AepResponse()
        while i < self.max_retry_num:
            try:
                response = self.implementation_of_do_action(aep_request)
                if isinstance(response, Response):
                    data = response.json()
                    return aep.success(data=data)
                else:
                    msg = "The response is not a valid AepResponse."
                i += 1
            except Exception as e:
                # traceback.print_exc()
                msg = str(e)
                i += 1
        return aep.failure(message=msg)





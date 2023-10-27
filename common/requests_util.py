# python3.8 (python版本)
# -*- coding: utf-8 -*-
# @Author  : ZYC
# @Software: PyCharm
# @Time    : 2023/10/17 14:59
# @File    : requests_util.py
import json
import requests
from common.rw_data import getdata
from common.log_util import logger


class RequestUtil:

    def __init__(self):
        self.session = requests.Session()
        self.base_url = getdata.read_ini('conf.ini')['host']['base_url']

    def request(self, method, url, **kwargs):
        self.log_request(method, url, **kwargs)
        try:
            return self.session.request(method=method, url=self.base_url+url, **kwargs)
        except:
            logger.error('接口请求失败')

    def log_request(self, method, url, **kwargs):
        data = dict(**kwargs).get('data')
        jsons = dict(**kwargs).get('jsons')
        params = dict(**kwargs).get('params')
        headers = dict(**kwargs).get('headers')

        logger.info('测试url为: {}'.format(self.base_url+url))
        logger.info('测试方法为: {}'.format(method))

        if data:
            logger.info('data参数为\n{}'.format(json.dumps(data, indent=2, ensure_ascii=False)))
        if jsons:
            logger.info('jsons参数为\n{}'.format(json.dumps(json, indent=2, ensure_ascii=False)))
        if params:
            logger.info('params参数为\n{}'.format(json.dumps(params, indent=2, ensure_ascii=False)))
        if headers:
            logger.info('headers参数为\n{}'.format(json.dumps(headers, indent=2, ensure_ascii=False)))



requestutil = RequestUtil()


if __name__ == '__main__':
    # requestutil.request()
    pass
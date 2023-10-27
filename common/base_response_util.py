# python3.8 (python版本)
# -*- coding: utf-8 -*-
# @Author  : ZYC
# @Software: PyCharm
# @Time    : 2023/10/17 15:39
# @File    : base_response_util.py
class BaseResponse:
    def __init__(self):
        self.success = True

base_response = BaseResponse()

if __name__ == '__main__':
    base_response.body = 'dsafa'
    print(base_response.body)
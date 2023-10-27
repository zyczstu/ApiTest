# python3.8 (python版本)
# -*- coding: utf-8 -*-
# @Author  : ZYC
# @Software: PyCharm
# @Time    : 2023/10/17 14:59
# @File    : keywords.py
from common.requests_util import requestutil
import sys


class Api:

    # 获取手机验证码
    def send_code(self, **kwargs):
        res = requestutil.request(**kwargs)
        return res

    # 注册
    def register(self, **kwargs):
        res = requestutil.request(**kwargs)
        return res

    # 登录
    def login(self, **kwargs):
        res = requestutil.request(**kwargs)
        return res

    # 轮播图
    def banners(self, **kwargs):
        res = requestutil.request(**kwargs)
        return res

    # 添加购物车
    def add_shoppingcart(self, **kwargs):
        res = requestutil.request(**kwargs)
        return res

    # 个人留言
    def add_message(self, **kwargs):
        res = requestutil.request(**kwargs)
        return res

api = Api()

if __name__ == '__main__':
    print(sys.path)

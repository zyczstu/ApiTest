# python3.8 (python版本)
# -*- coding: utf-8 -*-
# @Author  : ZYC
# @Software: PyCharm
# @Time    : 2023/10/17 15:16
# @File    : user_api.py
from base_key.keywords import api
from common.response_util import process_response
from common.rw_data import getdata


def get_code(method, url, json_data):
    """
    注册时获取手机号验证码
    :param method: 请求方法
    :param url: 请求地址
    :param json_data: 请求数据
    :return: response返回结果
    """
    res = api.send_code(method=method, url=url, json=json_data)
    response = process_response(res)
    return response


def register(method, url, mobile, verifycode):
    """
    注册账号
    :param method: 请求方法
    :param url: 请求地址
    :param mobile: 注册手机号
    :param verifycode: 验证码
    :return: response返回结果
    """
    register_json = {"password": "123456", "username": str(mobile), "code": str(verifycode)}
    res = api.register(method=method, url=url, json=register_json)
    response = process_response(res)
    return response


def login(data):
    """
    登录
    :param data: 登录数据
    :return: 登录结果
    """
    res = api.login(method=data['method'], url=data['url'], json=data['data'])
    response = process_response(res)
    return response


def banners(data):
    """
    轮播图
    :param data: 轮播图数据
    :return:
    """
    res = api.banners(method=data['method'], url=data['url'])
    response = process_response(res)
    return response


def add_shoppingcart(data, headers):
    """
    添加购物车
    :param data:
    :param headers:
    :return:
    """
    # headers = {
    #     "Authorization": "JWT " + token
    # }
    res = api.add_shoppingcart(method=data['method'], url=data['url'], headers=headers, json=data['data'])
    response = process_response(res)
    return response


def add_message(data, headers):
    # headers = {
    #     "Authorization": "JWT " + token
    # }
    file_stream = getdata.read_file(data['file'])
    file = {"file": (data['file'], file_stream, data['file_content_type'])}
    res = api.add_message(method=data['method'], url=data['url'], headers=headers, files=file, data=data['data'])
    response = process_response(res)
    return response

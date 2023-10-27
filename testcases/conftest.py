# python3.8 (python版本)
# -*- coding: utf-8 -*-
# @Author  : ZYC
# @Software: PyCharm
# @Time    : 2023/10/25 14:36
# @File    : conftest.py
import os
import pytest
from base_key.user_api import login
from common.rw_data import getdata


# @pytest.fixture(scope='session')
# def login_fixture():
#     if 'token' not in os.environ:
#         com_login, login_data = getdata.read_data('test_login.yaml')
#         normal_login = login_data[0]
#         res = login(normal_login)
#         print('---------进行登录操作---------------')
#         os.environ['token'] = res.body['token']
#         token = os.environ['token']
#         yield token
#         del os.environ['token']
#         print('token >>>> ', os.environ.get('token'))
#     else:
#         return os.environ['token']
@pytest.fixture(scope='session')
def headers_fixture():
    com_login, login_data = getdata.read_data('test_login.yaml')
    normal_login = login_data[0]
    res = login(normal_login)
    print('---------进行登录操作---------------')
    token = res.body['token']
    headers = {
        "Authorization": "JWT " + token
    }
    return headers


@pytest.fixture(scope='function')
def get_mobile():
    com_login, login_data = getdata.read_data('test_login.yaml')
    normal_login = login_data[0]
    mobile = str(normal_login['data']['username'])
    return mobile
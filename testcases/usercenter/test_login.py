# python3.8 (python版本)
# -*- coding: utf-8 -*-
# @Author  : ZYC
# @Software: PyCharm
# @Time    : 2023/10/20 15:13
# @File    : test_login.py
import allure
import pytest

from common.assert_util import login_assert
from common.rw_data import getdata
from common.allure_util import dynamic_allure
from base_key.user_api import login

com_data, login_data = getdata.read_data('test_login.yaml')

@allure.epic('美客生鲜网站测试')
@allure.feature('用户中心模块')
class TestLogin:
    @pytest.mark.parametrize('in_data', login_data, ids=[i['detail'] for i in login_data])
    def test_login(self, in_data):
        dynamic_allure(com_data)
        res = login(in_data)
        login_assert(res, in_data)
        assert res.success is in_data['success']


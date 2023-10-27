# python3.8 (python版本)
# -*- coding: utf-8 -*-
# @Author  : ZYC
# @Software: PyCharm
# @Time    : 2023/10/26 9:36
# @File    : test_addmessage.py
import allure
import pytest
from common.rw_data import getdata
from common.allure_util import dynamic_allure
from base_key.user_api import add_message


com_data, message_data = getdata.read_data('test_addmessage.yaml')

@allure.epic('美客生鲜网站测试')
@allure.feature('用户中心模块')
class TestAddMessage:

    @pytest.mark.parametrize('in_data', message_data, ids=[i['detail'] for i in message_data])
    def test_add_message(self, in_data, headers_fixture):
        dynamic_allure(com_data)
        headers = headers_fixture
        res = add_message(in_data, headers)
        assert res.success == in_data['success']
        assert res.body['subject'] == in_data['assert_value1']
        assert res.body['message'] == in_data['assert_value2']
        assert res.body['message_type'] == in_data['assert_value3']


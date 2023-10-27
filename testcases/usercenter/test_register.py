# python3.8 (python版本)
# -*- coding: utf-8 -*-
# @Author  : ZYC
# @Software: PyCharm
# @Time    : 2023/10/17 16:19
# @File    : test_register.py
from base_key.user_api import get_code, register
import pytest
import allure
from common.rw_data import getdata
from common.fake_data import fake_data
from common.allure_util import dynamic_allure
from common.log_util import logger
from testcases.usercenter.usercenter_sql import get_verifycode,delete_verifycode,delete_test_user

data = getdata.read_yaml('test_register.yaml')


@allure.epic('美客生鲜网站测试')
@allure.feature('用户中心模块')
class TestRegister:
    @pytest.mark.parametrize('input', data['test_register'])
    def test_register01(self, input):
        dynamic_allure(input)
        request_vr = input['verifycode']
        request_re = input['register']
        get_code_json = fake_data(request_vr['json'])
        print('get_code_json: >>>>>', get_code_json)
        mobile = get_code_json['mobile']
        res_code = get_code(method=request_vr['method'], url=request_vr['url'], json_data=get_code_json)
        verifycode = get_verifycode(mobile)['code']
        # print('mobile: >>>', mobile)
        logger.info('verifycode: >>>', verifycode)
        res_register = register(method=request_re['method'], url=request_re['url'], mobile=mobile,
                                verifycode=verifycode)
        delete_test_user(mobile)
        delete_verifycode(mobile)
        assert res_code.success == True
        assert res_register.success == True



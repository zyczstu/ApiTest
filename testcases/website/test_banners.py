# python3.8 (python版本)
# -*- coding: utf-8 -*-
# @Author  : ZYC
# @Software: PyCharm
# @Time    : 2023/10/21 16:40
# @File    : test_banners.py
import allure
import pytest
from base_key.user_api import banners
from testcases.website.website_sql import get_banners_num
from common.rw_data import getdata
from common.allure_util import dynamic_allure
com_data, banners_data = getdata.read_data('test_banners.yaml')

@allure.epic('美客生鲜网站测试')
@allure.feature('轮播图模块')
class TestBanners:
    @pytest.mark.parametrize('in_data', banners_data)
    def test_banners(self, in_data):
        dynamic_allure(com_data)
        num = get_banners_num()
        res = banners(in_data)
        assert res.success == True
        assert len(res.body) == num

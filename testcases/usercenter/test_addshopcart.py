import allure
import pytest

from common.rw_data import getdata
from common.allure_util import dynamic_allure
from base_key.user_api import add_shoppingcart
from testcases.usercenter.usercenter_sql import select_goodsnum


com_goods, goods_data = getdata.read_data('test_addgoods.yaml')

@allure.epic('美客生鲜网站测试')
@allure.feature('用户中心模块')
class TestAddGoods:

    @pytest.mark.parametrize('in_data', goods_data, ids=[i['detail'] for i in goods_data])
    def test_addgoods(self,in_data, headers_fixture, get_mobile):
        dynamic_allure(com_goods)
        headers = headers_fixture
        mobile = get_mobile
        res = add_shoppingcart(in_data, headers)
        goods_id = in_data['data']['goods']
        nums = select_goodsnum(mobile, goods_id)
        assert res.success is in_data['success']
        assert in_data['value'] == res.body['goods']
        assert res.body['nums'] == nums


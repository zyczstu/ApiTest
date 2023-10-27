# python3.8 (python版本)
# -*- coding: utf-8 -*-
# @Author  : ZYC
# @Software: PyCharm
# @Time    : 2023/10/20 18:27
# @File    : assert_util.py


def login_assert(res, ast_data):
    status_code = ast_data['status_code']
    assert_data = ast_data['assert_data']
    type = ast_data['type']
    value = ast_data['value']
    if type == '==':
        assert res.status_code == status_code
        assert res.body == {assert_data: value}
    if type == 'is not':
        assert res.body is not None




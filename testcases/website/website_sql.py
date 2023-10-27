# python3.8 (python版本)
# -*- coding: utf-8 -*-
# @Author  : ZYC
# @Software: PyCharm
# @Time    : 2023/10/21 16:42
# @File    : website_sql.py
from common.sql_util import sqldb


def get_banners_num():
    sql = "select count(1) as banners_num from goods_banner"
    result = sqldb.select_sql_one(sql)
    return result['banners_num']

# python3.8 (python版本)
# -*- coding: utf-8 -*-
# @Author  : ZYC
# @Software: PyCharm
# @Time    : 2023/10/20 18:38
# @File    : usercenter_sql.py
from common.sql_util import sqldb


def get_verifycode(mobile):
    sql = f"SELECT code FROM users_verifycode WHERE mobile={mobile} ORDER BY add_time DESC LIMIT 0,1;"
    verifycode = sqldb.select_sql_one(sql)
    return verifycode


def delete_test_user(mobile):
    sql = f"DELETE FROM users_userprofile WHERE mobile={mobile};"
    sqldb.execute_sql(sql)


def delete_verifycode(mobile):
    sql = f"DELETE FROM users_verifycode WHERE mobile={mobile};"
    sqldb.execute_sql(sql)


def select_user_id(mobile):
    sql = f"SELECT id FROM users_userprofile WHERE mobile={mobile};"
    user_id = sqldb.select_sql_one(sql)['id']
    return user_id


def select_goodsnum(mobile, goods_id):
    user_id = select_user_id(mobile)
    sql = f"SELECT nums FROM trade_shoppingcart WHERE user_id={user_id} and goods_id={goods_id};"
    nums = sqldb.select_sql_one(sql)['nums']
    return nums

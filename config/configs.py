# python3.8 (python版本)
# -*- coding: utf-8 -*-
# @Author  : ZYC
# @Software: PyCharm
# @Time    : 2023/10/17 14:54
# @File    : configs.py


class SqlConfig:
    host = '127.0.0.1'
    port = 3306
    user = 'root'
    password = 'abc123'
    database = 'mydb2'
    charset = 'utf8mb4'

sqlconfig = SqlConfig()

if __name__ == '__main__':
    a = getattr(sqlconfig, 'host')
    print(a)
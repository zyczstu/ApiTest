# python3.8 (python版本)
# -*- coding: utf-8 -*-
# @Author  : ZYC
# @Software: PyCharm
# @Time    : 2023/10/17 14:58
# @File    : fake_data.py
from faker import Faker
from faker.generator import random
from common.rw_data import getdata
import json

from common.sql_util import sqldb

fake = Faker(locale='zh_CN')


def fake_data(data):
    if isinstance(data, dict):
        for k, v in data.items():
            if '${' and '}' in str(v):
                start = str(v).index('{')
                end = str(v).index('}')
                data[k] = eval(str(v)[start + 1:end])
    return data


def random_name():
    return fake.name()


def random_age():
    age = random.randint(1, 100)
    return age


def random_phone():
    phone_number = fake.phone_number()
    return phone_number


if __name__ == '__main__':
    dic = {'sex': 'man', 'name': '${random_name()}', 'age': '${random_age()}', 'phone': '${random_phone()}'}
    data = fake_data(dic)
    print(data)
    # datas = getdata.read_yaml('test_register.yaml')
    # print(datas)
    # print(type(datas.get('test_register')[0]['request']['json']))
    # data = fake_data(datas.get('test_register')[0]['request']['json'])
    # print(data)


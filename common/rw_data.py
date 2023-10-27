# python3.8 (python版本)
# -*- coding: utf-8 -*-
# @Author  : ZYC
# @Software: PyCharm
# @Time    : 2023/10/17 14:55
# @File    : rw_data.py
import json

import yaml
import os
import configparser


project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_path = os.path.join(project_path, 'data')

class fanshe:
    pass

# 获取数据
class GetData:

    # 获取yaml文件数据
    def read_yaml(self, file_name):
        file_path = os.path.join(data_path, file_name)
        with open(file_path, mode='r', encoding='utf-8') as f:
            yaml_data = yaml.safe_load(f)
        return yaml_data

    # 获取ini文件数据
    def read_ini(self, file_name):
        config = configparser.ConfigParser()
        file_path = os.path.join(data_path, file_name)
        config.read(file_path, encoding='utf-8')
        return config

    def read_data(self,file_name):
        loging_data = []
        data = self.read_yaml(file_name)
        data_idx = list(data)[1:len(data)]
        dic_common = data['common_data']
        for case_name in data_idx:
            loging_data.append(data[case_name])

        return dic_common, loging_data

    def read_file(self, file_name):
        file_path = os.path.join(data_path, file_name)
        with open(file_path, 'rb') as file:
            file_stream = file.read()
        return file_stream


# 写入数据
class WriteData:

    # 写入yaml
    def write_yaml_w(self, file_name, data):
        file_path = os.path.join(data_path, file_name)
        with open(file_path, mode='w', encoding='utf-8') as f:
            yaml.dump(data, f, allow_unicode=True)

    # 追加yaml
    def write_yaml_a(self, file_name, data):
        file_path = os.path.join(data_path, file_name)
        with open(file_path, mode='a', encoding='utf-8') as f:
            yaml.dump(data, f, allow_unicode=True)

    # 清理yaml
    def clean_yaml(self, file_name):
        file_path = os.path.join(data_path, file_name)
        with open(file_path, mode='w', encoding='utf-8') as f:
            yaml.dump(f)


getdata = GetData()
writedata = WriteData()


if __name__ == '__main__':
    # data = getdata.read_yaml('test_login.yaml')
    # data = getdata.read_yaml('test_register.yaml')
    # common_data, login_data = getdata.read_data('test_login.yaml')
    # print(common_data)
    # print(type(login_data[1]['value']))
    passa = getdata.read_file('c.png')
    print(passa)




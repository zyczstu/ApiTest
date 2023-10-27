# python3.8 (python版本)
# -*- coding: utf-8 -*-
# @Author  : ZYC
# @Software: PyCharm
# @Time    : 2023/10/17 14:57
# @File    : allure_util.py
import allure


def dynamic_allure(opt):
    story = opt['story']
    description = opt['description']
    severity = opt['severity']
    testcase = opt['testcase']
    allure.dynamic.story(story)
    allure.dynamic.description(description)
    allure.dynamic.severity(severity_level=severity)
    allure.dynamic.testcase(testcase)

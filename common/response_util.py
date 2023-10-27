# python3.8 (python版本)
# -*- coding: utf-8 -*-
# @Author  : ZYC
# @Software: PyCharm
# @Time    : 2023/10/17 15:34
# @File    : response_util.py
from common.base_response_util import base_response
from common.log_util import logger
import json


def process_response(res):
    """
    处理接口返回数据，判断返回状态码是否正确，显示返回内容
    :param res: 接口返回数据
    :return:
    """
    if res.status_code == 200 or res.status_code == 201:
        base_response.success = True
        try:
            base_response.body = res.json()
            base_response.status_code = res.status_code
            logger.info(f"接口返回内容为 >> {json.dumps(base_response.body, ensure_ascii=False)}")
        except:
            logger.warning('返回不是json格式')
    else:
        base_response.success = False
        try:
            base_response.body = res.json()
            base_response.status_code = res.status_code
            logger.info(f"接口返回内容为 >> {json.dumps(base_response.body, ensure_ascii=False)}")
        except:
            logger.warning('返回不是json格式')
        logger.info(f"接口返回状态码为{base_response.status_code}，请检查接口")

    return base_response

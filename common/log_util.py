# python3.8 (python版本)
# -*- coding: utf-8 -*-
# @Author  : ZYC
# @Software: PyCharm
# @Time    : 2023/10/17 15:00
# @File    : log_util.py
from loguru import logger
import os
from datetime import datetime

current_time = datetime.now().strftime("%Y_%m_%d")
root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
log_path = os.path.join(root_path, 'log')
log_file = f'{current_time}.log'
logger.add(os.path.join(log_path, log_file), format='{time} {level} {message}', level='INFO', encoding='utf8')
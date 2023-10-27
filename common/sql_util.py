# python3.8 (python版本)
# -*- coding: utf-8 -*-
# @Author  : ZYC
# @Software: PyCharm
# @Time    : 2023/10/19 15:53
# @File    : sql_util.py
import pymysql
from common.rw_data import getdata
from common.log_util import logger
data = getdata.read_ini('conf.ini')['mysql']


sql_data = {
    "host": data['host'],
    "port": int(data['port']),
    "user": data['user'],
    "password": data['password'],
    "db": data['db'],
    "charset": data['charset']
}

class SqlUtil:

    def __init__(self, sql_data):
        try:
            self.db = pymysql.connect(**sql_data, autocommit=True)
            logger.info('------------------Mysql连接成功------------------')
        except:
            logger.info('------------------Mysql连接失败------------------')

        self.cursor = self.db.cursor(cursor=pymysql.cursors.DictCursor)

    def __del__(self):
        self.cursor.close()
        self.db.close()
        logger.info('------------------关闭Mysql连接------------------')

    # 查询所有数据
    def select_sql_all(self, sql):
        try:
            logger.info(f'执行select类型sql语句 >>> {sql}')
            self.cursor.execute(sql)
            sql_result = self.cursor.fetchall()
            logger.info('------------------Mysql查询成功------------------')
            logger.info(f'sql返回{sql_result}')
            return sql_result
        except:
            logger.warning('------------------Mysql查询失败------------------')

    # 查询一条数据
    def select_sql_one(self, sql):
        try:
            logger.info(f'执行select类型sql语句 >>> {sql}')
            self.cursor.execute(sql)
            sql_result = self.cursor.fetchone()
            logger.info('------------------Mysql查询成功------------------')
            logger.info(f'sql返回{sql_result}')
            return sql_result
        except:
            logger.warning('------------------Mysql查询失败------------------')

    # 执行sql
    def execute_sql(self, sql):
        try:
            sql_list = ['insert', 'delete', 'update']
            for sql_type in sql_list:
                if sql_type in sql:
                    logger.info(f'执行{sql_type}类型sql语句 >>> {sql}')
            self.cursor.execute("START TRANSACTION;")
            self.cursor.execute(sql)
            self.db.commit()
            logger.info('------------------Mysql执行成功------------------')
        except:
            self.db.rollback()
            logger.warning('------------------Mysql执行失败,进行回滚------------------')

sqldb = SqlUtil(sql_data)


if __name__ == '__main__':
    sql = "SELECT code FROM users_verifycode ORDER BY add_time DESC LIMIT 0,1;"
    verify_code = sqldb.execute_sql(sql)
    print(verify_code)
    del sqldb
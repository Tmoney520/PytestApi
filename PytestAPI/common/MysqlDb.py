# -*- coding: utf-8 -*- 
"""          
# @Time   : 2023/2/25 18:19
# @Author :TGW
"""

import pymysql
import configparser


class MysqlDb:

    def __init__(self, configpath, db):
        # 实例config工具
        config = configparser.ConfigParser()
        # 读取文件数据(ini文件)
        config.read(configpath)
        host = config[db]['host']
        port = int(config[db]['port'])
        user = config[db]['user']
        password = config[db]['password']
        database = config[db]['database']
        charset = config[db]['charset']

        try:
            self.con = pymysql.connect(host=host, port=port, user=user, password=password, database=database,
                                       charset=charset)
        except Exception as e:
            print('初始化连接失败' % e)

        # 创建游标
        self.cur = self.con.cursor()

    def select_query(self, sql):
        try:
            # 执行sql
            self.cur.execute(sql)
            # 有结果 拿到结果
            result = self.cur.fetchall()
            # 把结果返回
            return result
        except Exception as e:
            print('查询失败' % e)

    def idu_query(self, sql):
        try:
            # 执行sql
            self.cur.execute(sql)
            self.cur.execute('commit')
            return True
        except Exception as e:
            print('增删改失败' % e)

    # 关闭游标和连接
    def close_db(self):
        self.cur.close()
        self.con.close()
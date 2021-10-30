# -*- coding: utf-8 -*-
# @Time : 2021-10-28 10:16
# @Author : bai ping
# @QQ : 376706275
import pymysql


class DbHandle:

    def __init__(self,host, user, password, database,port,charset='utf8'):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port
        self.charset = charset

    def get_conn(self):
        try:
            conn = pymysql.connect(host=self.host,user=self.user,password=self.password,database=self.database,
                                   port=self.port,charset=self.charset)
            return conn
        except Exception as e:
            print(e,'pymysql connect error~')


    def search_data(self,sql,param=None):
        try:
            conn = self.get_conn()
            cursor = conn.cursor()
            cursor.execute(sql,param)
            res = cursor.fetchall()
            conn.commit()
        except Exception as e:
            print(e,'operation error~')
            conn.rollback()
        finally:
            cursor.close()
            conn.close()
        return res


    def update_data(self,sql,param):
        try:
            conn = self.get_conn()
            cursor = conn.cursor()
            cursor.execute(sql, param)
            conn.commit()
        except Exception as e:
            print(e, 'operation error~')
            conn.rollback()
        finally:
            cursor.close()
            conn.close()
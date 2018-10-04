#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging

from twisted.enterprise import adbapi


class MySQLPipeline(object):
    def __init__(self, dbpool):
        self.__dbpool = dbpool

    @classmethod
    def from_crawler(cls, crawler):
        # 获得数据库配置
        MYSQL_SETTINGS = crawler.settings.get('MYSQL_SETTINGS')
        # 进行配置
        dbparams = dict(
            host=MYSQL_SETTINGS['HOST'],
            db=MYSQL_SETTINGS['DATABASE'],
            user=MYSQL_SETTINGS['USER'],
            passwd=MYSQL_SETTINGS['PASSWORD'],
            charset=MYSQL_SETTINGS['CHARSET']
        )
        # 创建mysql连接池
        dbpool = adbapi.ConnectionPool('pymysql', **dbparams)
        return cls(dbpool)

    def process_item(self, item, spider):
        defferd = self.__dbpool.runInteraction(self.db_insert, item)
        defferd.addErrback(self.db_error_handle, item, spider)
        return item

    def db_error_handle(self, failure, item, spider):
        logging.error(f"db_error_handle has error {failure}")

    def db_insert(self, cursor, item):
        data = dict(item)
        keys = ', '.join(data.keys())
        values = ', '.join(['%s'] * len(data))
        sql = '''
            insert into %s (%s) values(%s)
        ''' % (item.table_name, keys, values)
        logging.info(sql)
        cursor.execute(sql, tuple(data.values()))
        return True

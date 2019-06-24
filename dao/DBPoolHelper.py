# -*- coding: utf-8 -*-
"""
Created on June 18, 2019

DataBase connection pool.

@author: Zewen Huang
"""
from sys import  path
path.append('../config')

import logging
from mylogger import MyLogger
from mysql.connector import Error, pooling
from DBPoolConfigParser import DBPoolConfigParser

logger = MyLogger('dbpoolconfigparser', logging.INFO).get_logger()


class MySQLPool(object):
    def __init__(self, pool_token):
        self._connection_pool = self._init_pool(pool_token)

    def _init_pool(self, pool_token):
        try:
            connection_pool = pooling.MySQLConnectionPool(**pool_token)

            return connection_pool
        except Exception as e:
            logger.error("Fail to initialize MySQL database pool.")
            exit(1)

    def test_connection(self):
        try:
            connection_object = self._connection_pool.get_connection()
            if connection_object.is_connected():
                db_info = connection_object.get_server_info()
                logger.info('Connected to MySQL database using connection pool ... MySQL Server version on {}'
                            .format(db_info))

                cursor = connection_object.cursor()
                cursor.execute("SELECT DATABASE();")
                record = cursor.fetchone()
                logger.info('Success to connect to database: {}'.format(record[0]) )
        except Exception as e:
            logger.error(e)
        finally:
            if connection_object is not None and \
                    connection_object.is_connected():
                cursor.close()
                connection_object.close()
                logger.info('Connection is closed.')


if __name__ == "__main__":
    parser = DBPoolConfigParser()
    vlm_db_pool_cfg = parser.get_vlm_db_pool_cfg()
    print(vlm_db_pool_cfg)
    db_pool = MySQLPool(vlm_db_pool_cfg)

    db_pool.test_connection()
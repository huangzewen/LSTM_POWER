# -*- coding: utf-8 -*-
"""
Created on June 18, 2019

This module is used to parse config file of .ini type.

@author: Zewen Huang
"""
import os
from configparser import ConfigParser
from mylogger import MyLogger
import logging

CFG_PATH = os.path.join(os.path.expanduser('~'),
                        'git/favorites-web/LSTM_Power/config/configfile/db_connector_pool.ini')

SECTION_VLM = 'vlm_db'
logger = MyLogger('dbpoolconfigparser', logging.INFO).get_logger()


class DBPoolConfigParser(object):
    def __init__(self, cfg_path=CFG_PATH):
        self._cfg_path = cfg_path
        self._parser = ConfigParser()
        self._parser.read(self._cfg_path)

    def get_vlm_db_pool_cfg(self, section=SECTION_VLM):
        vlm_db_pool_cfg= {}
        try:
            vlm_db_pool_cfg['pool_name'] = self._parser.get(section, 'pool_name')
            vlm_db_pool_cfg['pool_size'] = self._parser.getint(section, 'pool_size')
            vlm_db_pool_cfg['pool_reset_session'] = self._parser.getboolean(section, 'pool_reset_session')
            vlm_db_pool_cfg['host'] = self._parser.get(section, 'host')
            vlm_db_pool_cfg['database'] = self._parser.get(section, 'database')
            vlm_db_pool_cfg['user'] = self._parser.get(section, 'user')
            vlm_db_pool_cfg['password'] = self._parser.get(section, 'password')
            vlm_db_pool_cfg['connection_timeout'] = self._parser.getint(section, 'connection_timeout')
            vlm_db_pool_cfg['charset'] = self._parser.get(section, 'charset')
            return vlm_db_pool_cfg
        except Exception as e:
            logger.error(e)


if __name__ == "__main__":
    parser = DBPoolConfigParser()
    vlm_db_pool_cfg = parser.get_vlm_db_pool_cfg()
    print(vlm_db_pool_cfg)
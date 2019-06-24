# -*- coding: utf-8 -*-
"""
Created on June 18, 2019

Logger module

@author: Huang Zewen
"""

import logging
import socket
import getpass

FORMAT = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'

EXTRA = {'clientip':  socket.gethostbyname(socket.gethostname()),
         'user': getpass.getuser()}

class MyLogger(object):
    def __init__(self, logger_name, logger_level):
        self._logger = None
        self._logger_name = logger_name
        self._logger_level = logger_level
        self.config_logger()

    def config_logger(self, format=FORMAT):
        logging.basicConfig(format=format)
        self._logger = logging.getLogger(self._logger_name)
        self._logger = logging.LoggerAdapter(self._logger, EXTRA)
        self._logger.setLevel(self._logger_level)

    def get_logger(self):
        return self._logger
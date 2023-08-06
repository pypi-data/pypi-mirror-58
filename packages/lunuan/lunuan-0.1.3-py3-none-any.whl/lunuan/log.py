#!/usr/bin/env python3
#coding=utf-8

import logging

class LogFormat:
    '''
    预定义日志格式\n
    logFilePath: 存放日志文件的路径\n
    ConsoleLogLevel、FileLogLevel: 指定控制台和文件日志等级\n
    LogLevel={ DEBUG:10, INFO:20, WARNING:30, ERROR:40, CRITICAL:50 }\n
    Formatter: 重写Formatter时指定, 默认为None即使用预定义格式\n
    '''
    __formatter = logging.Formatter('%(asctime)s %(levelname)s  %(message)s')
    def __init__(self, logFilePath, ConsoleLogLevel=logging.DEBUG, FileLogLevel=logging.DEBUG, Formatter=None):
        Formatter = self.__formatter if Formatter == None else logging.Formatter(Formatter)
        self.logger = logging.getLogger(logFilePath)
        self.logger.setLevel(logging.DEBUG)
        '''define file handler'''
        __file_handler = logging.FileHandler(logFilePath)
        __file_handler.setLevel(FileLogLevel)
        __file_handler.setFormatter(Formatter)   
        '''define console handler'''
        __console_handler = logging.StreamHandler()
        __console_handler.setLevel(ConsoleLogLevel)
        __console_handler.setFormatter(Formatter)
        '''binding handler'''
        self.logger.addHandler(__file_handler)
        self.logger.addHandler(__console_handler)

    def debug(self, message):
        '''level = 10'''
        self.logger.debug(message)

    def info(self, message):
        '''level = 20'''
        self.logger.info(message)

    def warning(self, message):
        '''level = 30'''
        self.logger.warning(message)

    def error(self, message):
        '''level = 40'''
        self.logger.error(message)

    def critical(self, message):
        '''level = 50'''
        self.logger.critical(message)

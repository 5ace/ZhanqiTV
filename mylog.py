#!/usr/bin/python3
#author = 'zeek'

import logging

logging.basicConfig(level    = logging.DEBUG,
                    format   = '%(asctime)s %(message)s',
                    filename = r'zhanqi.log',
                    filemode = 'w')

def writeLog(logType, message):
    message='[%s] %s' % (logType,message)
    logging.info(message)

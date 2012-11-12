#!/usr/bin/python

import logging
import logging.handlers

# create logger
logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)


ch2 = logging.FileHandler("hello.log")
ch2.setLevel(logging.ERROR)
formatter = logging.Formatter('%(levelname)s - %(message)s')
# add formatter to ch
ch2.setFormatter(formatter)
# add ch to logger
logger.addHandler(ch2)

ch3 = logging.handlers.DatagramHandler("165.114.86.227", 8888)
ch3.setLevel(logging.INFO)
formatter = logging.Formatter('%(levelname)s - %(message)s')
# add formatter to ch
ch3.setFormatter(formatter)
# add ch to logger
#logger.addHandler(ch2)


# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')
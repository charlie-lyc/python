# Logging Formatter
# - 로그의 결과값의 포맷을 지정해 줄 수 있음

import logging

logger = logging.getLogger('myapp')
hdlr = logging.FileHandler('myapp.log')

formatter = logging.Formatter('%(asctime)s %(levelname)s %(process)d %(message)s')
hdlr.setFormatter(formatter)

logger.addHandler(hdlr)

logger.setLevel(logging.INFO)
logger.info('Here we are')
logger.error('Error occurred')
# Example : Log Config File
import logging
# import logging.config
from logging import config
import csv

config.fileConfig('logging.conf')
logger = logging.getLogger()

USA_customers_list = []
try:
    with open('customers.csv', 'r') as customer_data:
        logger.info('Open file {0}'.format('customers.csv'))
        customer_reader = csv.reader(customer_data, delimiter=',', quotechar='"')
        for customer in customer_reader:
            if customer[10].upper() == 'USA':
                USA_customers_list.append(customer)
                logger.info('ID {0} added'.format(customer[0]))
except FileNotFoundError as e:
    logger.error('File NOT found {0}'.format(e))
customer_data.close()

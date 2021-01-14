__author__ = 'chandra'

import logging
import logging.handlers
# import logstash

logger = logging.getLogger(__name__)

# Set logging level accross the logger. Set to INFO in production
logger.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# LogstashLog Handler
#logstash_handler = logstash.LogstashHandler("54.191.32.247", 5544, version=1)

#Local File Handler
# create file handler which logs even debug messages
file_handler = logging.FileHandler( __name__ + '_file.log')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)

# create console handler with debug level
# This should be changed to ERROR in production
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)
# logger.addHandler(logstash_handler)


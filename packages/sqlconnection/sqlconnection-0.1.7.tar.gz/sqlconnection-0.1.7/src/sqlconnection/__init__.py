import logging
import os, sys
from dotenv import load_dotenv
logger = None


def init_app():
    if not load_dotenv(override=False):
        print('Could not find any .env file. The module will depend on system env only')
    global logger
    logger = logging.getLogger()
    if len(logger.handlers) == 0:
        stream_handler = logging.StreamHandler(sys.stdout)
        if os.environ.get('LOG_LEVEL'):
            stream_handler.setLevel(os.environ.get('LOG_LEVEL'))
            logger.setLevel(os.environ.get('LOG_LEVEL'))
        logger.addHandler(stream_handler)
    logger.info("Load module = {}, environment={}, region={}\n".format(
        os.environ.get('APP_NAME'), os.environ.get('ENVIRONMENT'), os.environ.get('REGION')))


if __name__ == 'sqlconnection':
    init_app()


from sqlconnection import postgresql as postgresql
from sqlconnection import postgresql_queries as postgresql_queries

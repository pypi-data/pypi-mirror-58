#-*- coding: utf-8-*-
import socket
import logging
from logging.handlers import SysLogHandler
import google.cloud.logging
import os

logger = None
APP_NAME = os.getenv('APP_NAME', '__name__')
LOG_LEVEL = os.getenv('LOG_LEVEL', 'DEBUG')
LOG_HOST = os.getenv('LOG_HOST', 'logs5.papertrailapp.com')
LOG_PORT = os.getenv('LOG_PORT', 27971)
ENV = os.getenv('ENV', 'LOCAL')

# Instantiates a client
client = None
try:
    client = google.cloud.logging.Client()
    # # Connects the logger to the root logging handler with log level debug or higher
    # client.setup_logging(log_level=getattr(logging,LOG_LEVEL))
except Exception:
    logging.info('Not GCP credentials')


def create_logger(name=APP_NAME):
    ''' Create logger and add handlers and filters
    '''
    global logger
    logger = logging.getLogger(name)

    log_format = '%(service)s %(hostname)s: [%(env)s] %(message)s '
    log_formatter = logging.Formatter(log_format,datefmt='%b %d %H:%M:%S')
    log_filter = ContextFilter()
    remote_handler = SysLogHandler(address=(LOG_HOST, int(LOG_PORT)))
    remote_handler.setFormatter(log_formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_formatter)

    if client is not None:
        hdlr = client.get_default_handler()
        # google.cloud.logging.handlers.setup_logging(hdlr)
        logger.addHandler(hdlr)
        logger.addHandler(logging.StreamHandler())
    
    logger.setLevel(LOG_LEVEL)
    logger.addFilter(log_filter)

    
    logger.addHandler(console_handler)
    logger.addHandler(remote_handler)


def get_logger():
    ''' Get the app logger by the app name
    '''
    return logging.getLogger(APP_NAME)


class ContextFilter(logging.Filter):
    hostname = socket.gethostname()
    service = APP_NAME
    env = ENV

    def filter(self, record):
        record.hostname = ContextFilter.hostname
        record.service = ContextFilter.service
        record.env = ContextFilter.env
        return True


class AppLogger(object):
    ''' General apps logger
    '''
    logger = None
    level = None
    format = '%(asctime)s %(service)s %(hostname)s %(levelname)s: %(message)s'
    filer = None
    # handlers
    console = None
    remote = None
    # remote 
    host = None
    port = None
    
    def __init__(self, level=LOG_LEVEL, host=LOG_HOST, port=LOG_PORT):
        ''' Instantiate loggers (remote and local)
            - Console handler: log to console
            - PaperTrail handler: send logs to remote host
        '''
        self.level = getattr(logging,level)
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(self.level)
        self.formatter = logging.Formatter(self.format,datefmt='%b %d %H:%M:%S')
        self.filter = ContextFilter()

        # Console Handler
        self.console = logging.StreamHandler()
        self.console.setFormatter(self.formatter)
        self.console.addFilter(self.filter)
        self.logger.addHandler(self.console)

        # Remote handler
        if host != None and port != None:
            self.host = host
            self.port = int(port)
            self.remote = SysLogHandler(address=(self.host, self.port))
            self.remote.addFilter(self.filter)
            self.remote.setFormatter(self.formatter)
            self.logger.addHandler(self.remote)

    def info(self,msg):
        ''' Info logging
        '''
        self.logger.info(msg)

    def debug(self,msg):
        ''' Debug logging
        '''
        self.logger.debug(msg)

    def warn(self,msg):
        ''' Warning logging
        '''
        self.logger.warn(msg)

    def error(self,msg):
        ''' Error logging
        '''
        self.logger.error(msg)

    def critical(self,msg):
        ''' Critical logging
        '''
        self.logger.critical(msg)


if __name__ == '__main__':
    logger = get_logger()
    logger.info('Info message sent!!')
    logger.debug('Debug message sent....')
    logger.warning('Warning message sent....')
    logger.error('Error!!! message sent....')

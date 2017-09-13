import os
import logging
import tempfile


project_name = "Telegraph"


class BaseConfig(object):
    DEBUG = True
    SECRET_KEY = os.environ.get('TELEGRAPH_SECRET', 'secret-key')
    APP_DIR = os.path.abspath(os.path.dirname(__file__))
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    SYSTEM_TEMP = tempfile.gettempdir()
    TELEGRAMS_PATH = SYSTEM_TEMP
    DEBUG_TB_ENABLED = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    JSON_AS_ASCII = False,
    LOGGER_NAME = "{}_log".format(project_name)
    LOG_LEVEL = logging.ERROR


class ProdConfig(BaseConfig):
    ENV = 'prod'
    DEBUG = False


class DevConfig(BaseConfig):
    ENV = 'dev'
    DEBUG = True
    DEBUG_TB_ENABLED = True
    LOG_LEVEL = logging.INFO
    SESSION_COOKIE_HTTPONLY = False

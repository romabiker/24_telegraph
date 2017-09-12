import os
import logging


project_name = "Telegraph"


class BaseConfig(object):
    """Base configuration."""
    DEBUG = True
    SECRET_KEY = os.environ.get('TELEGRAPH_SECRET', 'secret-key')
    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    TELEGRAMS_DIR = 'telegrams_storage'
    TELEGRAMS_PATH = os.path.join(APP_DIR, TELEGRAMS_DIR)
    DEBUG_TB_ENABLED = False  # Disable Debug toolbar
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    JSON_AS_ASCII = False,
    LOGGER_NAME = "{}_log".format(project_name)
    LOG_LEVEL = logging.ERROR


class ProdConfig(BaseConfig):
    """Production configuration."""
    ENV = 'prod'
    DEBUG = False


class DevConfig(BaseConfig):
    """Development configuration."""
    ENV = 'dev'
    DEBUG = True
    DEBUG_TB_ENABLED = True  # Inable Debug toolbar
    LOG_LEVEL = logging.INFO
    SESSION_COOKIE_HTTPONLY = False

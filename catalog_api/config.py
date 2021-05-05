import os
from dotenv import load_dotenv


load_dotenv()


class ProdConfiguration(object):
    SECRET_KEY = os.getenv('secret_key')
    # Щоб не виводило попередження при запуску сервера
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///catalog.db'


class TestConfiguration(object):
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SECRET_KEY = 'TEST_SECRET_SECRET_KEY'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'

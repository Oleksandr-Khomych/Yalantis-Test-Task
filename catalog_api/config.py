class Configuration(object):
    DEBUG = True
    SECRET_KEY = 'TEST_SECRET_SECRET_KEY'
    # Щоб не виводило попередження при запуску сервера
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///catalog.db'
    SQLALCHEMY_ECHO = True


# class TestConfiguration(object):
#     DEBUG = True
#     SECRET_KEY = 'TEST_SECRET_SECRET_KEY'
#     # Щоб не виводило попередження при запуску сервера
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#     SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
#

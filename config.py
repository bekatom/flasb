
class ProductionConfig(object):
    DEBUG = True
    TESTING = False
    MONGODB_SETTINGS = {'DB': 'flaskstarter_production'}
    SECRET_KEY = 'flask+mongoengine=<3'
    DEBUG_TB_INTERCEPT_REDIRECTS = False


class ProductionConfigHome(object):
    DEBUG = True
    TESTING = False
    MONGODB_SETTINGS = {'HOST': 'localhost', 'DB': 'test'}
    SECRET_KEY = 'flask+mongoengine=<3'
    DEBUG_TB_INTERCEPT_REDIRECTS = False


class TestConfig(object):
    DEBUG = True
    TESTING = True
    MONGODB_SETTINGS = {'DB': 'flaskstarter_test'}
    SECRET_KEY = 'flask+mongoengine=<3'
    DEBUG_TB_INTERCEPT_REDIRECTS = False

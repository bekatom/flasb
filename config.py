
class ProductionConfig(object):
    DEBUG = True
    TESTING = False
    MONGODB_SETTINGS = {'DB': 'flasb', 'USERNAME': 'vobi', 'PASSWORD': 'P@ssw0rd', 'HOST': 'ds053300.mongolab.com',
                        'PORT': 53300}
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


BOOTSTRAP_THEMS = [
    'cerulean',
    'cosmo',
    'cyborg',
    'darkly',
    'flatly',
    'journal',
    'lumen',
    'paper',
    'readable',
    'sandstone',
    'simplex',
    'slate',
    'spacelab',
    'superhero',
    'united',
    'yeti',
]
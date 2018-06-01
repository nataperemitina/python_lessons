
class BaseConfig(object):
    SECRET_KEY = 'Random string'
    WTF_CSRF_SECRET_KEY = 'Random string 2'


class DevConfig(BaseConfig):
    PONY = {
        'provider':'sqlite',
        'dbname': 'estore.sqlite'
    }

class ProdConfig(BaseConfig):
    PONY = {
        'provider':'mysql',
        'username':'name',
        'password':'pwd',
        'dbname': 'estore.sqlite'
    }
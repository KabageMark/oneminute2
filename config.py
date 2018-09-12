import os

class Config:

    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://markchege:newpassword@localhost/oneminutepitch'

    
    
class ProdConfig(Config):
    # SQLALCHEMY_DATABASE_URI = os.environ.get("HEROKU_POSTGRESQL_PURPLE_URL)
    pass
    


class DevConfig(Config):
    DEBUG = True
 
config_options = {
'development':DevConfig,
'production':ProdConfig
}
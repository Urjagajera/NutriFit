import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        "mysql+pymysql://root:password@localhost:3306/nutrifit_db"

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

# Select config based on environment
config_dict = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
active_config = config_dict.get(os.environ.get('FLASK_ENV', 'development'), DevelopmentConfig)

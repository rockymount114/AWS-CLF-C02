import os
class Config:
    SECRET_KEY = os.getenv('SECRET_KEY','dev-secret-key-change')
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL','sqlite:///quiz.db')
class DevConfig(Config):
    DEBUG=True
class ProdConfig(Config):
    DEBUG=False
config_by_name = {'dev': DevConfig, 'prod': ProdConfig}

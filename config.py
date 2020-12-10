import os

class Config:
    SECRET_KEY = "too hard to decypher string"

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DEV_DATABASE_URI") or \
        "mysql+pymysql://root:jplv123.YJ@localhost/something"

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get("PROD_DATABASE_URI") or \
        "mysql+pymysql://root:jplv123.YJ@localhost/practicing9"

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("TEST_DATABASE_URI") or \
        "mysql+pymysql://root:jplv123.YJ@localhost/practicing9-test"

config_name = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig
}
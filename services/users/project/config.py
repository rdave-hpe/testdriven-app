import os

class BaseConfig(object):
    "Base Configuration"
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True

class DevelopmentConfig(BaseConfig):
    "Development Configuration"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class TestingConfig(BaseConfig):
    "Test Configuration"
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_TEST_URL")

class ProductionConfig(BaseConfig):
    "Production Configuration"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") 

class BaseConfig(object):
    "Base Configuration"
    TESTING = False

class DevelopmentConfig(BaseConfig):
    "Development Configuration"
    pass

class TestingConfig(BaseConfig):
    "Test Configuration"
    TESTING = True

class ProductionConfig(BaseConfig):
    "Production Configuration"
    pass

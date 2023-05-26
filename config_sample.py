class Config:
    TESTING = False
    LOGGING_FILE_MAX_BYTES = 1024 * 1024
    LOGGING_FILE_BACKUP_COUNT = 10

    # get all keys and values of configuration
    def __str__(self):
        return "/".join([k+": "+v for k, v in vars(self.__class__).items() if not k.startswith('_')])

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///soma-production.db'
    LOGGING_FILENAME = 'production.log'

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///soma-development.db'
    LOGGING_FILENAME = 'development.log'

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///soma-testing.db' # TODO memory database
    LOGGING_FILENAME = 'testing.log'
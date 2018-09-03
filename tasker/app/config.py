import os
BASEDIR = os.path.abspath(os.path.dirname(__file__))
try:
    from .local_settings import *
except:
    pass

class Config:
    # DEBUG = False
    # TESTING = False
    # CSRF_ENABLED = True
    # SECRET_KEY = 'this-really-needs-to-be-changed'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLALCHEMY_DATABASE_URI = "postgresql:///flask_db"   # Enter your database name
    SQLALCHEMY_DATABASE_URI = f"postgresql://{DATABASE['POSTGRES_USER']}:{DATABASE['POSTGRES_PASSWORD']}@" \
                              f"{DATABASE['HOST']}:{DATABASE['PORT']}/{DATABASE['DB_NAME']}"
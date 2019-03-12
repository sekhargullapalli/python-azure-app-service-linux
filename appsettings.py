import os
approot = os.path.abspath(os.path.dirname(__file__))

class AppSettings(object):
    SECRET_KEY = '79283684-ee1d-4967-9182-1f0ae709a648'
    #ORM Configuration
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(approot,'countries.db')
    SQLALCHEMY_TRACK_MODIFICATIONS  = False
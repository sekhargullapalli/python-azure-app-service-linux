import os
approot = os.path.abspath(os.path.dirname(__file__))

class AppSettings(object):
    #ORM Configuration
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(approot,'countries.db')
    SQLALCHEMY_TRACK_MODIFICATIONS  = False
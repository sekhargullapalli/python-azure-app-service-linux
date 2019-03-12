from flask import Flask
from appsettings import AppSettings
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(AppSettings)
dbcontext = SQLAlchemy(app)
migrate = Migrate(app, dbcontext)
from app import routes
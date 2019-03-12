from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from app import routes
from appsettings import AppSettings

app = Flask(__name__)
app.config.from_object(AppSettings)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

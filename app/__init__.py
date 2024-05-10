from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_scss import Scss

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)
Scss(app)

from app import routes, models

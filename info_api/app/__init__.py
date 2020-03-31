from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database\\application.db"
db = SQLAlchemy(app)
api = Api(app)

from app.info.views import info
app.register_blueprint(info)

db.create_all()
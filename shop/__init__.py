from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
DB_NAME = "myshop.db"

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

from shop import routes
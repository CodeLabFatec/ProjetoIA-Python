from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
from env import Config
import os
from selected_env import selected_env
from env import Config


app = Flask(__name__)
CORS(app)
a = Config(config={'env': selected_env()}).config
app.config['SQLALCHEMY_DATABASE_URI'] = a.MYSQL_URL
db = SQLAlchemy(app)
app.app_context().push()
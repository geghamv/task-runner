from flask import Flask
from db import db
import logging
app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://localhost/gegham"
logging.basicConfig(level=logging.DEBUG)

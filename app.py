import os

from flask import Flask
from db import db
import logging
app = Flask(__name__)

uri = os.environ.get(
    'DATABASE_URL', 'postgresql://localhost/gegham')
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)
app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

logging.basicConfig(level=logging.DEBUG)

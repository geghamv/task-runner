import sys
import time
import random
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import DateTime
from sqlalchemy.sql import func
from db import db


class TaskModel(db.Model):
    __tablename__ = 'tasks'
    state = db.Column(db.String(80))
    name = db.Column(db.String(80), primary_key=True)
    done_by = db.Column(db.String(80))
    duration_seconds = db.Column(db.Integer)
    created_at = db.Column(DateTime(timezone=True),
                           server_default=func.now())
    updated_at = db.Column(DateTime(timezone=True),
                           server_default=func.now(), onupdate=func.now())

    def __init__(self, state, name, done_by, duration_seconds=None):
        self.state = state
        self.name = name
        self.done_by = done_by
        self.duration_seconds = duration_seconds

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_state(cls, state):
        return cls.query.filter_by(state=state).first()

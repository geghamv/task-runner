import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import DateTime
from db import db
import logging


class TaskModel(db.Model):
    __tablename__ = 'tasks'
    state = db.Column(db.String(80))
    name = db.Column(db.String(80), primary_key=True)
    done_by = db.Column(db.String(80))
    duration_seconds = db.Column(db.Integer)
    created_at = db.Column(DateTime(timezone=True),
                           default=datetime.datetime.utcnow)
    updated_at = db.Column(DateTime(
        timezone=True), default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    def __init__(self, state, name, done_by, duration_seconds=None):
        self.state = state
        self.name = name
        self.done_by = done_by
        self.duration_seconds = duration_seconds

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @ classmethod
    def find_by_state_with_update(cls, state, new_state, tr_name):
        task = cls.query.filter_by(state=state).order_by(
            TaskModel.created_at).limit(1).with_for_update().first()
        if task is None:
            return None
        task.state = new_state
        task.done_by = tr_name
        task.save_to_db()
        return task

from db import db
from task_model import TaskModel
from app import app

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
with app.app_context():
    db.init_app(app)
    db.drop_all()
    db.create_all()
    for letter in letters:
        TaskModel("QUEUED", "task_" + letter,).save_to_db()
    db.session.close()

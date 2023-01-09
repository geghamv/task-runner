from db import db
from task_model import TaskModel
from app import app

with app.app_context():
    db.init_app(app)
    db.drop_all()
    db.create_all()
    tsk1 = TaskModel("DONE", "task_A", "TR_1", 13)
    tsk2 = TaskModel("PENDING", "task_B", "TR_2")
    tsk3 = TaskModel("QUEUED", "task_D", None)
    tsk4 = TaskModel("QUEUED", "task_E", None)
    tsk1.save_to_db()
    tsk2.save_to_db()
    tsk3.save_to_db()
    tsk4.save_to_db()
    db.session.close()

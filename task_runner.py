from task_model import TaskModel
from run_task import run_task
import datetime
import logging
from app import app
from db import db


class TaskRunner:
    def __init__(self, name):
        self.name = name

    def get_with_lock(self):
        return TaskModel.find_by_state_with_update("QUEUED", "PENDING", self.name)

    def run(self, task, task_name):
        TaskRunner.print_time("started task {} ".format(task_name))
        _, duration_seconds = run_task(task_name)
        TaskRunner.print_time("finished task {} ".format(task_name))
        logging.info(f'duration seconds {duration_seconds}')
        task.state = "DONE"
        task.duration_seconds = duration_seconds
        task.save_to_db()

    @classmethod
    def print_time(cls, message):
        logging.info(message + str(datetime.datetime.utcnow()))

    @classmethod
    def task_runner(cls, name):
        tsr = TaskRunner(name)
        while True:
            task = tsr.get_with_lock()
            if task is None:
                break
            tsr.run(task, task.name)


with app.app_context():
    db.init_app(app)
    TaskRunner.task_runner("TR_1")

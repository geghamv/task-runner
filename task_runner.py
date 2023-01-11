from task_model import TaskModel
from run_task import run_task
import logging
from app import app
from db import db
import argparse


class TaskRunner:
    def __init__(self, name):
        self.name = name

    def get_with_lock(self):
        """ Picks first QUEUED task, locks the row,
         updates state and other column values, unlocks the row
        """
        return TaskModel.find_by_state_with_update("QUEUED", "PENDING", self.name)

    def run(self, task, task_name):
        """ Runs the task,
         updates column values,
         logs times
        """
        TaskRunner.print_time("started task", task.updated_at)
        _, duration_seconds = run_task(task_name)
        task.state = "DONE"
        task.duration_seconds = duration_seconds
        task.save_to_db()
        TaskRunner.print_time("finished task", task.updated_at)

    @classmethod
    def print_time(cls, message, time):
        logging.info(" ".join([message, str(time)]))

    @classmethod
    def task_runner(cls, name):
        """ Finds QUEUED tasks and processes them 
        until no QUEUED tasks are left
        """
        tsr = TaskRunner(name)
        while True:
            task = tsr.get_with_lock()
            if task is None:
                break
            tsr.run(task, task.name)


with app.app_context():
    db.init_app(app)
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", default="TR_1", required=False)
    args = parser.parse_args()
    TaskRunner.task_runner(args.name)

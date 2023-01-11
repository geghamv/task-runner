import time
import random


def run_task(task_name):
    duration_seconds = random.random() * 3
    time.sleep(duration_seconds)  # simulate heavy computation for ~20 seconds
    return task_name, duration_seconds

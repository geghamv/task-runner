# task-runner
Implemented task_runner that connects to the postgres DB and performs some tasks. 



## Description
create_tasks.py creates `tasks` table in postgresql DB in Heroku and populates it with 10 tasks in the state of "QUEUED" <br />
task_runner.py connects to the postgres DB and processes "QUEUED" tasks

## Dependencies
Flask, Flask-SQLALchemy, psycopg2

<!-- GETTING STARTED -->
## Getting Started
Connect to Heroku app task-runner by invitation email. <br />
Download Heroku Connect CLI.

If you want to create new `tasks` table with 10 tasks run

  ```sh
  heroku run python create_tasks.py --app task-runner
  ```
To create a task runner <name> and process the tasks run 
  ```sh
  heroku run python task_runner.py --name <name>  --app task-runner
  ```
Note if no name argument is specified the task runner's name will be "TR_1" by default. <br />

To create multiple task runners just run the command above in multiple terminals and provide uniquie names for each task runner

**_NOTE:_** All dates and times in database are in utc time zone.



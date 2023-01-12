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

To create multiple task runners just run the command above in multiple terminals and provide uniquie names for each task runner. <br />
  
To insert task manually in the `tasks` first run
  ```sh
  heroku pg:psql --app task-runner
  ```
Then run the following command with your desired values in the following format
  ```sh
   INSERT INTO tasks(state, name, done_by, duration_seconds, created_at, updated_at)  VALUES('QUEUED', 'task_Y',null ,null, 'December 12, 2022 2:02:13am','December 12, 2022 2:02:13am');
  ```
**_NOTE:_** All dates and times in database are in utc time zone.



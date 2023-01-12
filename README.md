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
**_NOTE:_** All dates and times in the database are in utc time zone.

## Examples
  
  <img width="663" alt="Screen Shot 2023-01-11 at 20 43 47" src="https://user-images.githubusercontent.com/60388824/212094873-a4f0e3bd-0157-4bea-8b42-838b5192acc0.png">
<img width="585" alt="Screen Shot 2023-01-12 at 18 32 22" src="https://user-images.githubusercontent.com/60388824/212094881-9ac56afb-6871-4fa9-b936-83d805cc1b68.png">
<img width="676" alt="Screen Shot 2023-01-12 at 18 33 29" src="https://user-images.githubusercontent.com/60388824/212094885-f5a0cf37-f999-4ac2-9276-6072ce2775bf.png">
<img width="668" alt="Screen Shot 2023-01-12 at 18 33 44" src="https://user-images.githubusercontent.com/60388824/212094887-5781284d-394b-4f2d-9af5-8a4668a12932.png">
<img width="694" alt="Screen Shot 2023-01-12 at 18 34 00" src="https://user-images.githubusercontent.com/60388824/212094894-f2feae37-de7e-4483-9c17-fb9eeff821a6.png">




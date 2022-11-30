# PROJECT: 0x0E. API
### AUTHOR: Matthew Allen

## TASKS:
### 0. Gather data from an API - `0-gather_data_from_an_API.py`
Python script that uses a REST API to return information about an employee's TODO list progress for a given employee ID.
* Uses `urllib` or `requests` module
* Accepts an integer employee ID as parameter
* Displays on standard output the employee TODO list progress in this exact format:
    * First line: `Employee EMPLOYEE_NAME is donw with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):`
        * `EMPLOYEE_NAME`: name of the employee
        * `NUMBER_OF_DONE_TASKS`: number of completed tasks
        * `TOTAL_NUMBER_OF_TASKS`: total number of tasks, which is the sum of completed and non-completed tasks
    * Second and N next lines display the title of completed tasks: `TASK_TITLE` (with 1 tabulation and 1 space before the `TASK_TITLE`).

### 1. Export to CSV - `1-export_to_CSV.py`
Python script to export data in the CSV format.
* Records all tasks that are owned by this employee
* Format is: `"USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"`
* File name is `USER_ID.csv`

### 2. Export to JSON - `2-export_to_JSON.py`
Python script to export data in JSON format.
* Records all tasks that are owned by this employee
* Format is: `{ "USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}`
* File name is `USER_ID.json`

### 3. Dictionary of list of dictionaries - `3-dictionary_of_list_of_dictionaries.py`
Python script to export data in JSON format
* Records all tasks from all employees
* Format is: `{ "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ], "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ]}`
* File name is `todo_all_employees.json`

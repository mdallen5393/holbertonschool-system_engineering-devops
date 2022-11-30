#!/usr/bin/python3
"""
Script that exports information about an employees TODO list progress
given an employee id to a CSV file named `USER_ID.csv`.
"""
import json
import requests


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/users/'
    user_response = requests.get(url)
    user_info = json.loads(user_response.text)

    # create dictionary containing users and their associated tasks
    tasks = {}
    for user in user_info:
        user_id = user['id']

        # create Response object for specific user and that user's tasks
        url = 'https://jsonplaceholder.typicode.com/todos/?userId={}'\
            .format(user_id)
        todo_response = requests.get(url)

        # create Dictionary objects from response objects
        todo_info = json.loads(todo_response.text)

        tasks_list = []
        for task in todo_info:
            # create a dictionary for each task
            task_dict = {}
            task_dict['username'] = user['username']
            task_dict['task'] = task['title']
            task_dict['completed'] = task['completed']
            # add task dictionary to the list of tasks
            tasks_list.append(task_dict)

        # add list of tasks to dictionary for that specific user
        tasks[user_id] = tasks_list

    # print json string to file; note: could have used dump to print
    # directly to file.
    with open('todo_all_employees.json', 'w', encoding='UTF8',
              newline='') as f:
        f.write(json.dumps(tasks))

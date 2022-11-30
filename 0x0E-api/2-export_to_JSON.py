#!/usr/bin/python3
"""
Script that exports information about an employees TODO list progress
given an employee id to a CSV file named `USER_ID.csv`.
"""
import json
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]

    # create Response object for specific user and that user's tasks
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    user_response = requests.get(url)

    url = 'https://jsonplaceholder.typicode.com/todos/?userId={}'\
        .format(user_id)
    todo_response = requests.get(url)

    # create Dictionary objects from response objects
    user_info = json.loads(user_response.text)
    todo_info = json.loads(todo_response.text)

    tasks = {}

    tasks_list = []
    for task in todo_info:
        # create a dictionary for each task
        task_dict = {}
        task_dict['task'] = task['title']
        task_dict['completed'] = task['completed']
        task_dict['username'] = user_info['username']
        # add task dictionary to the list of tasks
        tasks_list.append(task_dict)

    # add list of tasks to dictionary
    tasks[user_id] = tasks_list

    with open('./{}.json'.format(user_id), 'w', encoding='UTF8',
              newline='') as f:
        f.write(json.dumps(tasks))

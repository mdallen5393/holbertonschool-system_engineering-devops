#!/usr/bin/python3
"""
Script that returns information about an employees TODO list progress
given an employee id.
"""
import json
import requests
import sys

if __name__ == "__main__":
    num_done, num_tasks = 0, 0
    userId = sys.argv[1]

    # create Response object for specific user and that user's tasks
    user_response = requests.get('https://jsonplaceholder.typicode.com\
                                 /users/{}'.format(userId))
    todo_response = requests \
        .get('https://jsonplaceholder.typicode.com/todos/?userId={}'
             .format(userId))

    # create Dictionary objects from response objects
    user_info = json.loads(user_response.text)
    todo_info = json.loads(todo_response.text)
    print(type(user_info))
    print(type(todo_info))

    employee_name = user_info['name']

    for task in todo_info:
        num_tasks += 1
        if task['completed']:
            num_done += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, num_done, num_tasks))

    for task in todo_info:
        if task['completed']:
            print("\t {}".format(task['title']))

#!/usr/bin/python3
"""
Script that exports information about an employees TODO list progress
given an employee id to a CSV file named `USER_ID.csv`.
"""
import json
import requests
import sys
import csv


def writeCSV(list_to_write, id):
    """Writes a list of dictionaries to as CSV file."""
    fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
    with open('./{}.csv'.format(id), 'w', encoding='UTF8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames,
                                quoting=csv.QUOTE_ALL, quotechar='"')
        writer.writerows(list_to_write)


if __name__ == "__main__":
    num_done, num_tasks = 0, 0
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

    task_list = []
    username = user_info['name']
    for task in todo_info:
        task_dict = {}
        task_dict['USER_ID'] = user_id
        task_dict['USERNAME'] = username
        task_dict['TASK_COMPLETED_STATUS'] = task['completed']
        task_dict['TASK_TITLE'] = task['title']
        task_list.append(task_dict)

    writeCSV(task_list, user_id)

#!/usr/bin/python3
"""given eployee id returns user todo list info from API"""

import csv
import requests
from sys import argv


if __name__ == "__main__":

    id = argv[1]
    task_counter = 0
    all_tasks = []

    employee_request = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(id)).json()
    username = employee_request.get('username')
    task_request = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}/todos"
        .format(id)).json()
    for task in task_request:
        row = []
        row.append(id)
        row.append(username)
        row.append(task.get('completed'))
        row.append(task.get('title'))
        all_tasks.append(row)
    with open('{}.csv'.format(id), 'w') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        csv_writer.writerows(all_tasks)

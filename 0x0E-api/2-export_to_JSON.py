#!/usr/bin/python3
"""given eployee id exports todo list info in JSON from API"""

import json
import requests
from sys import argv


if __name__ == "__main__":

    id = argv[1]
    user_dict = {}

    employee_request = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(id)).json()
    username = employee_request.get('username')
    task_request = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}/todos"
        .format(id)).json()
    user_dict[id] = []
    for item in task_request:
        temp_dict = {}
        temp_dict['task'] = item.get('title')
        temp_dict['completed'] = item.get('completed')
        temp_dict['username'] = username
        user_dict[id].append(temp_dict)
    with open('{}.json'.format(id), 'w') as f:
        json.dump(user_dict, f)

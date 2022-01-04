#!/usr/bin/python3
"""given eployee id returns user todo list info from API"""


from sys import argv
import requests

if __name__ == "__main__":

    id = argv[1]
    task_counter = 0
    completed_tasks = []

    employee_request = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(id)).json()
    name = employee_request.get('name')
    task_request = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}/todos"
        .format(id)).json()
    for task in task_request:
        if task.get('completed') is True:
            task_counter += 1
            completed_tasks.append(task.get('title'))
    print('Employee {} is done with tasks({}/{}):'.format(name,
          task_counter, len(task_request)))
    for item in completed_tasks:
        print('\t {}'.format(item))

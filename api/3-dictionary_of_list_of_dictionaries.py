#!/usr/bin/python3

"""This module defines an API that saved data of a given employee"""

import json
import requests


if __name__ == '__main__':
    users_data = requests.get(
        'https://jsonplaceholder.typicode.com/users').json()

    employees_data = {}

    for user in users_data:
        user_todos = requests.get(
            'https://jsonplaceholder.typicode.com/user/{}/todos'.format(
                user['id']
            )).json()

        user_tasks = []
        for todo in user_todos:
            task_data = {}
            task_data['username'] = user['username']
            task_data['task'] = todo['title']
            task_data['completed'] = todo['completed']
            user_tasks.append(task_data)

        employees_data['{}'.format(user['id'])] = user_tasks

    with open('todo_all_employees.json', 'w') as f:
        json_data = json.dumps(employees_data)
        f.write(json_data)

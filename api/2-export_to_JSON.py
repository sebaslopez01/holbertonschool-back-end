#!/usr/bin/python3

"""This module defines an API that saved data of a given employee"""

import json
import requests
import sys


if __name__ == '__main__':
    user_id = int(sys.argv[1])
    user_data = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)).json()
    user_todos = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
            user_id
        )).json()

    with open('{}.json'.format(user_id), 'w') as f:
        tasks_lst = []
        for todo in user_todos:
            local_data = {}
            local_data['task'] = todo['title']
            local_data['completed'] = todo['completed']
            local_data['username'] = user_data['username']

            tasks_lst.append(local_data)
        json_data = json.dumps({'{}'.format(user_id): tasks_lst})
        f.write(json_data)

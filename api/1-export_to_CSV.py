#!/usr/bin/python3

"""This module defines an API that saved data of a given employee"""

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

    with open('{}.csv'.format(user_id), 'w') as f:
        for todo in user_todos:
            f.write('"{}","{}","{}","{}"\n'.format(
                user_id,
                user_data['username'],
                todo['completed'],
                todo['title']
            ))

#!/usr/bin/pytohon3

"""This module defines an API that returns data for a given employee"""

import requests
import sys


if __name__ == '__main__':
    user_id = int(sys.argv[1])
    user_data = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)).json()
    user_todos = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.format(user_id)).json()

    todos_completed = sum(1 for todo in user_todos if todo['completed'])

    print('Employee {} is done with tasks({}/{}):'.format(
        user_data['name'],
        todos_completed,
        len(user_todos)))

    for todo in user_todos:
        if todo['completed']:
            print('\t '+todo['title'])

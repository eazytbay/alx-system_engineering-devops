#!/usr/bin/python3
"""
This scirpt usesUsing https://jsonplaceholder.typicode.com
gathers data from API and exports it to JSON file
Implemented using recursion
"""
import json
import requests


API = "https://jsonplaceholder.typicode.com"
"""REST API url"""


if __name__ == '__main__':
    res_users = requests.get('{}/users'.format(API)).json()
    res_todos = requests.get('{}/todos'.format(API)).json()
    users_data = {}
    for user in users_res:
        id = user.get('id')
        user_name = user.get('username')
        pend = list(filter(lambda x: x.get('userId') == id, res_todos))
        user_data = list(map(
            lambda x: {
                'username': user_name,
                'task': x.get('title'),
                'completed': x.get('completed')
            },
            pends
        ))
        users_data['{}'.format(id)] = user_data
    with open('todo_all_employees.json', 'w') as file:
        json.dump(users_data, file)

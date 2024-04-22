#!/usr/bin/python3
"""
This is a script that returns to-do-list information for a given employee ID
"""
import re
import requests
import sys


API = "https://jsonplaceholder.typicode.com"
"""REST API url"""


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            id = int(sys.argv[1])
            res_user = requests.get('{}/users/{}'.format(API, id)).json()
            res_todos = requests.get('{}/todos'.format(API)).json()
            user_name = res_user.get('name')
            pend = list(filter(lambda x: x.get('userId') == id, res_todos))
            done_todos = list(filter(lambda x: x.get('completed'), pend))
            print(
                'Employee {} is done with tasks({}/{}):'.format(
                    user_name,
                    len(done_todos),
                    len(pend)
                )
            )
            for done_todo in done_todos:
                print('\t {}'.format(done_todo.get('title')))

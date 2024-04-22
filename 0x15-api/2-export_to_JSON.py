#!/usr/bin/python3
"""
Using https://jsonplaceholder.typicode.com
gathers data from API and exports it to JSON file
Implemented using recursion
"""
import json
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
            user_name = res_user.get('username')
            pends = list(filter(lambda x: x.get('userId') == id, res_todos))
            with open("{}.json".format(id), 'w') as json_file:
                user_data = list(map(
                    lambda x: {
                        "task": x.get("title"),
                        "completed": x.get("completed"),
                        "username": user_name
                    },
                    pends
                ))
                user_data = {
                    "{}".format(id): user_data
                }
                json.dump(user_data, json_file)

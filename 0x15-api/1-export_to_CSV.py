#!/usr/bin/python3
"""
This script Uses https://jsonplaceholder.typicode.com
to gather data from API and exports it to CSV file
This is Implemented using recursion
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
            user_name = res_user.get('username')
            pends = list(filter(lambda x: x.get('userId') == id, res_todos))
            with open('{}.csv'.format(id), 'w') as file:
                for pend in pends:
                    file.write(
                        '"{}","{}","{}","{}"\n'.format(
                            id,
                            user_name,
                            pend.get('completed'),
                            pend.get('title')
                        )
                    )

#!/usr/bin/python3
"""
This scirpt uses https://jsonplaceholder.typicode.com
and gathers data from API and exports it to JSON file
Implemented using recursion
"""
import json
import requests
import sys


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/users"

    resp = requests.get(url)
    users = response.json()

    dictionary = {}
    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
        url = url + '/todos/'
        resp = requests.get(url)
        tsks = resp.json()
        dictionary[user_id] = []
        for tsk in tsks:
            dictionary[user_id].append({
                "task": tsk.get('title'),
                "completed": tsk.get('completed'),
                "username": username
            })
    with open('todo_all_employees.json', 'w') as file:
        json.dump(dictionary, file)

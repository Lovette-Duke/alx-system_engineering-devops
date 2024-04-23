#!/usr/bin/python3
"""script to get API for todo lists of all employees"""

import json
import sys
from urllib import request, parse

if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/users"

    with request.urlopen(url) as response:
        Users = json.loads(response.read().decode('utf-8'))

    users_dict = {}
    for user in Users:
        USER_ID = user.get('id')
        USERNAME = user.get('username')
        user_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'
        user_url = user_url.format(USER_ID)

        with request.urlopen(user_url) as response:
            tasks = json.loads(response.read().decode('utf-8'))

        users_dict[USER_ID] = []
        for task in tasks:
            TASK_COMPLETED_STATUS = task.get('completed')
            TASK_TITLE = task.get('title')
            users_dict[USER_ID].append({
                "task": TASK_TITLE,
                "completed": TASK_COMPLETED_STATUS,
                "username": USERNAME
            })

    with open('todo_all_employees.json', 'w') as f:
        json.dump(users_dict, f)

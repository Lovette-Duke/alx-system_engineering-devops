#!/usr/bin/python3
"""exports to-do list info for an employee ID to JSON format."""
import json
import sys
from urllib import request, parse

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user_url = url + "users/{}".format(user_id)
    todos_url = url + "todos"

    with request.urlopen(user_url) as response:
        user_data = json.loads(response.read().decode('utf-8'))
        username = user_data.get("username")

    with request.urlopen(todos_url + "?userId=" + user_id) as response:
        todos_data = json.loads(response.read().decode('utf-8'))

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump({user_id: [{
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": username
            } for todo in todos_data]}, jsonfile)

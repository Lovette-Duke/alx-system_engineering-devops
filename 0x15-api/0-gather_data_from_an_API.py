#!/usr/bin/python3
"""returns info on the to-do list for a given employee ID."""
import json
import sys
from urllib import request, parse

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user_url = url + "users/{}".format(employee_id)
    todos_url = url + "todos"

    with request.urlopen(user_url) as response:
        user_data = json.loads(response.read().decode('utf-8'))

    with request.urlopen(todos_url + "?userId=" + employee_id) as response:
        todos_data = json.loads(response.read().decode('utf-8'))

    completed_tasks = [todo['title'] for todo in todos_data if todo['completed']]
    num_completed_tasks = len(completed_tasks)
    total_tasks = len(todos_data)
    employee_name = user_data['name']

    print("Employee {} is done with tasks({}/{}):".format(employee_name, num_completed_tasks, total_tasks))
    for task in completed_tasks:
        print("\t {}".format(task))

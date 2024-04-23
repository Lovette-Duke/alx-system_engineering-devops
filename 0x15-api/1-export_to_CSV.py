#!/usr/bin/python3
"""exports to-do list information for an employee ID to CSV format."""
import csv
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

    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for todo in todos_data:
            writer.writerow([user_id, username,
                            todo.get("completed"), todo.get("title")])

#!/usr/bin/python3
"""
This module provide todo_progress function to display a specific
user completed list
"""

import requests
import sys


def todo_progress():
    if len(sys.argv) != 2:
        return
    id = sys.argv[1]
    space = "\u2003"
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"/users/{id}"
    user_response = requests.get(base_url + user_url)

    if user_response.status_code == 200:
        user = user_response.json()
    else:
        return 'Error fetching data: {}'.format(user_response.status_code)

    todo_url = f"/todos?userId={id}"
    todo_response = requests.get(base_url + todo_url)

    if todo_response.status_code == 200:
        todos = todo_response.json()
    else:
        return 'Error fetching data: {}'.format(user_response.status_code)

    completed_tasks = [todo["title"] for todo in todos if todo["completed"]]
    task_per = f"{len(completed_tasks)}/{len(todos)}"
    user_text = f"Employee {user['name']} is done with tasks({task_per}):"
    print(user_text)

    for task in completed_tasks:
        print('\t',task)


if __name__ == "__main__":
    todo_progress()

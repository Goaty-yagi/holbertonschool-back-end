#!/usr/bin/python3
"""
This module provide export_json function to write
json formatted user task data.
"""

import sys
import requests
import json


def export_json():
    if len(sys.argv) != 2:
        return
    id = sys.argv[1]
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

    file_name = f"{id}.json"
    with open(file_name, 'w') as file:
        lines = [{
            'task': todo["title"], 'completed': todo["completed"], 'username': user["username"]
        } for todo in todos]
        data = {id: lines}
        json.dump(data, file)


if __name__ == "__main__":
    export_json()

#!/usr/bin/python3
"""
This module provide export_all_todo function to write
all json formatted user task data.
"""
import json
import requests


def export_all_todo():
    base_url = "https://jsonplaceholder.typicode.com"

    todo_url = f"/todos"
    todo_response = requests.get(base_url + todo_url)

    if todo_response.status_code == 200:
        all_todos = todo_response.json()
    else:
        return 'Error fetching data: {}'.format(todo_response.status_code)

    with open("todo_all_employees.json", 'w') as file:
        sorted_todos = sorted(all_todos, key=lambda x: x['userId'])
        init_id = sorted_todos[0]['id']
        user_url = f"/users/{init_id}"
        user_response = requests.get(base_url + user_url)
        if user_response.status_code == 200:
            user = user_response.json()
        else:
            return 'Error fetching data: {}'.format(user_response.status_code)

        each_list = []
        store = {}
        for todo in sorted_todos:
            if init_id != todo['userId']:
                store[init_id] = each_list
                each_list = []
                init_id = todo['userId']
                user_url = f"/users/{init_id}"
                user_response = requests.get(base_url + user_url)
                if user_response.status_code == 200:
                    user = user_response.json()
                else:
                    return 'Error fetching data: {}'.format(user_response.status_code)
            each_list.append({
                'username': user["username"], 'task': todo["title"], 'completed': todo["completed"]
            })

        each_list.append({
            'username': user["username"], 'task': todo["title"], 'completed': todo["completed"]
        })
        store[init_id] = each_list
        json.dump(store, file)


if __name__ == "__main__":
    export_all_todo()

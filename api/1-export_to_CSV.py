#!/usr/bin/python3
"""
This module provide export_csv function to write
csv formatted user task data.
"""
import requests
import sys


def export_csv():
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

    file_name = f"{id}.csv"
    with open(file_name, 'w') as file:
        for todo in todos:
            id_str = f'"{id}"'
            name_str = f'"{user["username"]}"'
            completed_str = f'"{todo["completed"]}"'
            title_str = f'"{todo["title"]}"'

            line = f"{id_str},{name_str},{completed_str},{title_str}\n"
            file.write(line)


if __name__ == "__main__":
    export_csv()

import sys
import requests


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
    print(
        f"Employee{space}{user['name']}{space}is{space}done{space}with{space}tasks{space}({len(completed_tasks)}/{len(todos)})")

    for task in completed_tasks:
        print('\t ', end='')
        print(task.replace(" ", space))


if __name__ == "__main__":
    todo_progress()

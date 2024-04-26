
#!/usr/bin/python3
"""Python script to export data in the json format."""
import json
import requests
import sys


def fetch_todo_list_progress(employee_id):
    """
    extend your Python script to export data in the json format
    """
    todos = requests.get(
        f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    ).json()
    user = requests.get(
        f"https://jsonplaceholder.\
typicode.com/users/{employee_id}"
    ).json()
    data = {

        employee_id: [
            {
                "username": user["username"],
                "task": task["title"],
                "completed": task["completed"],
            }
            for task in todos
        ]
    }
    with open(f"{employee_id}.json", "w") as jsonfile:
        json.dump(data, jsonfile)


if __name__ == "__main__":
    employee_id = sys.argv[1]
    fetch_todo_list_progress(employee_id)

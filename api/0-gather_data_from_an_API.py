#!/usr/bin/python3
"""Python script that, using this REST API,
for a given employee ID, returns information
about his/her TODO list progress."""

import requests
import sys


def fetch_todo_list_progress(employee_id):
    """
    Fetches the TODO list progress for a given employee ID.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
    todos = requests.get(
        f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
        ).json()
    user_info = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{employee_id}"
        ).json()
    completed_tasks = [task["title"] for task in todos if task["completed"]]
    a = len(completed_tasks)
    b = len(todos)
    print(
        f"Employee {user_info['name']} is done with tasks ({a}/{b}):")
    for task in completed_tasks:
        print("\t{}".format(task))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    fetch_todo_list_progress(employee_id)

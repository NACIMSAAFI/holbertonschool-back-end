#!/usr/bin/python3
"""Python script to export data in the json format."""

import json
import requests


def fetch_all_todo_lists():
    """
    Records all tasks for all employees.

    Returns:
        None
    """
    todos = requests.get(f"https://jsonplaceholder.typicode.com/todos").json()
    users = requests.get(
        f"https://jsonplaceholder.\
typicode.com/users"
    ).json()

    data = {
        user["id"]: [
            {
                "username": user["username"],
                "task": task["title"],
                "completed": task["completed"],
            }
            for task in todos
            if task["userId"] == user["id"]
        ]
        for user in users
    }

    with open(f"todo_all_employees.json", "w") as jsonfile:
        json.dump(data, jsonfile)


if __name__ == "__main__":
    fetch_all_todo_lists()

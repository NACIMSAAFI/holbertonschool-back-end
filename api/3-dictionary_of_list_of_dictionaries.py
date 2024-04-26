#!/usr/bin/python3
"""Python script to export data in the json format."""

import requests
import json


def fetch_all_todo_lists():
    """
    Records all tasks for all employees.

    Returns:
        None
    """
    # Base URL for the fake REST API
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch user information for all users
    users_url = f"{base_url}/users"
    users_response = requests.get(users_url)
    users_data = users_response.json()

    # Construct JSON data
    json_data = {}

    # Fetch TODO list for each user
    for user in users_data:
        employee_id = user["id"]
        employee_name = user["name"]
        todos_url = f"{base_url}/todos?userId={employee_id}"
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()

        # Construct JSON data for this employee
        json_data[str(employee_id)] = [
            {
                "username": employee_name,
                "completed": todo["completed"],
                "task": todo["title"],
            }
            for todo in todos_data
        ]

    # Write JSON data to file
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(json_data, jsonfile)


if __name__ == "__main__":
    # Call function to fetch and record all tasks
    fetch_all_todo_lists()

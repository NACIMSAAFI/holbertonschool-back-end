#!/usr/bin/python3
"""Python script to export data in the json format."""

import requests
import sys
import json


def fetch_todo_list_progress(employee_id):
    """
    Records all tasks that are owned by this employee.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
    # Base URL for the fake REST API
    base_url = "https://jsonplaceholder.typicode.com"

    # URL to fetch user information
    user_url = f"{base_url}/users/{employee_id}"
    # URL to fetch TODO list for the user
    todos_url = f"{base_url}/todos?userId={employee_id}"

    # Fetch user information
    user_response = requests.get(user_url)
    user_data = user_response.json()
    # Extract employee name from user data
    employee_name = user_data.get("name")

    # Fetch TODO list for the user
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Construct JSON data
    json_data = {
        employee_id: [
            {
                "username": employee_name,
                "completed": todo["completed"],
                "task": todo["title"],
            }
            for todo in todos_data
        ]
    }
    # Write JSON data to file
    with open(f"{employee_id}.json", "w") as jsonfile:
        json.dump(json_data, jsonfile)


if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    # Extract employee ID from command line argument
    employee_id = sys.argv[1]
    try:
        employee_id = int(employee_id)
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    # Call function to fetch and display TODO list progress
    fetch_todo_list_progress(employee_id)

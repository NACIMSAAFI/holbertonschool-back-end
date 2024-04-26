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

    # Calculate progress
    tasks = len(todos_data)
    # Count number of completed tasks
    task = sum(True for todo in todos_data if todo["completed"])

    # Display progress
    print(f"Employee {employee_name} is done with tasks ({task}/{tasks}):")
    # Display titles of completed tasks
    for todo in todos_data:
        if todo["completed"]:
            print(f"\t{todo['title']}")


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

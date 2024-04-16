#!/usr/bin/python3
import requests
import sys


def fetch_todo_list_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    # Fetch user information
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data.get("name")

    # Fetch todo list
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Calculate progress
    tasks = len(todos_data)
    task = sum(1 for todo in todos_data if todo["completed"])

    # Display progress
    print(f"Employee {employee_name} is done with tasks({task}/{tasks}):")
    for todo in todos_data:
        if todo["completed"]:
            print(f"\t{todo['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    try:
        employee_id = int(employee_id)
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    fetch_todo_list_progress(employee_id)

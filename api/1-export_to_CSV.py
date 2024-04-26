#!/usr/bin/python3
"""
This script will use the REST API to return information
about a given employee's TODO list progress.
"""
import csv
import requests
import sys


def fetch_todo_list_progress(employee_id):
    """
    extend your Python script to export data in the CSV format
    """
    todos = requests.get(
        f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    ).json()
    user_info = requests.get(
        f"https://jsonplaceholder.\
typicode.com/users/{employee_id}"
    ).json()
    with open(f"{employee_id}.csv", mode="w") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow(
                [(employee_id), user_info["username"],
                 todo["completed"], todo["title"]]
            )


if __name__ == "__main__":
    employee_id = sys.argv[1]
    fetch_todo_list_progress(employee_id):

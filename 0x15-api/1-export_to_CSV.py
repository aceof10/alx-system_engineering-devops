#!/usr/bin/python3

"""
    exports data in the CSV format
"""
import csv
import requests
import sys


def get_employee_todo_progress(emp_id):
    employee_url = f"https://jsonplaceholder.typicode.com/users/{emp_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={emp_id}"

    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()

    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    username = employee_data.get("username")

    csv_filename = f"{emp_id}.csv"
    with open(csv_filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todos_data:
            csv_writer.writerow([
                    emp_id, username, task.get("completed"), task.get("title")
                ])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
    else:
        try:
            emp_id = int(sys.argv[1])
            get_employee_todo_progress(emp_id)
        except ValueError:
            print("Please provide a valid integer as employee_id")

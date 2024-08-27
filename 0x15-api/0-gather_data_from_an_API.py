#!/usr/bin/python3

"""
    returns information about an employee's TODO list progress
    given their employee ID
"""
import requests
import sys


def get_employee_todo_progress(emp_id):
    employee_url = f"https://jsonplaceholder.typicode.com/users/{emp_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={emp_id}"

    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()

    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    name = employee_data.get("name")

    total_tasks = len(todos_data)
    done_tasks = [task for task in todos_data if task.get("completed")]
    ndone_tasks = len(done_tasks)

    print(f"Employee {name} is done with tasks({ndone_tasks}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
    else:
        try:
            emp_id = int(sys.argv[1])
            get_employee_todo_progress(emp_id)
        except ValueError:
            print("Please provide a valid integer as employee_id")

#!/usr/bin/python3

"""
    exports data in the JSON format
"""
import json
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

    tasks_list = []
    for task in todos_data:
        tasks_list.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        })

    json_data = {str(emp_id): tasks_list}

    json_filename = f"{emp_id}.json"
    with open(json_filename, mode='w') as json_file:
        json.dump(json_data, json_file)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
    else:
        try:
            emp_id = int(sys.argv[1])
            get_employee_todo_progress(emp_id)
        except ValueError:
            print("Please provide a valid integer as employee_id")

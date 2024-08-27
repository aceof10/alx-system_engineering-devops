#!/usr/bin/python3

"""
    exports data in the JSON format
"""
import json
import requests


def get_all_employees_todo_progress():
    employees_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    employees_response = requests.get(employees_url)
    employees_data = employees_response.json()

    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    todos_by_user = {}
    for employee in employees_data:
        user_id = employee.get("id")
        username = employee.get("username")
        todos_by_user[user_id] = []
        for task in todos_data:
            if task.get("userId") == user_id:
                todos_by_user[user_id].append({
                    "username": username,
                    "task": task.get("title"),
                    "completed": task.get("completed")
                })

    json_filename = "todo_all_employees.json"
    with open(json_filename, mode='w') as json_file:
        json.dump(todos_by_user, json_file)


if __name__ == "__main__":
    get_all_employees_todo_progress()

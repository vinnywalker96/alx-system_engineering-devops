#!/usr/bin/python3
"""import libraries"""
import json
import requests


def get_all_task():
    """Retrieves all employees task"""
    base_url = 'https://jsonplaceholder.typicode.com'
    response = requests.get(f'{base_url}/users')
    users = response.json()
    res = requests.get(f"{base_url}/todos")
    todos = res.json()
    filename = 'todo_all_employees.json'
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump({user.get('id'): [{"username": user.get("username"),
                  "task": todo.get("title"),
                  "completed": todo.get("completed")
                  } for todo in todos]
                  for user in users}, f)


if __name__ == "__main__":
    get_all_task()

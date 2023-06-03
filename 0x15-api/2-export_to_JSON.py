#!/usr/bin/python3
"""import modules"""
import json
import requests
import sys


def export_to_json(employee_id):
    """exports to json format"""
    base_url = 'https://jsonplaceholder.typicode.com'
    response = requests.get(f'{base_url}/users/{employee_id}')
    data = response.json()
    employee_name = data['name']
    res = requests.get(f'{base_url}/todos?userId={employee_id}')
    todos = res.json()
    employee_task = []
    filename = f'{employee_id}.json'
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump({employee_id: [{
                  "task": todo.get("title"),
                  "completed": todo.get("competed"),
                  "username": employee_name
                  }
                  for todo in todos]}, f)


if __name__ == "__main__":
    export_to_json(sys.argv[1])

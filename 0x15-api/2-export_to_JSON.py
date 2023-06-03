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
    for todo in todos:
        if str(todo['userId']) == employee_id:
            task = {
                "task": todo['title'],
                "completed": todo['completed'],
                "username": employee_name
            }
            employee_task.append(task)
    data = {
        employee_id: employee_task
    }

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f)
    return data


if __name__ == "__main__":
    export_to_json(sys.argv[1])

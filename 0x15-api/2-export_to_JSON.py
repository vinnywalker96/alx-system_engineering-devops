#!/usr/bin/python3

import requests
import sys
import json


def export_to_json(employee_id):
    """exports to json format"""
    base_url = 'https://jsonplaceholder.typicode.com'
    try:
        #get employee information
        reponse = requests.get(f'{base_url}/users{employee_id}')
        employee_data = response.json()
        employee_name = employee_data['name']
        todo = requests.get(f'{base_url}/todos?userId={employee_id}')
        todo_data = todo_response.json()
        task = {}
        filename = ""
        for todo in todo_data:
            if str(todo['userId']) == employee_id:
                task['userId'] = [{
                    "task": todo['title'],
                    "completed": todo['completed'],
                    "username": employee_name}]
                filename = f"{todo['userId']}.json"
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dumb(task,f) 


if __name__ == "__main__":
    export_to_json(sys.argv[1])

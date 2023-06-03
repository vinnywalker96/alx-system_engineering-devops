#!/usr/bin/python3
"""import libraries"""
import csv
import requests
import sys


def export_employee_todo_to_csv(employee_id):
    """Export to csv"""
    # Fetch employee details
    employee_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    response = requests.get(employee_url)
    employee_data = response.json()
    employee_username = employee_data['username']

    # Fetch employee's TODO list
    url = 'https://jsonplaceholder.typicode.com'
    base_url = f'{url}/todos?userId={employee_id}'
    response = requests.get(base_url)
    todos = response.json()
    # Export data to CSV
    filename = f'{employee_id}.csv'
    with open(filename, 'w', encoding='utf-8', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for todo in todos:
            if str(todo['userId']) == employee_id:
                data = [
                    str(todo['userId']),
                    employee_username,
                    str(todo['completed']),
                    todo['title']
                ]
                
            writer.writerow(data)


if __name__ == "__main__":
    export_employee_todo_to_csv(sys.argv[1])

#!/usr/bin/python3
import requests
import csv

def export_employee_todo_to_csv(employee_id):
    # Fetch employee details
    employee_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    response = requests.get(employee_url)
    employee_data = response.json()
    employee_username = employee_data['username']

    # Fetch employee's TODO list
    todos_url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    response = requests.get(todos_url)
    todos = response.json()

    # Export data to CSV
    filename = f'{employee_id}.csv'
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for todo in todos:
            user_id = todo['userId']
            task_completed = todo['completed']
            task_title = todo['title']
            writer.writerow(user_id, employee_username, task_completed, task_title])

    print(f"Data exported to {filename} successfully.")


# Example usage
employee_id = 2  # Enter the employee ID here
export_employee_todo_to_csv(employee_id)


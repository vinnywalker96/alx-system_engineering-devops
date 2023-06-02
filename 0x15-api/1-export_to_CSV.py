#!/usr/bin/python3
import requests
import csv
import sys


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
    with open(filename, 'w', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for todo in todos:
            data = "{},{},{},{}".format(todo['userId'],
                employee_username, todo['completed'],
                    todo['title'])
            writer.writerow(data)

    print(f"Data exported to {filename} successfully.")


# Example usage
if __name__ == "__main__":
    export_employee_todo_to_csv(sys.argv[1])

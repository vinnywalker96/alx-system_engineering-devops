#!/usr/bin/python3
import requests
import sys


def get_employee_todo_progress(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com'

    # Retrieve employee information
    employee_response = requests.get(f'{base_url}/users/{employee_id}')
    employee_data = employee_response.json()
    employee_name = employee_data['name']

    # Retrieve employee's TODO list
    todo_response = requests.get(f'{base_url}/todos?userId={employee_id}')
    todo_data = todo_response.json()

    # Count the number of completed tasks
    completed_tasks = [task for task in todo_data if task['completed']]
    number_of_done_tasks = len(completed_tasks)
    total_number_of_tasks = len(todo_data)

    # Display employee TODO list progress
    print(f"Employee {employee_name} is done\
           with tasks({number_of_done_tasks}/{total_number_of_tasks}):")
    print(f"\t{employee_name}: {number_of_done_tasks}\
            completed tasks out of {total_number_of_tasks}")

    # Display the titles of completed tasks
    print("Completed tasks:")
    for task in completed_tasks:
        print(f"\t\t{task['title']}")


# Example usage: get TODO list progress for employee with ID 1
get_employee_todo_progress(sys.argv[1])

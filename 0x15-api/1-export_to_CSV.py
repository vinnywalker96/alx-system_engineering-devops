#!/usr/bin/python3
"""Import libraries"""
import requests
import sys


def get_employee_todo_progress(employee_id):
    """returns employee todo
    Args:
        employee_id (int)
    """
    base_url = 'https://jsonplaceholder.typicode.com'

    # Retrieve employee information
    employee_response = requests.get(f'{base_url}/users/{employee_id}')
    employee_data = employee_response.json()
    EMPLOYEE_NAME = employee_data['name']

    # Retrieve employee's TODO list
    todo_response = requests.get(f'{base_url}/todos?userId={employee_id}')
    todo_data = todo_response.json()

    # Count the number of completed tasks
    completed_tasks = [task for task in todo_data if task['completed']]
    NUMBER_OF_DONE_TASKS = len(completed_tasks)
    TOTAL_NUMBER_OF_TASKS = len(todo_data)

    # Display employee TODO list progress
    print("Employee {} is done with tasks({}/{}):".
          format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS,
                 TOTAL_NUMBER_OF_TASKS))
    for task in completed_tasks:
        print("\t {}".format(task['title']))


# Example usage: get TODO list progress for employee with ID 1
if __name__ == "__main__":
    get_employee_todo_progress(sys.argv[1])

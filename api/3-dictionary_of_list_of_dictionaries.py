#!/usr/bin/python3
""" Using the REST API jsonplaceholder """
import json
import requests
import sys


BASE_URL = "https://jsonplaceholder.typicode.com"
USERS_URL = BASE_URL + "/users/"
TODOS_URL = BASE_URL + "/todos"


def get_employee_data():
    """Retrieve employee data."""
    response = requests.get(USERS_URL)
    if response.status_code != 200:
        print(
            f"Error fetching employee data: \
            {response.status_code} {response.text}"
        )
        sys.exit(1)
    return response.json()


def get_tasks_data(user_id):
    """Retrieve tasks data."""
    response = requests.get(TODOS_URL, params={"userId": user_id})
    if response.status_code != 200:
        print(
            f"Error fetching task data: \
            {response.status_code} {response.text}"
        )
        sys.exit(1)
    return response.json()


def get_list_task(tasks_data, name_employee, id_employee):
    """make lists with data"""
    list_task = []
    for dict in tasks_data:  # liste de dictionnaires
        new_dict = {
            "username": name_employee,
            "task": dict["title"],
            "completed": dict["completed"],
        }
        list_task.append(new_dict)

    concat_filename = str(id_employee) + ".json"
    return list_task


def list_to_json(total_dict, filename):
    """list to json file"""
    with open('todo_all_employees.json', "w") as json_file:
        json.dump(total_dict, json_file)


def main():
    if len(sys.argv) > 2:
        print("Usage: script_name employee_id")
        sys.exit(1)


employees = get_employee_data()
json_dict = {}
for employee in employees:
    user_id = employee['id']
    name_employee = employee['name']
    task_data = get_tasks_data(user_id)
    list_task = get_list_task(task_data, name_employee, user_id)
    json_dict[user_id] = list_task
list_to_json(json_dict, 'todo_all_employees.json')

if __name__ == "__main__":
    main()

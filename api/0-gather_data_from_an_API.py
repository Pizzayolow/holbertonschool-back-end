#!/usr/bin/python3
"""Requests some data with API and return infos"""
import requests
import sys

# Requests some data with API
if __name__ == "__main__":
    # Get the name of the employee by ID
    employee_id = {'id': sys.argv[1]}
    response = requests.get(
        'https://jsonplaceholder.typicode.com/users/', params=employee_id)
    data = response.json()
    dict_d = data[0]  # Create a dictionary to extract the name

    # Get the tasks
    user_id = {'userId': sys.argv[1]}
    tasks = requests.get(
        'https://jsonplaceholder.typicode.com/todos', params=user_id)
    dt_tk = tasks.json()

    # Create a counter to know the number of completed tasks
    ct = 0
    list_task_completed = []
    for element in dt_tk:
        if element['completed'] is True:
            list_task_completed.append((element["title"]))
            ct += 1

    # Print final output and format the prompt
    print(
        f"Employee {dict_d['name']} is done with tasks({ct}/{len(dt_tk)}):")
    for element in list_task_completed:
        print("\t" + ' ' + element)

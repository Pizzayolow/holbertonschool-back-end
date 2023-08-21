#!/usr/bin/python3

import requests
import sys
from collections import Counter

"""get the name of the employee by id"""
employee_id = {'id': sys.argv[1]}
response = requests.get(
    'https://jsonplaceholder.typicode.com/users/', params=employee_id)
"""converti le get en format json"""
data = response.json()
"""créer un dictionnaire afin de pouvoir extraire le nom"""
dict_d = data[0]

"""get the task"""
user_id = {'userId': sys.argv[1]}
tasks = requests.get(
    'https://jsonplaceholder.typicode.com/todos', params=user_id)
data_task = tasks.json()
"""créer un compteur afin de connaitre le nombre de task accomplies"""
count = 0
list_task_completed = []
for element in data_task:
    if element['completed'] is True:
        list_task_completed.append((element["title"]))
        count += 1
"""print final et mise en forme du prompt"""
print(
    f"Employee {dict_d['name']} is done with tasks({count}/{len(data_task)}):")
for element in list_task_completed:
    print("\t" + ' ' + element)

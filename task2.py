"""task2.py"""

import json
import requests

def create_json_file():
    url = 'https://jsonplaceholder.typicode.com/todos/'
    response = requests.get(url)
    data = response.json()
    with open('todos.json', 'w') as f:
        json.dump(data, f, indent=4)

def split_json_to_files():
    with open('todos.json', 'r') as f:
        todos = json.load(f)
    for i, todo in enumerate(todos):
        with open(f'todo_{i}.json', 'w') as f:
            json.dump(todo, f, indent=4)

if __name__ == "__main__":
    create_json_file()
    split_json_to_files()

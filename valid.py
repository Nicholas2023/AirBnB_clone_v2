#!/usr/bin/python3

import json

file_path = 'file.json'

try:
    with open(file_path, 'r') as file:
        json_data = json.load(file)
    print("JSON is valid.")
except json.JSONDecodeError as e:
    print(f"JSON is invalid. Error: {e}")

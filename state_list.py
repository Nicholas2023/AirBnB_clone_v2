#!/usr/bin/python3
"""
populate the file.json file using the MySQL dump data you provided,
"""
import mysql.connector
import json
from models.city import City
from models.state import State

# Connect to your MySQL server (adjust the connection settings)
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Nick1996',
    database='hbnb_dev_db'
)

# Create a cursor
cursor = conn.cursor()

# Execute the SQL statements in the MySQL dump
with open('7-dump.sql', 'r') as sql_file:
    sql_commands = sql_file.read().split(';')

for command in sql_commands:
    cursor.execute(command)

# Fetch data from the 'cities' and 'states' tables
cursor.execute("SELECT * FROM cities")
cities_data = cursor.fetchall()

cursor.execute("SELECT * FROM states")
states_data = cursor.fetchall()

# Close the cursor and database connection
cursor.close()
conn.close()

# Create Python objects and populate __objects dictionary
for city_data in cities_data:
    city = City(**{
        'id': city_data[0],
        'created_at': city_data[1],
        'updated_at': city_data[2],
        'name': city_data[3],
        'state_id': city_data[4]
    })
    key = f"City.{city.id}"
    storage.__objects[key] = city

for state_data in states_data:
    state = State(**{
        'id': state_data[0],
        'created_at': state_data[1],
        'updated_at': state_data[2],
        'name': state_data[3]
    })
    key = f"State.{state.id}"
    storage.__objects[key] = state

# Save the __objects dictionary to file.json
storage.save()

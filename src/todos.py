"""
To-Do Project
"""

import json
import os
from uuid import uuid4

from utils.logger import logger


# Generate the unique ID for the task.
def generate_id():
    """
    Generate a unique ID for the task.
    """
    return uuid4().hex


# Then fetch the hardcoded data from the file.
TODO_FILE = "data/todo.json"


# Function to Load JSON List
def load_list():
    """
    Load the list of todos from a JSON file.
    """
    if not os.path.exists(TODO_FILE):
        logger.warning("File %s not found. Returning an empty list", TODO_FILE)
        return []

    try:
        with open(TODO_FILE, "r", encoding="UTF-8") as file:
            json_data = json.load(file)
            logger.info("JSON loaded from %s", TODO_FILE)
            return json_data  # returns the list of json tasks
    except json.JSONDecodeError as jde:
        logger.error("JSON Decode Error: %s", jde)
        return []
    except (OSError, IOError) as e:
        logger.error("Unexpected error while loading: %s", e)
        return []


# Function to Save the current list of JSON back to JSON File
def save_list(todo_list):
    """
    Save the list of todos back to a JSON file.
    """
    try:
        with open(DATA_FILE, "w", encoding="UTF-8") as file:
            json.dump(todo_list, file, indent=4)
        logging.info("JSON saved to %s", DATA_FILE)
    except (OSError, IOError) as e:
        logging.error("Unexpected error while saving: %s", e)
        return []


# Function to append data to existing JSON File.


def append_list():
    """
    Append the new list of todo to a JSON list.
    """
    new_todo = {
        "title": "New Todo Item",
        "description": "This is a new todo item that is added to the list.",
        "doneStatus": False,
        "id": generate_id(),
    }

    print("Trying to Add new todo:", new_todo)

    todos = load_list()

    # Check if new todo already exists in todos list.
    # If it already exists, do not add it again.
    # If it does not exist, add it to the list.
    found = False
    for todo in todos:
        if todo["title"] == new_todo["title"]:
            found = True
            break
    
    if not found:
        todos.append(new_todo)

        with open(DATA_FILE, "w", encoding="UTF-8") as file_write:
            json.dump(todos, file_write, indent=4)
        print("New Todo Item Added to the List.")
    else:
        print("Todo Item already exists in the List.")


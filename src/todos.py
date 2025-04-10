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
TODO_FILE = "../data/todos.json"


# Function to Load JSON List
def load_list(file_path=TODO_FILE):
    """
    Load the list of todos from a JSON file.
    """
    if not os.path.exists(file_path):
        logger.warning("File %s not found. Returning an empty list", file_path)
        return []

    try:
        with open(file_path, "r", encoding="UTF-8") as file:
            json_data = json.load(file)
            logger.info("JSON loaded from %s", file_path)
            return json_data  # returns the list of json tasks
    except json.JSONDecodeError as jde:
        logger.error("JSON Decode Error: %s", jde)
        return []
    except (OSError, IOError) as e:
        logger.error("Unexpected error while loading: %s", e)
        return []



# Function to get to do details by its unique ID
def get_todo_details_by_id(todo_id,file_path=TODO_FILE):
    """
    Get the todo details by its unique ID.

    Args:
        todo_id (str): The unique ID of the todo.
        file_path (str): The path to the JSON file.

    Returns:
        dict: The todo details if found, otherwise None.
    
    Raises:
        FileNotFoundError: If the JSON file does not exist.
        json.JSONDecodeError: If the JSON file is not valid.
    """
    todos_list = load_list(file_path)
    for todo in todos_list:
        if todo["id"] == todo_id:
            logger.info("Todo found with ID %s", todo_id)
            return todo
    logger.warning("Todo with ID %s not found", todo_id)
    # If the todo is not found, return None
    # return None
    # or raise an exception.
    raise ValueError(f"Todo with ID {todo_id} not found.")

    
if __name__ == "__main__":
    # Load the list of todos from the JSON file and print to console.
    todos = load_list()
    print("Running todos.py")
    print(todos)

    # Try fetching a todo by ID
    try:
        TODO_ID = "1101adb6fb8642209a5ab8cdb17b2231"  # Change this to an actual ID from your JSON file
        todo = get_todo_details_by_id(TODO_ID)
        print(f"Todo found:\nTitle: {todo['title']}\nDescription: {todo['description']}")
    except ValueError as e:
        print(f"{e}")

"""
To-Do Project
"""

import json
import logging
import os


# First write the setup of logging function.

def setup_logging():
    """
    Setup Logging
    """
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(levelname)s  - %(message)s",
        # asctime = ASCII Time.
        handlers=[
            logging.FileHandler("logging/app.log"),
            logging.StreamHandler()
        ]
    )

# Call the logging function
setup_logging()



# Then fetch the hardcoded data from the file.
DATA_FILE = "data/todos.json"


# Function to Load JSON List
def load_list():
    """
    Load the list of todos from a JSON file.
    """
    if not os.path.exists(DATA_FILE):
        logging.warning("File %s not found. Returning an empty list", DATA_FILE)
        return []

    try:
        with open(DATA_FILE, "r", encoding="UTF-8") as file:
            json_tasks = json.load(file)
            logging.info("JSON loaded from %s", DATA_FILE)
            # print(json_tasks)
            # print(type(json_tasks))  #The JSON from file is stored in json_tasks as a list.
            return json_tasks  # returns the list of json tasks
    except json.JSONDecodeError as jde:
        logging.error("JSON Decode Error: %s",jde)
        return []
    except (OSError,IOError) as e:
        logging.error("Unexpected error while loading: %s", e)
        return []
        

# Function to Save the current list of JSON back to JSON File
def save_list(todo_list):
    """
    Save the list of todos back to a JSON file.
    """
    try:
        with(open(DATA_FILE, "w", encoding="UTF-8")) as file:
            json.dump(todo_list, file, indent=4)
        logging.info("JSON saved to %s", DATA_FILE)
    except (OSError, IOError) as e:
        logging.error("Unexpected error while saving: %s", e)
        return []

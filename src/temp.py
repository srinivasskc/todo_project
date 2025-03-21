"""
To-Do Project
"""

import uuid
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

DATA_FILE = "data/todo.json"


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
            # print(json_tasks)
            # print(type(json_tasks))  #The JSON from file is stored in json_tasks as a list.
            return json_tasks  # returns the list of json tasks
    except json.JSONDecodeError as jde:
        logging.error("JSON Decode Error: %s",jde)
        return []
    except (OSError,IOError) as e:
        logging.error("Unexpected error while loading: %s", e)
        return []

print("Returning the Json from file: \n", load_list())


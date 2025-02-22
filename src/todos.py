"""
To-Do Project
"""

import uuid
import json


DATA_FILE = "data/todos.json"


# Function to Load JSON List
def load_list():
    """
    Load the list of todos from a JSON file.
    """
    with open(DATA_FILE, "r", encoding="UTF-8") as file:
        json_tasks = json.load(file)
        # print(json_tasks)
        # print(type(json_tasks))  #The JSON from file is stored in json_tasks as a list.
        return json_tasks  # returns the list of json tasks


print("Returning the Json from file: \n", load_list())


##########################################################################################################


# Function to Generate Unique IDs
def generate_unique_todo_id():
    """
    Generate Unique ID using UUID
    """
    return uuid.uuid4().hex


# Function to Save JSON List Back
def save_list(todo_list):
    """Save the current list of todos back to the JSON file"""
    with open(DATA_FILE, "w", encoding="UTF-8") as file:
        json.dump(todo_list, file, indent=4)
        print("Todos saved successfully.")


# Function to Append New Todo
def append_new_todo():
    """
    Append a new todo only if it doesn't already exist
    """
    todos = load_list()
    print("\n Print the data in todos: \n", todos)

    # Generate a new todo dictionary
    new_todo = {
        "id": generate_unique_todo_id(),
        "title": "This is new title",
        "description": "Step 1 of Becoming Technical Tester",
        "doneStatus": True,
    }

    # Check if the new todo already exists (based on title)
    for todo in todos:
        if todo["title"] == "This is new title":
            print("Todo already exists. Do not add duplicates.")
            return

    todos.append(new_todo)
    print("\n New Todo Added - current New Todo list: \n", todos)
    save_list(todos)

append_new_todo()

####################################################################################################


# Function to Retrieve Todo by ID
def get_todo_details(todo_id):
    """
    Retrieve details for a specific todo based on a unique identifier
    """
    with open(DATA_FILE, "r", encoding="UTF-8") as file:
        json_tasks = json.load(file) 
    
    for todo in json_tasks:
        if todo["id"] == todo_id:
            return todo  
        
    print("Todo not found.")
    return None  # Return None if not found

# Example: Retrieve a todo by its ID
TODO_ID_TO_SEARCH = "338b8e7cc41c4173bdd3b9564b348003"
todo_details = get_todo_details(TODO_ID_TO_SEARCH)

if todo_details:
    print("ToDo Found: \n", todo_details)
else:
    print(f"ToDo with ID {TODO_ID_TO_SEARCH} is not found")

"""
To-Do Project
"""

import uuid
import json


# Function to Generate Unique IDs
def generate_unique_todo_id():
    """
    Generate Unique ID using UUID
    """
    return uuid.uuid4().hex


DATA_FILE = "data/todos.json"


# Function to Load JSON List
def load_list():
    """
    Load the list of todos from a JSON file.
    """
    with open(DATA_FILE, "r", encoding="UTF-8") as file:
        json_tasks = json.load(file)
        print(json_tasks)
        print(type(json_tasks))  #The JSON from file is stored in json_tasks as a list.
        return json_tasks  # returns the list of json tasks


print(load_list())


# Function to Save JSON List Back
def save_list(json_tasks):
    """
    Save the current list of todos back to the JSON file
    """
    # dump(from,to,indentation)
    with open(DATA_FILE, "w", encoding="UTF-8") as file:
        json.dump(json_tasks, file, indent=4)
    print("ToDo's saved Successfully")


# Function to Append New Todo
def append_new_todo(title, status=True):
    """
    Append a new todo only if it doesn't already exist
    """
    todos = load_list()

    # Generate a new todo dictionary
    new_todo = {
        "id": generate_unique_todo_id(),
        "title": title,
        "description": "Step 1 of Becoming Technical Tester",
        "doneStatus": status
    }

    # Check if the new todo already exists (based on title)
    for todo in todos:
        if todo["title"] == title:
            print("Todo already exists. Not adding duplicate.")
            return
    
    todos.append(new_todo)
    save_list(todos)
    print("New Todo Added: ", new_todo)


# Function to Retrieve Todo by ID
def get_todo_details(todo_id):
    """
    Retrieve details for a specific todo based on a unique identifier
    """
    todos = load_list()
    print("All Todos: ", todos)
    print("\n")

    for todo in todos:
        if todo["id"] == todo_id:
            return todo  # Return the matching todo

    print("Todo not found.")
    return None  # Return None if not found

# Run the function to add a new todo
append_new_todo("Generate UUID from a function again")

# Example: Retrieve a todo by its ID
TODO_ID_TO_SEARCH = "7f9047b5faf247b2907b99827dca568c"
todo_details = get_todo_details(TODO_ID_TO_SEARCH)

if todo_details:
    print("ToDo Found", todo_details)
else:
    print(f"ToDo with ID {TODO_ID_TO_SEARCH} is not found")

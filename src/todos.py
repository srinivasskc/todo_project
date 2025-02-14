"""
To-Do Project
"""

import uuid
import json

# Generate Unique IDs for To Do List.

def generate_unique_todo_id():
    """
    Generate Unique ID using UUID
    """
    return uuid.uuid4().hex

new_todo = {
        "title": "Generate UUID from a function again",
        "Status": True
            }


new_todo["id"] = generate_unique_todo_id()
print("New Todo: ",new_todo)

DATA_FILE = "data/todos.json"

print("\nNow - Print Load List Function \n")


def load_list():
    """
    Load the list of todos from a JSON file.
    """
    with open(DATA_FILE,"r",encoding="UTF-8") as file:
        json_tasks = json.load(file)
        return json_tasks

print(load_list())



print("\nNow - Get Todo Details Function \n")

def get_todo_details(todo_id):
    """
     Retrieve details for a specific todo based on a unique identifier 
    """
    todos = load_list()
    print("All Todos: ",todos)
    print("\n")

    for todo in todos:
        if todo["id"] == todo_id:
            return todo

print(get_todo_details("7f9047b5faf247b2907b99827dca568c"))


print("\n")

print("Appending the new json task back to json list")

def append_json_task_to_json():
    """
    Appending the New JSON Task to JSON 
    """
    with open(DATA_FILE,"r",encoding="UTF-8") as file: 
        json_tasks = json.load(file)
        json_tasks.append(new_todo)
        print(json_tasks)
        #print(type(json_tasks))

append_json_task_to_json()   


print("\n")

# Writing back to JSON File with write mode.
def write_back_to_json_file():
    """
    Writing back to JSON File with write mode.
    """
    with open(DATA_FILE,"r",encoding="UTF-8") as file:
        json_tasks = json.load(file)
        print(json_tasks)
    
    json_tasks.append(new_todo)
    print(json_tasks)
    
    # dump(from,to,indentation)
    with open(DATA_FILE,"w",encoding="UTF-8") as file_write:
        json.dump(json_tasks,file_write,indent=4)
        print("Appended Successfully")

write_back_to_json_file()


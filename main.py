from src.todos import (load_list, save_list)

print(load_list())

todos = load_list()
todos.append({
    "id": "123",
    "title": "Manual Add",
    "description": "Added directly in main.py",
    "doneStatus": False
})
save_list(todos)

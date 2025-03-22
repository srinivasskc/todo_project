from src.todos import (load_list, append_list)

# 1. Load and print current todos
print("---Current Todos---")
todos = load_list()
for todo in todos:
    print("\n")
    print(todo)

# 2. Append a new todo to the list
print("\n--- Appending a New Todo ---")
print("\n")
append_list()

# 3. Load and print updated todos
print("\n--- Updated Todos ---")
updated_todos = load_list()
for todo in updated_todos:
    print(todo)
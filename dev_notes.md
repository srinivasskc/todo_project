## 2025-03-21
- Reviewed TODO_PROJECT and todos.py
- I have written till now:
    - setup_logging(): This creates a log file - app.log
    - Once setup_logging() function is created, it is called.
    - Data File is created: data/todos.json
- I have added main.py and imported the todos.py and called the load_list() function.
- Tested load_list() from main.py
    - If the todos.json file is not available,  WARNING  - File data/todos.json not found. Returning an empty list is displayed.
    - If the todos.json file is empty,  ERROR  - JSON Decode Error: Expecting value: line 1 column 1 (char 0) is displayed
    - If the todos.json fie has json but missing comma in json, ERROR  - JSON Decode Error: Expecting ',' delimiter: line 5 column 9 (char 70) is displayed 
    - If the todos.json file is having [] empty json, [] is returned.
- Next Task::: save_list(todo_list)

## 2025-03-22
- Worked on save_list(todo_list)
    - This will first open the DATA_FILE with write access
    - we will be using JSON.dump() to add data from todo_list to DATA_FILE
- In the main.py, we load the existing data to todos variable.
    - Then appended the json list (manually)
    - Finally saving the list with Todos.
- Next Tasks:: Problem == Whenever I run the main.py, same json list is appended multiple times to todos.json.

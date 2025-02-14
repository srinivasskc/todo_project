
## Installation

Step 1: Create a Github Repository.

Step 2: Open Visual Studio -> Terminal and follow the steps from Github Repository

Step 3: Create a New Git Branch

```bash
cd /path/to/todo_project
git checkout -b feature/todo-management
```

Step 4: Set Up a Virtual Environment
```bash
python -m venv venv
```    


Step 4: Activate the Virtual Environment
```bash
venv\Scripts\activate
```    

Step 5: Verify the Virtual Environment is Active
```bash
where python
```    

Step 6: Create a requirements.in File
```bash
echo > requirements.in
```    

Step 7: Open the requirements.in file and add below python packages:
```bash
uuid
```    

Step 8: 
Install and Freeze Dependencies Install all dependencies and generate a requirements.txt file:

```bash
pip install -r requirements.in
pip freeze > requirements.txt
```    

Step 9: 
Initialize a data/ Folder for JSON Storage

```bash
mkdir data
create a file:  data/todos.json
echo "[]" > data/todos.json
```    

Step 10: Add files to version control and commit:

```bash
git add .
git commit -m "Setup virtual environment, requirements, and JSON storage"
git push origin feature/todo-management
```    







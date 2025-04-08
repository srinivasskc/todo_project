# ✅ Todo Management System – 7-Day Progress Checklist

Track your daily goals and progress here. Check `[x]` when complete!

---

## 📅 Day 1 – Project Setup & `load_list`

- [X] Set up project folder structure  
- [X] Create `todos.json` file in `data/` or let app create it
- [X] Implement `load_list()` with logging and error handling
- [x] Set up logging in `utils/logger.py`
- [x] Write unit tests for `load_list()`:
  - [x] File missing
  - [x] Valid JSON file
  - [x] Invalid JSON file

---

## 📅 Day 2 – `get_todo_details(todo_id)`

- [ ] Implement `get_todo_details(todo_id)`
- [ ] Add error handling and logging
- [ ] Write unit tests:
  - [ ] Todo exists
  - [ ] Todo does not exist (raises 404)

---

## 📅 Day 3 – `save_list(todo_list)`

- [ ] Implement `save_list(todo_list)`
- [ ] Add error handling for file write issues
- [ ] Write unit tests:
  - [ ] Save valid list
  - [ ] Simulate permission/path errors

---

## 📅 Day 4 – `remove_todo(todo_id)`

- [ ] Implement `remove_todo(todo_id)`
- [ ] Add logging and 404 error if ID not found
- [ ] Write unit tests:
  - [ ] Remove existing todo
  - [ ] Try removing non-existent todo

---

## 📅 Day 5 – `update_todo(todo_id, todo)` & `generate_id()`

- [ ] Implement `generate_id()` using UUID
- [ ] Implement `update_todo()` (supports partial update)
- [ ] Add error handling and logging
- [ ] Write unit tests:
  - [ ] Update existing todo
  - [ ] Try updating non-existent todo
  - [ ] Update with partial fields only

---

## 📅 Day 6 – Testing & Logging Review

- [ ] Ensure 100% test coverage for all functions
- [ ] Check logging for all:
  - [ ] Success
  - [ ] Warnings
  - [ ] Errors
- [ ] Review edge cases:
  - [ ] Empty list
  - [ ] Malformed JSON
  - [ ] File permission errors

---

## 📅 Day 7 – Cleanup & Final Polish

- [ ] Finalize `main.py` (run and test all functions)
- [ ] Add clear docstrings for all functions
- [ ] Clean up code and folder structure
- [ ] Backup project (e.g., zip or push to GitHub)
- [ ] Celebrate your progress 🎉

---

📝 _Tip: You can copy this into a GitHub issue, your README, or a `progress.md` file in your project root._

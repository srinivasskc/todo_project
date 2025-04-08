# Unit Tests using Python Testing Library - unittest

import unittest
import os
import json
from src.todos import load_list,generate_id, TODO_FILE


class TestLoadList(unittest.TestCase):
    def setUp(self):
        os.makedirs("data",exist_ok=True)
        # This is to make sure "data" directory exists

    
    def tearDown(self):
        if os.path.exists(TODO_FILE):
            os.remove(TODO_FILE)
        # This is to remove the file after test run.
    
    

    def test_file_missing_returns_empty(self):
        """
        To simulate when the file is missing
        and check if the function returns an empty list.
        """
        if os.path.exists(TODO_FILE):
            os.remove(TODO_FILE)
        result = load_list()
        self.assertEqual(result, [])

    
    def test_valid_json_returns_data(self):
        """
        This is to validate json data and check if the function returns the data.
        """
        sample_data = [
            {
                "title": "Sample Todo",
                "description": "This is a sample todo item.",
                "doneStatus": False,
                "id": generate_id(),
            }
        ]

        with open(TODO_FILE, "w", encoding="UTF-8") as file:
            json.dump(sample_data, file)
        result = load_list()
        self.assertEqual(result, sample_data)


    def test_invalid_json_logs_error(self):
        """
        This is to validate invalid json data and check if the function returns an empty list.
        """
        with open(TODO_FILE, "w", encoding="UTF-8") as file:
            file.write("Invalid JSON")
        result = load_list()
        self.assertEqual(result, [])

"""
file_io.py
----------
Reading and writing text, CSV, and JSON files.
"""
import json

def file_io_examples():
    # Text file
    with open('sample.txt', 'w') as f:
        f.write('Hello, file!')
    with open('sample.txt', 'r') as f:
        text = f.read()
    # JSON
    data = {'a': 1, 'b': 2}
    with open('sample.json', 'w') as f:
        json.dump(data, f)
    with open('sample.json', 'r') as f:
        data_loaded = json.load(f)
    return text, data_loaded

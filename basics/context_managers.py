"""
context_managers.py
------------------
Using and creating context managers (with statement, contextlib).
"""
from contextlib import contextmanager

def file_context_example():
    with open('sample.txt', 'w') as f:
        f.write('context manager!')
    with open('sample.txt', 'r') as f:
        return f.read()

@contextmanager
def custom_context():
    print('Enter')
    yield 'inside'
    print('Exit')

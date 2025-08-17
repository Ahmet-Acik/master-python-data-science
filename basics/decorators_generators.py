"""
decorators_generators.py
-----------------------
Writing and using decorators, generator functions, and expressions.
"""

def simple_decorator(func):
    def wrapper(*args, **kwargs):
        print('Before call')
        result = func(*args, **kwargs)
        print('After call')
        return result
    return wrapper

@simple_decorator
def greet(name):
    return f"Hello, {name}!"

def generator_example():
    for i in range(3):
        yield i

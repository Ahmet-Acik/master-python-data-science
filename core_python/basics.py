"""
basics.py
---------
Comprehensive core Python: variables, data types, control flow, functions, comprehensions, lambda/functional tools, exception handling, file I/O, modules, decorators/generators, type annotations, context managers, regex, datetime, argparse. (OOP is in a separate file.)

This module follows best practices, uses real-world and data science examples, and is designed for clarity and practical learning.
"""

# =========================
# VARIABLES & ASSIGNMENT
# =========================
# Variables store data. Python is dynamically typed.
age = 29  # int
height_m = 1.75  # float
name = "Ahmet"  # str
is_student = False  # bool

# Multiple assignment (unpacking)
latitude, longitude = 41.0082, 28.9784  # Istanbul coordinates

# Swapping values
x, y = 5, 10
x, y = y, x

# =========================
# DATA TYPES & DATA STRUCTURES
# =========================
# Numbers
price = 19.99
quantity = 3
total = price * quantity

# Strings
city = "Istanbul"
greeting = f"Hello, {name} from {city}!"
upper_city = city.upper()

# Lists (ordered, mutable)
temperatures = [22.1, 23.4, 21.8, 20.0]
temperatures.append(19.5)
avg_temp = sum(temperatures) / len(temperatures)

# Tuples (ordered, immutable)
rgb = (255, 0, 128)
date = (2025, 8, 18)

# Dictionaries (key-value, mutable)
person = {"name": name, "age": age, "city": city}
person["job"] = "Data Scientist"
for key, value in person.items():
	pass  # iterate over key-value pairs

# Sets (unique, unordered)
skills = {"python", "sql", "pandas", "python"}
skills.add("numpy")

# NoneType
optional_value = None

# Most-used built-in functions
max_temp = max(temperatures)
min_temp = min(temperatures)
unique_skills = list(set(skills))
rounded_price = round(price)
enumerated = list(enumerate(temperatures))
zipped = list(zip(temperatures, range(len(temperatures))))

# =========================
# DATA TYPES
# =========================
# Built-in types: int, float, str, bool, list, tuple, dict, set, NoneType

# Numbers
integer = 42
floating = 2.718
complex_num = 2 + 3j
list_comp = [x**2 for x in range(5)]
dict_comp = {x: x**2 for x in range(5)}
set_comp = {x % 2 for x in range(5)}

# =========================
# LAMBDA & FUNCTIONAL TOOLS
# =========================
nums = [1, 2, 3, 4]
squares = list(map(lambda x: x**2, nums))
evens = list(filter(lambda x: x % 2 == 0, nums))
from functools import reduce
product = reduce(lambda x, y: x * y, nums)
pairs = list(zip(nums, squares))

# =========================
# EXCEPTION HANDLING
# =========================
def safe_divide(a, b):
	try:
		return a / b
	except ZeroDivisionError:
		return 'Cannot divide by zero'
	finally:
		pass

class CustomError(Exception):
	pass

# =========================
# FILE I/O
# =========================
def write_and_read_file():
	with open('sample.txt', 'w') as f:
		f.write('Hello, file!')
	with open('sample.txt', 'r') as f:
		return f.read()

# =========================
# MODULES & PACKAGES
# =========================
import math
from math import sqrt
pi_val = math.pi
sqrt_16 = sqrt(16)

# =========================
# DECORATORS & GENERATORS
# =========================
def simple_decorator(func):
	def wrapper(*args, **kwargs):
		print('Before call')
		result = func(*args, **kwargs)
		print('After call')
		return result
	return wrapper

@simple_decorator
def decorated_greet(name):
	return f"Hi, {name}!"

def generator_example():
	for i in range(3):
		yield i

# =========================
# TYPE ANNOTATIONS
# =========================
def add_typed(a: int, b: int) -> int:
	return a + b
x_typed: float = 3.14
y_typed: str = 'hello'

# =========================
# CONTEXT MANAGERS
# =========================
from contextlib import contextmanager
@contextmanager
def custom_context():
	print('Enter')
	yield 'inside'
	print('Exit')

# =========================
# REGULAR EXPRESSIONS
# =========================
import re
def regex_examples():
	text = 'Data science 2025!'
	numbers = re.findall(r'\d+', text)
	words = re.findall(r'\w+', text)
	replaced = re.sub(r'\d+', 'YEAR', text)
	return numbers, words, replaced

# =========================
# DATETIME
# =========================
from datetime import datetime, timedelta
def datetime_examples():
	now = datetime.now()
	future = now + timedelta(days=7)
	formatted = now.strftime('%Y-%m-%d')
	return now, future, formatted

# =========================
# ARGPARSE
# =========================
import argparse
def argparse_example():
	parser = argparse.ArgumentParser(description='Example')
	parser.add_argument('--x', type=int, default=1)
	args = parser.parse_args([])  # Empty list for demo
	return args.x

# Strings
single = 'single quotes'
double = "double quotes"
multiline = """multi\nline\nstring"""

# Boolean
flag = False

# Lists (mutable, ordered)
fruits = ['apple', 'banana', 'cherry']
fruits.append('date')

# Tuples (immutable, ordered)
point = (3, 4)

# Dictionaries (mutable, key-value pairs)
person = {'name': 'Alice', 'age': 30}
person['city'] = 'London'

# Sets (mutable, unique, unordered)
unique_numbers = {1, 2, 3, 2}

# NoneType
nothing = None

# Type checking
def type_examples():
	return type(integer), type(floating), type(str_var), type(fruits), type(person), type(unique_numbers), type(nothing)

# =========================
# CONTROL FLOW
# =========================
# if, elif, else
def sign_of_number(x):
	if x > 0:
		return "Positive"
	elif x < 0:
		return "Negative"
	else:
		return "Zero"

# for loop
def sum_list(lst):
	total = 0
	for item in lst:
		total += item
	return total

# while loop
def countdown(n):
	result = []
	while n > 0:
		result.append(n)
		n -= 1
	return result

# break and continue
def first_even(nums):
	for n in nums:
		if n % 2 == 0:
			return n
	return None

# =========================
# FUNCTIONS
# =========================
# Function definition, arguments, return, docstrings
def greet(name):
	"""Return a greeting string."""
	return f"Hello, {name}!"

def add(a, b=0):
	"""Return the sum of a and b (default 0)."""
	return a + b

# Arbitrary arguments
def sum_all(*args):
	return sum(args)

# Keyword arguments
def print_info(**kwargs):
	return ', '.join(f"{k}={v}" for k, v in kwargs.items())

# Lambda (anonymous) functions
square = lambda x: x * x

# Nested functions
def outer(x):
	def inner(y):
		return x + y
	return inner

# Example usage (for demonstration, not executed on import)
if __name__ == "__main__":
	print("Type examples:", type_examples())
	print("Sign of -5:", sign_of_number(-5))
	print("Sum of [1,2,3]:", sum_list([1,2,3]))
	print("Countdown from 3:", countdown(3))
	print("First even in [1,3,5,8]:", first_even([1,3,5,8]))
	print(greet("Bob"))
	print("Add 2+3:", add(2,3))
	print("Sum all 1,2,3:", sum_all(1,2,3))
	print("Print info:", print_info(name="Alice", age=30))
	print("Square of 4:", square(4))
	print("Outer/Inner:", outer(10)(5))



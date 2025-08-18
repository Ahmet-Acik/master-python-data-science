"""
basics.py
---------
Comprehensive, real-world introduction to core Python for data science, scripting, and professional development.
- Variables, data types, control flow, functions, comprehensions, functional programming, exception handling, file I/O, modules, decorators/generators, type annotations, context managers, regex, datetime, argparse, and more. (OOP is in a separate file.)
- Beginners to intermediate Python users, especially those preparing for data science, analytics, or automation roles.
- Best practices, type hints, practical comments, and real-world/data science examples.
- Each section is clearly explained and grouped for quick reference.
- Example usage at the end demonstrates real scenarios.
basics.py
Comprehensive, real-world introduction to core Python for data science, scripting, and professional development.

Scope:
	- Variables, data types, control flow, functions, comprehensions, functional programming, exception handling, file I/O, modules, decorators/generators, type annotations, context managers, regex, datetime, argparse, and more. (OOP is in a separate file.)

Audience:
	- Beginners to intermediate Python users, especially those preparing for data science, analytics, or automation roles.

Features:
	- Best practices, type hints, practical comments, and real-world/data science examples.
	- Each section is clearly explained and grouped for quick reference.
	- Example usage at the end demonstrates real scenarios.
"""
"""

**Features:**
- Best practices, type hints, practical comments, and real-world/data science examples.
- Each section is clearly explained and grouped for quick reference.
- Example usage at the end demonstrates real scenarios.
"""


"""- Each section is clearly explained and grouped for quick reference.
- Example usage at the end demonstrates real scenarios.
"""

# Type hints for advanced return types
from typing import Generator, Callable

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
# COMPREHENSIONS (Best Practice for Data Transformation)
# =========================
# List comprehension
temp_c = [round((f-32)*5/9, 1) for f in [68, 70, 72, 66]]  # Fahrenheit to Celsius
# Dict comprehension
fruit_lengths = {fruit: len(fruit) for fruit in ["apple", "banana", "cherry"]}
# Set comprehension
unique_first_letters = {fruit[0] for fruit in ["apple", "banana", "cherry", "avocado"]}

# =========================
# LOOPS (for, while, enumerate, zip)
# =========================
for idx, temp in enumerate(temperatures):
	pass  # idx is index, temp is value

for t, day in zip(temperatures, ["Mon", "Tue", "Wed", "Thu", "Fri"]):
	pass  # t is temperature, day is day name

# While loop example
def find_below_threshold(temps: list[float], threshold: float) -> float | None:
	"""
Return the first temperature below the threshold.
Useful for early stopping in data scans.
	"""
	i = 0
	while i < len(temps):
		if temps[i] < threshold:
			return temps[i]
		i += 1
	return None

# =========================
# STRING METHODS (Most Used)
# =========================
sentence = "  Python is awesome!  "
clean = sentence.strip()
words = clean.split()
joined = "-".join(words)
replaced = clean.replace("awesome", "powerful")
is_title = clean.istitle()
upper = clean.upper()
lower = clean.lower()

# =========================
# LIST METHODS (Most Used)
# =========================
nums = [3, 1, 4, 1, 5, 9]
nums.sort()
nums.reverse()
nums.append(2)
nums.remove(1)  # removes first occurrence
count_1 = nums.count(1)
index_4 = nums.index(4) if 4 in nums else -1

# =========================
# FUNCTIONAL PROGRAMMING (map, filter, reduce, any, all)
# =========================
evens = list(filter(lambda x: x % 2 == 0, nums))
squared = list(map(lambda x: x**2, nums))
from functools import reduce
product = reduce(lambda x, y: x * y, nums)
all_positive = all(x > 0 for x in nums)
any_even = any(x % 2 == 0 for x in nums)

# =========================
# FIX str_var ERROR IN type_examples
# =========================
def type_examples_fixed():
	example_str = "example"
	return type(integer), type(floating), type(example_str), type(fruits), type(person), type(unique_numbers), type(nothing)

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
def safe_divide(a: float, b: float) -> float | str:
	"""
Divide a by b, handling division by zero.
Returns a string if division by zero occurs.
	"""
	try:
		return a / b
	except ZeroDivisionError:
		return 'Cannot divide by zero'
	finally:
		pass

class CustomError(Exception):
	"""Custom exception for demonstration purposes."""
	pass

# =========================
# FILE I/O
# =========================
def write_and_read_file() -> str:
	"""
Write a string to a file and read it back.
Demonstrates basic file I/O for logs, configs, etc.
	"""
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
	"""
Print messages before and after calling the decorated function.
Use for logging, timing, etc.
	"""
	def wrapper(*args, **kwargs):
		print('Before call')
		result = func(*args, **kwargs)
		print('After call')
		return result
	return wrapper

@simple_decorator
def decorated_greet(name: str) -> str:
	"""Return a decorated greeting string."""
	return f"Hi, {name}!"

def generator_example() -> Generator[int, None, None]:
	"""
Yield numbers 0, 1, 2. Use for streaming data, pipelines, etc.
	"""
	for i in range(3):
		yield i

# =========================
# TYPE ANNOTATIONS
# =========================
def add_typed(a: int, b: int) -> int:
	"""Add two integers with type hints."""
	return a + b
x_typed: float = 3.14
y_typed: str = 'hello'

# =========================
# CONTEXT MANAGERS
# =========================
from contextlib import contextmanager
@contextmanager
def custom_context():
	"""
Example context manager for resource management.
Use for DB connections, files, etc.
	"""
	print('Enter')
	yield 'inside'
	print('Exit')

# =========================
# REGULAR EXPRESSIONS
# =========================
import re
def regex_examples() -> tuple[list[str], list[str], str]:
	"""
Find numbers and words in a string, and replace numbers with 'YEAR'.
Useful for data cleaning and extraction.
	"""
	text = 'Data science 2025!'
	numbers = re.findall(r'\d+', text)
	words = re.findall(r'\w+', text)
	replaced = re.sub(r'\d+', 'YEAR', text)
	return numbers, words, replaced

# =========================
# DATETIME
# =========================
from datetime import datetime, timedelta
def datetime_examples() -> tuple[datetime, datetime, str]:
	"""
Return current datetime, a week later, and formatted string.
Useful for time series, scheduling, etc.
	"""
	now = datetime.now()
	future = now + timedelta(days=7)
	formatted = now.strftime('%Y-%m-%d')
	return now, future, formatted

# =========================
# ARGPARSE
# =========================
import argparse
def argparse_example() -> int:
	"""
Parse a command-line argument (demo only).
Use for building CLI tools and scripts.
	"""
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
def type_examples() -> tuple[type, ...]:
	"""
Return types of various example variables.
Useful for introspection and debugging.
	"""
	str_var = "example"
	return type(integer), type(floating), type(str_var), type(fruits), type(person), type(unique_numbers), type(nothing)

# =========================
# CONTROL FLOW
# =========================
# if, elif, else
def sign_of_number(x: float) -> str:
	"""
Return whether a number is positive, negative, or zero.
Useful for data validation and feature engineering.
	"""
	if x > 0:
		return "Positive"
	elif x < 0:
		return "Negative"
	else:
		return "Zero"

# for loop
def sum_list(lst: list[float]) -> float:
	"""
Return the sum of a list of numbers.
	"""
	total = 0
	for item in lst:
		total += item
	return total

# while loop
def countdown(n: int) -> list[int]:
	"""
Return a list counting down from n to 1.
Useful for loops, timers, etc.
	"""
	result = []
	while n > 0:
		result.append(n)
		n -= 1
	return result

# break and continue
def first_even(nums: list[int]) -> int | None:
	"""
Return the first even number in a list, or None if not found.
Useful for data filtering.
	"""
	for n in nums:
		if n % 2 == 0:
			return n
	return None

# =========================
# FUNCTIONS
# =========================
# Function definition, arguments, return, docstrings
def greet(name: str) -> str:
	"""
Return a greeting string for the given name.
	"""
	return f"Hello, {name}!"

def add(a: float, b: float = 0) -> float:
	"""
Return the sum of a and b (default 0).
	"""
	return a + b

# Arbitrary arguments
def sum_all(*args: float) -> float:
	"""
Return the sum of all arguments.
Useful for variable-length input.
	"""
	return sum(args)

# Keyword arguments
def print_info(**kwargs) -> str:
	"""
Return a string of key=value pairs from keyword arguments.
Useful for logging and debugging.
	"""
	return ', '.join(f"{k}={v}" for k, v in kwargs.items())

# Lambda (anonymous) functions
square = lambda x: x * x

# Nested functions
def outer(x: int) -> Callable[[int], int]:
	"""
Return a closure that adds x to its argument.
Demonstrates nested functions and closures.
	"""
	def inner(y: int) -> int:
		return x + y
	return inner

# =========================
# EXTENDED EXAMPLE USAGE
# =========================
if __name__ == "__main__":
	print("--- Type Checking ---")
	print(type_examples())

	print("\n--- Control Flow ---")
	print("Sign of -5:", sign_of_number(-5))
	print("Sum of [1,2,3]:", sum_list([1,2,3]))
	print("Countdown from 3:", countdown(3))
	print("First even in [1,3,5,8]:", first_even([1,3,5,8]))

	print("\n--- Functions ---")
	print(greet("Bob"))
	print("Add 2+3:", add(2,3))
	print("Sum all 1,2,3:", sum_all(1,2,3))
	print("Print info:", print_info(name="Alice", age=30))
	print("Square of 4:", square(4))
	print("Outer/Inner:", outer(10)(5))

	print("\n--- Comprehensions ---")
	print("Celsius temps:", temp_c)
	print("Fruit lengths:", fruit_lengths)
	print("Unique first letters:", unique_first_letters)

	print("\n--- String & List Methods ---")
	print("Cleaned sentence:", clean)
	print("Words:", words)
	print("Joined:", joined)
	print("Replaced:", replaced)
	print("Upper:", upper)
	print("Sorted nums:", nums)
	print("Count of 1:", count_1)
	print("Index of 4:", index_4)

	print("\n--- Functional Programming ---")
	print("Evens:", evens)
	print("Squared:", squared)
	print("Product:", product)
	print("All positive:", all_positive)
	print("Any even:", any_even)

	print("\n--- Exception Handling ---")
	print("Safe divide 10/2:", safe_divide(10,2))
	print("Safe divide 10/0:", safe_divide(10,0))

	print("\n--- File I/O ---")
	print("File content:", write_and_read_file())

	print("\n--- Modules & Packages ---")
	print("Pi:", pi_val)
	print("Sqrt 16:", sqrt_16)

	print("\n--- Decorators & Generators ---")
	print(decorated_greet("Streamlit"))
	print("Generator output:", list(generator_example()))

	print("\n--- Type Annotations ---")
	print("Add typed 2+3:", add_typed(2,3))

	print("\n--- Context Managers ---")
	with custom_context() as val:
		print("Inside context:", val)

	print("\n--- Regex ---")
	print("Regex examples:", regex_examples())

	print("\n--- Datetime ---")
	print("Datetime examples:", datetime_examples())

	print("\n--- Argparse ---")
	print("Argparse example:", argparse_example())


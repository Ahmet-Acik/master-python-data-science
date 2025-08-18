"""
basics.py
---------
Variables, data types, control flow, functions.
"""

# --- Variables ---
x = 10  # integer
name = "Alice"  # string

# --- Data Types ---
integer = 42
floating = 3.14
boolean = True
my_list = [1, 2, 3]
my_tuple = (1, 2, 3)
my_dict = {'a': 1, 'b': 2}
my_set = {1, 2, 3}

# --- Control Flow ---
def control_flow_example(val):
	if val > 0:
		return "Positive"
	elif val < 0:
		return "Negative"
	else:
		return "Zero"

# --- Functions ---
def greet(name):
	return f"Hello, {name}!"

def add(a, b):
	return a + b


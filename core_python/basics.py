"""
basics.py
---------
Variables, data types, control flow, functions.
"""

# --- Variables ---
x = 10  # integer
name = "Alice"  # string
print(type(x), type(name))  # Output: <class 'int'> <class 'str'>

# --- Data Types ---
integer = 42
floating = 3.14
boolean = True
my_list = [1, 2, 3]
my_tuple = (1, 2, 3)
my_dict = {'a': 1, 'b': 2}
my_set = {1, 2, 3}

print(type(integer), type(floating), type(boolean), type(my_list), type(my_tuple), type(my_dict), type(my_set))

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

print(greet("Alice"))  # Output: Hello, Alice!
print(add(5, 3))  # Output: 8
print(control_flow_example(10))  # Output: Positive
print(control_flow_example(-5))  # Output: Negative
print(control_flow_example(0))  # Output: Zero

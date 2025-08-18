"""
advanced_basics.py
-----------------
Advanced core Python topics for data science and robust scripting.
Includes: advanced built-ins, slicing, copying, mutability, advanced error handling, advanced file I/O, iterators, unpacking, comprehensions, modules, type hints, context managers, regex, datetime, argparse, and more.
"""

# =========================
# ADVANCED BUILT-IN FUNCTIONS
# =========================
nums = [5, 2, 9, 1]
sorted_nums = sorted(nums)
reversed_nums = list(reversed(nums))
sum_with_start = sum(nums, 10)

# =========================
# SLICING
# =========================
letters = ['a', 'b', 'c', 'd', 'e']
first_three = letters[:3]
last_two = letters[-2:]
every_other = letters[::2]
reversed_letters = letters[::-1]

# =========================
# COPYING (SHALLOW VS DEEP)
# =========================
import copy
original = [[1, 2], [3, 4]]
shallow = list(original)
deep = copy.deepcopy(original)
original[0][0] = 99  # affects shallow, not deep

# =========================
# MUTABILITY/IMMUTABILITY
# =========================
immutable_tuple = (1, 2, 3)
# immutable_tuple[0] = 10  # would raise TypeError
mutable_list = [1, 2, 3]
mutable_list[0] = 10

# =========================
# ADVANCED ERROR HANDLING
# =========================
def parse_int(val):
    try:
        return int(val)
    except ValueError:
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        raise
    else:
        print("Parsed successfully!")
    finally:
        print("Done.")

# =========================
# ADVANCED FILE I/O (CSV, JSON)
# =========================
import csv, json

def write_csv():
    with open('data.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['name', 'score'])
        writer.writerow(['Alice', 90])
        writer.writerow(['Bob', 85])

def read_csv():
    with open('data.csv') as f:
        reader = csv.DictReader(f)
        return list(reader)

def write_json():
    data = {'a': 1, 'b': 2}
    with open('data.json', 'w') as f:
        json.dump(data, f)

def read_json():
    with open('data.json') as f:
        return json.load(f)

# =========================
# ITERATORS & CUSTOM ITERABLES
# =========================
class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high
    def __iter__(self):
        return self
    def __next__(self):
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1

# =========================
# ADVANCED UNPACKING
# =========================
head, *body, tail = [1, 2, 3, 4, 5]

# =========================
# NESTED/CONDITIONAL COMPREHENSIONS
# =========================
mat = [[1,2,3],[4,5,6]]
flat = [x for row in mat for x in row]
even_squares = [x**2 for x in range(10) if x % 2 == 0]

# =========================
# MODULES & __name__ == "__main__"
# =========================
def main():
    print("This runs only if called directly.")

if __name__ == "__main__":
    main()

# =========================
# TYPE HINTS (typing)
# =========================
from typing import List, Dict, Optional, Union

def greet_all(names: List[str]) -> None:
    for name in names:
        print(f"Hello, {name}")

def get_value(d: Dict[str, int], key: str) -> Optional[int]:
    return d.get(key)

def add_or_concat(a: Union[int, str], b: Union[int, str]):
    if isinstance(a, str) or isinstance(b, str):
        return str(a) + str(b)
    else:
        return a + b

# =========================
# CONTEXT MANAGERS (__enter__/__exit__)
# =========================
class FileOpener:
    def __init__(self, filename):
        self.filename = filename
    def __enter__(self):
        self.file = open(self.filename, 'r')
        return self.file
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

# =========================
# REGEX (groups, match objects)
# =========================
import re
pattern = r'(\w+)@(\w+).com'
match = re.match(pattern, 'test@example.com')
if match:
    user, domain = match.groups()

# =========================
# DATETIME (parsing, timezones)
# =========================
from datetime import datetime, timezone
iso_str = '2025-08-18T12:00:00+00:00'
dt = datetime.fromisoformat(iso_str)
now_utc = datetime.now(timezone.utc)

# =========================
# ARGPARSE (subcommands, help)
# =========================
import argparse

def argparse_advanced():
    parser = argparse.ArgumentParser(description='Advanced Example')
    subparsers = parser.add_subparsers(dest='command')
    foo_parser = subparsers.add_parser('foo')
    foo_parser.add_argument('--bar', type=int, default=0)
    args = parser.parse_args([])  # Empty for demo
    return args

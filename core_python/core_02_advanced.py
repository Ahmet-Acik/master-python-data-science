"""
advanced_basics.py
------------------
Advanced core Python topics for data science and robust scripting.
Includes: advanced built-ins, slicing, copying, mutability, advanced error handling, advanced file I/O, iterators, unpacking, comprehensions, modules, type hints, context managers, regex, datetime, argparse, and more.

All examples use type hints, docstrings, and real-world comments. See the __main__ block for practical usage.

Enhancements:
- Clear docstrings and comments for every function/class (what, why, when to use)
- Practical, data science–oriented examples (pandas, regex, datetime, etc.)
- Grouped topics with headers and explanations
- __main__ block with real-world demo code for each topic
- Type hints everywhere
- "Wrong" and "right" usage for tricky topics
- Error handling with logging/re-raise
- Context managers: class-based and contextlib
- Iterators: usage in loops and with built-ins
- Argparse: realistic CLI example
"""


# =========================
# ADVANCED BUILT-IN FUNCTIONS
# =========================
# Why: Built-ins like sorted, reversed, sum are essential for data wrangling and analysis.
nums: list[int] = [5, 2, 9, 1]
sorted_nums: list[int] = sorted(nums)  # Sort a list (ascending)
reversed_nums: list[int] = list(reversed(nums))  # Reverse a list
sum_with_start: int = sum(nums, 10)  # Sum with a starting value

# =========================
# SLICING
# =========================
# Why: Slicing is crucial for selecting subsets of data (e.g., rows/columns in arrays).
letters: list[str] = ['a', 'b', 'c', 'd', 'e']
first_three: list[str] = letters[:3]  # ['a', 'b', 'c']
last_two: list[str] = letters[-2:]    # ['d', 'e']
every_other: list[str] = letters[::2] # ['a', 'c', 'e']
reversed_letters: list[str] = letters[::-1]  # ['e', 'd', 'c', 'b', 'a']

# =========================
# COPYING (SHALLOW VS DEEP)
# =========================
# Why: Copying is tricky with nested data (e.g., DataFrames, lists of lists).
import copy
original: list[list[int]] = [[1, 2], [3, 4]]
shallow: list[list[int]] = list(original)  # Wrong: only top-level copied
deep: list[list[int]] = copy.deepcopy(original)  # Right: all levels copied
original[0][0] = 99  # Affects shallow, not deep

# =========================
# MUTABILITY/IMMUTABILITY
# =========================
# Why: Understanding mutability prevents bugs in data pipelines.
immutable_tuple: tuple[int, ...] = (1, 2, 3)
# immutable_tuple[0] = 10  # TypeError: tuples are immutable
mutable_list: list[int] = [1, 2, 3]
mutable_list[0] = 10  # Lists are mutable

# =========================
# ADVANCED ERROR HANDLING
# =========================
import logging
from typing import Any

def parse_int(val: Any) -> int | None:
    """
    Try to parse an integer from val. Returns None if ValueError.
    Logs unexpected errors and re-raises them.
    """
    try:
        return int(val)
    except ValueError:
        logging.warning(f"ValueError: {val} is not an int")
        return None
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        raise
    else:
        logging.info("Parsed successfully!")
    finally:
        logging.debug("parse_int finished.")

# =========================
# ADVANCED FILE I/O (CSV, JSON, pandas)
# =========================
import csv, json
import pandas as pd
from typing import Any, Iterator

def write_csv(filename: str = 'data.csv') -> None:
    """
    Write sample data to a CSV file.
    Use for exporting tabular data (e.g., model results).
    """
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['name', 'score'])
        writer.writerow(['Alice', 90])
        writer.writerow(['Bob', 85])

def read_csv(filename: str = 'data.csv') -> list[dict[str, str]]:
    """
    Read a CSV file into a list of dicts.
    Use for small files or config tables.
    """
    with open(filename) as f:
        reader = csv.DictReader(f)
        return list(reader)

def read_csv_pandas(filename: str = 'data.csv') -> pd.DataFrame:
    """
    Read a CSV file into a pandas DataFrame (preferred for data science).
    """
    return pd.read_csv(filename)

def write_json(data: dict[str, Any], filename: str = 'data.json') -> None:
    """
    Write a dict to a JSON file.
    Use for config, model parameters, etc.
    """
    with open(filename, 'w') as f:
        json.dump(data, f)

def read_json(filename: str = 'data.json') -> dict[str, Any]:
    """
    Read a JSON file into a dict.
    """
    with open(filename) as f:
        return json.load(f)

# =========================
# ITERATORS & CUSTOM ITERABLES
# =========================
# Why: Custom iterators let you stream/process data efficiently (e.g., large files).
class Counter:
    """
    Custom iterator that counts from low to high (inclusive).
    Use for batching, pagination, etc.
    """
    def __init__(self, low: int, high: int) -> None:
        self.current = low
        self.high = high
    def __iter__(self) -> 'Counter':
        return self
    def __next__(self) -> int:
        if self.current > self.high:
            raise StopIteration
        val = self.current
        self.current += 1
        return val

# =========================
# ADVANCED UNPACKING
# =========================
# Why: Unpacking is useful for splitting data (e.g., header, body, footer rows).
head, *body, tail = [1, 2, 3, 4, 5]  # head=1, body=[2,3,4], tail=5

# =========================
# NESTED/CONDITIONAL COMPREHENSIONS
# =========================
# Why: Comprehensions are concise for data cleaning, flattening, filtering.
mat: list[list[int]] = [[1,2,3],[4,5,6]]
flat: list[int] = [x for row in mat for x in row]  # Flatten matrix
even_squares: list[int] = [x**2 for x in range(10) if x % 2 == 0]  # Filtered squares

# =========================
# MODULES & __name__ == "__main__"
# =========================
# Why: Use __main__ to provide demo/test code for modules.
def main() -> None:
    print("This runs only if called directly.")

# =========================
# TYPE HINTS (typing)
# =========================
# Why: Type hints improve code clarity and help with static analysis.
from typing import List, Dict, Optional, Union

def greet_all(names: List[str]) -> None:
    """Print a greeting for each name."""
    for name in names:
        print(f"Hello, {name}")

def get_value(d: Dict[str, int], key: str) -> Optional[int]:
    """Get value from dict, or None if not found."""
    return d.get(key)

def add_or_concat(a: Union[int, str], b: Union[int, str]) -> Union[int, str]:
    """
    Add if both are int, concatenate if both are str, else raise TypeError.
    """
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    elif isinstance(a, str) and isinstance(b, str):
        return a + b
    else:
        raise TypeError("Arguments must be both int or both str.")

# =========================
# CONTEXT MANAGERS (__enter__/__exit__, contextlib)
# =========================
# Why: Context managers ensure resources (files, DBs) are cleaned up.
from contextlib import contextmanager

class FileOpener:
    """
    Class-based context manager for opening files.
    Use when you need custom enter/exit logic.
    """
    def __init__(self, filename: str) -> None:
        self.filename = filename
    def __enter__(self) -> Any:
        self.file = open(self.filename, 'r')
        return self.file
    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.file.close()

@contextmanager
def managed_resource(name: str) -> Iterator[str]:
    """
    Context manager using contextlib (preferred for simple cases).
    """
    print(f"Acquiring {name}")
    yield name
    print(f"Releasing {name}")

# =========================
# REGEX (groups, match objects, data cleaning)
# =========================
# Why: Regex is essential for data cleaning, extraction, validation.
import re
pattern = r'(\w+)@(\w+)\.com'
match = re.match(pattern, 'test@example.com')
if match:
    user, domain = match.groups()

def clean_phone_numbers(text: str) -> list[str]:
    """
    Extract all phone numbers from text (e.g., for data cleaning).
    """
    phone_pattern = r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b'
    return re.findall(phone_pattern, text)

# =========================
# DATETIME (parsing, timezones, time series)
# =========================
# Why: Datetime is key for time series, logs, and scheduling.
from datetime import datetime, timezone
iso_str = '2025-08-18T12:00:00+00:00'
dt = datetime.fromisoformat(iso_str)
now_utc = datetime.now(timezone.utc)

def parse_dates_pandas(series: pd.Series) -> pd.Series:
    """
    Parse a pandas Series of date strings to datetime objects.
    """
    return pd.to_datetime(series)

# =========================
# ARGPARSE (subcommands, help, realistic CLI)
# =========================
# Why: Argparse is used for building robust CLI tools.
import argparse

def argparse_advanced() -> argparse.Namespace:
    """
    Example CLI with subcommands. Run from terminal:
    python advanced_basics.py foo --bar 42
    """
    parser = argparse.ArgumentParser(description='Advanced Example')
    subparsers = parser.add_subparsers(dest='command')
    foo_parser = subparsers.add_parser('foo')
    foo_parser.add_argument('--bar', type=int, default=0)
    args = parser.parse_args()
    return args

# =========================
# EXAMPLE USAGE (REAL-WORLD DEMOS)
# =========================
if __name__ == "__main__":
    print("\n--- Advanced Built-ins ---")
    print(f"Sorted: {sorted_nums}")
    print(f"Reversed: {reversed_nums}")
    print(f"Sum with start: {sum_with_start}")

    print("\n--- Slicing ---")
    print(f"First three: {first_three}")
    print(f"Last two: {last_two}")
    print(f"Every other: {every_other}")
    print(f"Reversed: {reversed_letters}")

    print("\n--- Shallow vs Deep Copy (Wrong/Right) ---")
    print(f"Original: {original}")
    print(f"Shallow: {shallow}")
    print(f"Deep: {deep}")

    print("\n--- Mutability ---")
    print(f"Tuple (immutable): {immutable_tuple}")
    print(f"List (mutable): {mutable_list}")

    print("\n--- Error Handling ---")
    print(f"parse_int('42'): {parse_int('42')}")
    print(f"parse_int('notanint'): {parse_int('notanint')}")

    print("\n--- File I/O (CSV/JSON) ---")
    write_csv()
    print(f"CSV rows: {read_csv()}")
    import os
    if os.path.exists('data.csv'):
        df = read_csv_pandas()
        print(f"Pandas DataFrame:\n{df}")
    write_json({'a': 1, 'b': 2})
    print(f"JSON: {read_json()}")

    print("\n--- Iterators ---")
    counter = Counter(1, 3)
    print("Counter values:", list(counter))
    # Use in a loop
    for i in Counter(4, 6):
        print(f"Iter: {i}")

    print("\n--- Advanced Unpacking ---")
    print(f"head: {head}, body: {body}, tail: {tail}")

    print("\n--- Comprehensions ---")
    print(f"Flat: {flat}")
    print(f"Even squares: {even_squares}")

    print("\n--- Type Hints ---")
    greet_all(['Alice', 'Bob'])
    print(f"get_value: {get_value({'x': 1}, 'x')}")
    try:
        print(f"add_or_concat(1, 2): {add_or_concat(1, 2)}")
        print(f"add_or_concat('a', 'b'): {add_or_concat('a', 'b')}")
        add_or_concat(1, 'b')  # Should raise
    except TypeError as e:
        print(f"Caught TypeError: {e}")

    print("\n--- Context Managers ---")
    with FileOpener('data.csv') as f:
        print(f"First line of data.csv: {f.readline().strip()}")
    with managed_resource('resource') as r:
        print(f"Using {r}")

    print("\n--- Regex ---")
    if match:
        user, domain = match.groups()
        print(f"Email match: user={user}, domain={domain}")
    else:
        print("No email match found.")
    phones = clean_phone_numbers('Call 555-123-4567 or 555.987.6543!')
    print(f"Phones found: {phones}")

    print("\n--- Datetime ---")
    print(f"Parsed: {dt}, Now UTC: {now_utc}")
    s = pd.Series(['2025-01-01', '2025-08-18'])
    print(f"Parsed dates: {parse_dates_pandas(s)}")

    print("\n--- Argparse (CLI) ---")
    # To test argparse, run: python advanced_basics.py foo --bar 42
    # args = argparse_advanced()
    # print(f"Args: {args}")

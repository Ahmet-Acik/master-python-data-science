"""
comprehensions.py
-----------------
List, dict, and set comprehensions for concise data transformations.
"""

def comprehension_examples():
    squares = [x**2 for x in range(5)]
    even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
    unique_lengths = {len(word) for word in ['data', 'science', 'python', 'data']}
    return squares, even_squares, unique_lengths

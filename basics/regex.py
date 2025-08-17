"""
regex.py
--------
Pattern matching and data cleaning with re.
"""
import re

def regex_examples():
    text = 'Data science 2025!'
    numbers = re.findall(r'\d+', text)
    words = re.findall(r'\w+', text)
    replaced = re.sub(r'\d+', 'YEAR', text)
    return numbers, words, replaced

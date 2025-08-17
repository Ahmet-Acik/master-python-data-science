"""
argparse_examples.py
-------------------
Using argparse for command-line tools.
"""
import argparse

def argparse_example():
    parser = argparse.ArgumentParser(description='Example')
    parser.add_argument('--x', type=int, default=1)
    args = parser.parse_args([])  # Empty list for demo
    return args.x

print(argparse_example())
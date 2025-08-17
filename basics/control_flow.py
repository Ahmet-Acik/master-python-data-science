"""
control_flow.py
---------------
Covers if-else, for, while, and basic logic.
"""

def control_flow_examples():
    results = []
    # If-else
    x = 10
    if x > 5:
        results.append('x is greater than 5')
    else:
        results.append('x is 5 or less')
    # For loop
    for i in range(3):
        results.append(i)
    # While loop
    count = 0
    while count < 2:
        results.append(f'count={count}')
        count += 1
    return results

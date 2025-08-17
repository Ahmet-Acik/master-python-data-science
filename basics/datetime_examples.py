"""
datetime_examples.py
-------------------
Working with dates and times for data analysis.
"""
from datetime import datetime, timedelta

def datetime_examples():
    now = datetime.now()
    future = now + timedelta(days=7)
    formatted = now.strftime('%Y-%m-%d')
    return now, future, formatted

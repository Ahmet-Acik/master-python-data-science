import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import importlib
import os

st.title("Master Python for Data Science")
st.write("Welcome! Practice Python and data science interactively.")

# --- Sidebar for Python Basics Modules ---
st.sidebar.title("Python Basics Explorer")
basics_dir = "basics"
modules = [f[:-3] for f in os.listdir(basics_dir) if f.endswith('.py') and not f.startswith('__')]
modules.sort()
selected = st.sidebar.selectbox("Choose a topic to explore:", modules)

if selected:
    mod = importlib.import_module(f"basics.{selected}")
    st.subheader(f"basics/{selected}.py")
    module_path = os.path.join(basics_dir, f"{selected}.py")
    with open(module_path) as f:
        module_code = f.read()
    with st.expander("Show module code"):
        st.code(module_code, language="python")

    # --- Interactive code editor ---
    st.markdown("**Practice this topic:**")
    default_code = module_code
    user_code = st.text_area("Edit and run code below:", value=default_code, height=250, key=f"editor_{selected}")
    if st.button(f"Run Your Code for {selected}"):
        import io, contextlib
        output = io.StringIO()
        result = None
        # Common imports for all basics modules
        common_imports = """
import sys
import os
import math
import re
import json
import argparse
import datetime
from functools import reduce
from contextlib import contextmanager
"""
        code_to_run = common_imports + "\n" + user_code
        try:
            with contextlib.redirect_stdout(output):
                # Use exec in a shared namespace for globals and locals
                exec_namespace = {}
                exec(code_to_run, exec_namespace, exec_namespace)
            std_output = output.getvalue()
            st.markdown("**Standard Output:**")
            if std_output.strip():
                st.code(std_output)
            else:
                st.info("No output from print statements.")
            # Only call user-defined functions (not built-ins or imported)
            import types
            user_funcs = [k for k, v in exec_namespace.items() if callable(v) and isinstance(v, types.FunctionType) and v.__module__ == '__main__']
            if 'main' in user_funcs:
                ret = exec_namespace['main']()
                st.markdown("**main() Return Value:**")
                st.success(ret)
            elif user_funcs:
                ret = exec_namespace[user_funcs[0]]()
                st.markdown(f"**{user_funcs[0]}() Return Value:**")
                st.success(ret)
        except Exception as e:
            st.error(f"Error: {e}")

# Example: DataFrame
df = pd.DataFrame(np.random.randn(50, 3), columns=['A', 'B', 'C'])
st.write("Random DataFrame:", df)

# Example: Chart
st.line_chart(df)

# Example: Seaborn plot
fig, ax = plt.subplots()
sns.histplot(data=df, x='A', kde=True, ax=ax)
st.pyplot(fig)

# Example: User code execution (safe for simple code)
import io
import contextlib

code = st.text_area("Try Python code (e.g., print('Hello'))", "print('Hello, world!')")
if st.button("Run code"):
    output = io.StringIO()
    try:
        with contextlib.redirect_stdout(output):
            exec(code)
        result = output.getvalue()
        if result:
            st.code(result)
        else:
            st.info("No output.")
    except Exception as e:
        st.error(f"Error: {e}")

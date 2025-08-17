import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import importlib
import os

# --- Custom CSS for professional look ---
st.markdown(
    """
    <style>
    .main-title {font-size:2.2rem; font-weight:700; color:#4F8BF9; margin-bottom:0.5em; letter-spacing: -1px;}
    .section-header {font-size:1.3rem; font-weight:600; color:#22223B; margin-top:1.5em; margin-bottom:0.5em;}
    .stApp {background-color: #f7f9fa;}
    .sidebar-title {font-size:1.2rem; font-weight:600; color:#4F8BF9; margin-bottom:0.5em;}
    .sidebar-section {margin-bottom:1.5em;}
    .footer {margin-top:2em; color:#888; font-size:0.95em; text-align:center;}
    .logo-title {display:flex; align-items:center; gap:0.7em; margin-bottom:1.5em;}
    .logo-img {height:40px;}
    .stTextArea textarea {font-family: 'Fira Mono', 'Consolas', monospace; font-size: 1.05em;}
    .stButton>button {background-color:#4F8BF9; color:white; font-weight:600; border-radius:6px;}
    .stButton>button:hover {background-color:#3566b8;}
    .stCode {background-color:#f0f4fa;}
    </style>
    """,
    unsafe_allow_html=True
)

# --- Logo and Title ---
st.markdown(
    '<div class="logo-title">'
    '<img src="https://img.icons8.com/color/48/000000/python--v2.png" class="logo-img">'
    '<span class="main-title">Master Python for Data Science</span>'
    '</div>', unsafe_allow_html=True)

# --- Section selection ---
st.markdown(
    """
    <style>
    .main-title {font-size:2.2rem; font-weight:700; color:#4F8BF9; margin-bottom:0.5em;}
    .section-header {font-size:1.3rem; font-weight:600; color:#22223B; margin-top:1.5em; margin-bottom:0.5em;}
    .stApp {background-color: #f7f9fa;}
    .sidebar-title {font-size:1.2rem; font-weight:600; color:#4F8BF9;}
    .sidebar-section {margin-bottom:1.5em;}
    </style>
    """,
    unsafe_allow_html=True
)


# --- Sidebar ---
with st.sidebar:
    st.markdown('<div class="sidebar-title">🧑‍💻 Python for Data Science</div>', unsafe_allow_html=True)
    section = st.radio("", ["🐍 Python Basics", "📊 Data Science"], key="section_radio")
    st.markdown('<div class="sidebar-section"><b>Topics</b></div>', unsafe_allow_html=True)
    if section == "🐍 Python Basics":
        basics_dir = "basics"
        modules = [f[:-3] for f in os.listdir(basics_dir) if f.endswith('.py') and not f.startswith('__')]
        modules.sort()
        selected = st.selectbox("Select topic:", modules, key="basics_select")
    else:
        ds_dir = "data_science"
        modules = [f[:-3] for f in os.listdir(ds_dir) if f.endswith('.py') and not f.startswith('__')]
        modules.sort()
        selected = st.selectbox("Select topic:", modules, key="ds_select")
        basics_dir = ds_dir

st.title("Master Python for Data Science")
st.write("Welcome! Practice Python and data science interactively.")

# --- Sidebar for Python Basics Modules ---
st.sidebar.title("Python Basics Explorer")
basics_dir = "basics"
modules = [f[:-3] for f in os.listdir(basics_dir) if f.endswith('.py') and not f.startswith('__')]
modules.sort()
selected = st.sidebar.selectbox("Choose a topic to explore:", modules)


# --- Main Content ---
if selected:
    mod = importlib.import_module(f"{basics_dir}.{selected}")
    st.markdown(f'<div class="section-header">{basics_dir}/{selected}.py</div>', unsafe_allow_html=True)
    module_path = os.path.join(basics_dir, f"{selected}.py")
    with open(module_path) as f:
        module_code = f.read()
    with st.expander("Show module code", expanded=False):
        st.code(module_code, language="python")

    st.markdown('<div class="section-header">Practice this topic:</div>', unsafe_allow_html=True)
    default_code = module_code
    user_code = st.text_area("Edit and run code below:", value=default_code, height=250, key=f"editor_{basics_dir}_{selected}")
    run_btn = st.button(f"▶️ Run Your Code for {selected}")
    if run_btn:
        import io, contextlib
        output = io.StringIO()
        result = None
        # Common imports for all modules
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
            st.markdown("<b>Standard Output:</b>", unsafe_allow_html=True)
            if std_output.strip():
                st.code(std_output)
            else:
                st.info("No output from print statements.")
            # Only call user-defined functions (not built-ins or imported)
            import types
            user_funcs = [k for k, v in exec_namespace.items() if callable(v) and isinstance(v, types.FunctionType) and v.__module__ == '__main__']
            if 'main' in user_funcs:
                ret = exec_namespace['main']()
                st.markdown("<b>main() Return Value:</b>", unsafe_allow_html=True)
                st.success(ret)
            elif user_funcs:
                ret = exec_namespace[user_funcs[0]]()
                st.markdown(f"<b>{user_funcs[0]}() Return Value:</b>", unsafe_allow_html=True)
                st.success(ret)
        except Exception as e:
            st.error(f"Error: {e}")

# --- Footer ---
st.markdown('<div class="footer">© 2025 Master Python for Data Science &nbsp;|&nbsp; Built with Streamlit</div>', unsafe_allow_html=True)

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

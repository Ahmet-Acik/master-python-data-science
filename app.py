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
    with st.expander("Show module code"):
        st.code(open(os.path.join(basics_dir, f"{selected}.py")).read(), language="python")
    # Find example function
    example_func = [fn for fn in dir(mod) if fn.endswith('example') or fn.endswith('examples')]
    if example_func:
        fn = getattr(mod, example_func[0])
        if st.button(f"Run Example from {selected}.py"):
            st.write("**Example Output:**")
            try:
                result = fn()
                st.success(result)
            except Exception as e:
                st.error(f"Error running example: {e}")
        else:
            st.info("Click 'Run Example' to see output.")
    else:
        st.warning("No example function found in this module.")

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

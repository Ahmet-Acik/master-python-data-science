import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Master Python for Data Science")
st.write("Welcome! Practice Python and data science interactively.")

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

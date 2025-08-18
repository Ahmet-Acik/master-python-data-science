

# Master Python for Data Science

**A modular, interactive platform to master Python and data science skills, built with Streamlit.**

---

## Features
- Interactive code editor and runner for every topic
- Switch easily between Python basics, advanced Python, and data science modules
- View, edit, and run code for each concept
- Modern, professional UI with sidebar navigation
- Extensible: add your own modules, quizzes, and datasets
- Real-world, best-practice code with comprehensive docstrings and type hints

## Project Structure

```
master-python-data-science/
│
├── app.py                  # Streamlit main app
├── requirements.txt        # List of dependencies
├── README.md               # Project overview and instructions
│
├── basics/                 # Python basics modules (auto-discovered)
├── core_python/            # Core Python (basics, advanced, OOP, exercises)
├── data_science/           # Data science modules (pandas, numpy, seaborn, sklearn, etc.)
│   └── datasets/           # Example datasets
├── quizzes/                # Quizzes and interactive exercises
└── utils/                  # Utility functions (e.g., code execution)
```

## Getting Started

1. **Clone the repository:**
    ```sh
    git clone https://github.com/Ahmet-Acik/master-python-data-science.git
    cd master-python-data-science
    ```
2. **(Optional) Create a virtual environment:**
    ```sh
    python3 -m venv .venv
    source .venv/bin/activate
    ```
3. **Install requirements:**
    ```sh
    pip install -r requirements.txt
    ```
4. **Run the app:**
    ```sh
    streamlit run app.py
    ```

## How to Use
- Use the sidebar to switch between "Python Basics", "Advanced Python", and "Data Science".
- Select a topic to view, edit, and run code interactively.
- Expand the code section to see the full source for each module.
- Practice by editing code and running it directly in the browser.

## What's Included
- **Core Python:**
   - `basics.py`: Variables, data types, control flow, functions, comprehensions, file I/O, modules, decorators, type hints, context managers, regex, datetime, argparse, and more.
   - `advanced_basics.py`: Advanced built-ins, slicing, copying, mutability, advanced error handling, advanced file I/O, iterators, unpacking, comprehensions, modules, type hints, context managers, regex, datetime, argparse, and more. All with real-world comments and example usage.
- **Data Science Modules:**
   - `numpy_intro.py`, `pandas_intro.py`, `matplotlib_intro.py`, `seaborn_intro.py`, `sklearn_intro.py`, and more.
   - Each module includes practical, real-world examples and visualizations.
   - `seaborn_intro.py` demonstrates plots using built-in datasets: titanic, penguins, flights, car_crashes, and tips.
- **Quizzes:**
   - Interactive quizzes to test your knowledge.
- **Utils:**
   - Utility functions for code execution and more.

## Best Practices
- Separation of Concerns: Keep Python basics, advanced, and data science content in separate folders.
- Reusability: Use utility modules for shared logic (e.g., code execution, data loading).
- Extensibility: Add new modules for advanced topics or new exercises without changing the main app.
- Documentation: Use `README.md` and docstrings in your modules.
- Testing: (Optional) Add a `tests/` folder for unit tests as your project grows.

## Contributing
- Fork the repo and create a feature branch
- Add your module or improvement
- Submit a pull request with a clear description

## License
MIT License

---

Happy learning and coding!

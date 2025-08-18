"""
sklearn_intro.py
----------------
Introduction to scikit-learn for machine learning.
"""
# Example: Simple classification with scikit-learn (using the digits dataset)

from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load dataset
X, y = load_digits(return_X_y=True)

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

# Train a logistic regression model
clf = LogisticRegression(max_iter=200)
clf.fit(X_train, y_train)

# Predict and evaluate
y_pred = clf.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

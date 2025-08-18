"""
seaborn_intro.py
----------------
Introduction to seaborn for statistical visualization.
"""
import seaborn as sns
import matplotlib.pyplot as plt

# Example seaborn plot: tips dataset
tips = sns.load_dataset("tips")
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="day")
plt.title("Total Bill vs Tip by Day")
plt.show()

print(sns.get_dataset_names())
iris = sns.load_dataset("iris")
titanic = sns.load_dataset("titanic")
penguins = sns.load_dataset("penguins")
flights = sns.load_dataset("flights")
diamonds = sns.load_dataset("diamonds")
planets = sns.load_dataset("planets")
exercise = sns.load_dataset("exercise")
fmri = sns.load_dataset("fmri")
tips = sns.load_dataset("tips")
car_crashes = sns.load_dataset("car_crashes")
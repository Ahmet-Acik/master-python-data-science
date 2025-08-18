"""
seaborn_intro.py
----------------
Introduction to seaborn for statistical visualization.
"""
import seaborn as sns
import matplotlib.pyplot as plt

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

# Example seaborn plot: tips dataset
tips = sns.load_dataset("tips")
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="day")
plt.title("Total Bill vs Tip by Day")
plt.show()

# Example 1: Titanic dataset - Survival by class and sex
titanic = sns.load_dataset("titanic")
sns.countplot(data=titanic, x="class", hue="sex")
plt.title("Titanic Survival Count by Class and Sex")
plt.show()

# Example 2: Penguins dataset - Flipper length vs bill length
penguins = sns.load_dataset("penguins")
sns.scatterplot(data=penguins, x="flipper_length_mm", y="bill_length_mm", hue="species")
plt.title("Penguins: Flipper Length vs Bill Length by Species")
plt.show()

# Example 3: Flights dataset - Heatmap of passengers by month and year
flights = sns.load_dataset("flights")
flights_pivot = flights.pivot(index="month", columns="year", values="passengers")
sns.heatmap(flights_pivot, annot=True, fmt="d", cmap="YlGnBu")
plt.title("Monthly Airline Passengers (Flights Dataset)")
plt.show()

# Example 4: Car Crashes dataset - Total crashes by state
car_crashes = sns.load_dataset("car_crashes")
sns.barplot(data=car_crashes, x="total", y="abbrev", orient="h")
plt.title("Total Car Crashes by US State")
plt.xlabel("Total Crashes")
plt.ylabel("State")
plt.show()




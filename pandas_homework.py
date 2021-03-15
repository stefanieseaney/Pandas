import pandas as pd
import numpy as np

"""
Perform the following tasks with pandas Series:

"""
# Create a Series from the list [7, 11, 13, 17].

print("#1: Create a Series from the list [7, 11, 13, 17].")
series = pd.Series([7, 11, 13, 17])
print(series)

# Create a Series with five elements that are all 100.0.

print()
print("#2: Create a Series with five elements that are all 100.0.")
series1 = pd.Series(100.0, range(5))
print(series1)

# Create a Series with 20 elements that are all random numbers in the range 0 to 100.
# Use method describe to produce the Series’ basic descriptive statistics.

print()
series2 = pd.Series(np.random.randint(0, 101, 20))
print("#3: Create 20 element series with random numbers and then describe.")
print(series2.describe())

# Create a Series called temperatures of the floating-point values 98.6, 98.9, 100.2 and 97.9.
# Using the index keyword argument, specify the custom indices 'Julie', 'Charlie', 'Sam' and 'Andrea'.

print()
print("#4: Make temperature series and add custom indicies.")
temperatures = pd.Series(
    [98.6, 98.9, 100.2, 97.9], index=["Julie", "Charlie", "Sam", "Andrea"]
)
print(temperatures)

# Form a dictionary from the names and values in Part (4), then use it to initialize a Series.

print()
print("#5: Use dictionary of names for temperatures.")
person_dict = {"Julie": 98.6, "Charlie": 98.9, "Sam": 100.2, "Andrea": 97.9}
temperatures = pd.Series(person_dict)
print(temperatures)
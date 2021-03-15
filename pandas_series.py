import pandas as pd

grades = pd.Series([87, 100, 94])

print(grades)

same_grade = pd.Series(98.6, range(3))

print(same_grade)

print(grades[0])

grades.count()
grades.mean()
grades.min()
grades.max()
grades.std()

#  includes all of the methods above
print(grades.describe())

grades = pd.Series([87, 100, 94], indexes=["Wally", "Eva", "Sam"])

print(grades)

# if you initialize a series with a dictionary, its keys become indexes and values become series values
grades = pd.Series({"Wally": 87, "Eva": 100, "Sam": 94})

print(grades["Eva"])

print(grades.Wally)

print(grades.dtype)

print(grades.values)

hardware = pd.Series(["Hammer", "Saw", "Wrench"])

answer = hardware.str.contains("a")
print(answer)

hardware_upper = hardware.str.upper()
print(hardware_upper)

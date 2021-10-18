import pandas as pd

grades = pd.Series([87, 100, 94])

print(grades)

grades2 = pd.Series(98.6, range(3))

# print(grades2)

print(grades[0])

# shows you all the aggregate functions of your array
print(grades.describe())


grades = pd.Series([87, 100, 94], index=["Wally", "Ava", "Sam"])


grades = pd.Series({"Wally": 87, "Eva": 100, "Sam": 94})
# keys becomes the index value in the array (use a dictionary to build an array)

# print(grades)


# print(grades["Eva"])
# when you use custom indexes, you don't have to worry about the order of index nunbers

# print(grades.Wally)
# ^^^ because indexes becomes attributes of the object

# print(grades.dtype)

# print(type(grades.values))

hardware = pd.Series(["Hammer", "Saw", "Wrench"])

print(hardware.str.contains("a"))
# returns a boolean array

print(hardware.str.upper())

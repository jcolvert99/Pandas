import pandas as pd

grades_dict = {
    "Wally": [87, 96, 79],
    "Eva": [100, 87, 90],
    "Sam": [94, 87, 90],
    "Katie": [100, 81, 82],
    "Bob": [83, 65, 85],
}
# keys in a dictionary become the columns and the values become the rows
# there would be 5 columns for each student and 3 rows for each test

grades = pd.DataFrame(grades_dict)

grades.index = ["Test1", "Test2", "Test3"]

# .T is the transpose method
# print(grades.T)

# each column is a pandas series- 1 dimensioanl arrary
"""
print(grades["Eva"])
print(grades.Sam)

"""
# using the loc and iloc methods

# used to extract a row (uses customer indexes)
print(grades.loc["Test2"])

# iloc uses number indexes (integer lock)
print(grades.iloc[1])
# ':' means consecutive, ',' means non-consecutive (must use [] brackets)

# For consecutive rows
print(grades.loc["Test1":"Test3"])
# loc method includes the upper bound
print(grades.iloc[0:3])


# for non-consecutive rows
print(grades.loc[["Test1", "Test3"]])
print(grades.iloc[[0, 2]])  # need to makr sure to have double brackets
# when pulling non-consecutive rows

# View only Eva's and Katie's grades for Test1 and Test2
print(grades.loc["Test1":"Test2", ["Katie", "Eva"]])
# don't need double brackets for rows because consecutive, need double brackets for columns
# because not consecutive


# View only Sam's THRU Bob's grades for Test1 and Test3
print(grades.loc[["Test1", "Test3"], "Sam":"Bob"])


# find all grades that were an A:
grades_A = grades[grades >= 90]
print(grades_A)
# NaN stands for not a number

grades_B = grades[(grades >= 80) & (grades < 90)]
print(grades_B)


grades_A_or_b = [(grades >= 90) | (grades >= 80)]
#'|' is the symbol for OR
print(grades_A_or_b)

print(grades.describe())
# gives aggregate info by columns

pd.set_option("precision", 2)
print(grades.T.describe())
# throwing in the .T gives you the summary info by test instead of student


# SORTINIG----------------------------------------------

# sorts by row INDEXES
print(
    grades.sort_index(ascending=False)
)  # ascending false is reverse alphabetical order
# sorts column INDEXES
print(grades.sort_index(axis=1, ascending=False))

# sorts by column VALUES (Katie and eva first because scored 100)
print(grades.sort_values(by="Test1", axis=1, ascending=False))

print(grades.T.sort_values(by="Test1", ascending=False))


print(grades.loc['Test1'].sort_values(ascending=False))
#only shows us column 1

#sort values and sort indexes return a copy of the original DataFrame
#if you add inplace=True, it replaces the original dataFrame

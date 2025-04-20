import pandas as pd

# Sample data (as provided)
listData = [
    ['John', 'math', 23],
    ['John', 'programming', 66],
    ['Mary', 'math', 45],
    ['Mary', 'programming', 33],
    ['Mark', 'SIEM', 57],
    ['Mark', 'programming', 70],
    ['Mark', 'math', 73],
    ['John', 'programming', 61]
]

# Creating DataFrame
df = pd.DataFrame(listData, columns=['name', 'subject', 'grade'])

#  Using df.describe() to get the mean of the grades
mean_from_describe = df.describe().loc['mean', 'grade']
print(f"Mean from describe(): {mean_from_describe}")



import pandas as pd
import os

# to create a folder name data to store csv file 
os.makedirs('data', exist_ok=True)

# existinf dataframe sample data
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

df = pd.DataFrame(listData, columns=['name', 'subject', 'grade'])

# to Save file
csv_path = 'data/grades.csv'

# this saves data as colmn name first followed by the data
# in this case no comma as it is take header name, csv would start witl comma DF to reflect index in DF
# Columns are defined by name, however, index are not so it is left blank and shows with comma
df.to_csv(csv_path, index=False) 

# Confirm the path
if os.path.exists(csv_path):
    print(f" File saved successfully at: {os.path.abspath(csv_path)}")
else:
    print(f" Failed to save the file.")

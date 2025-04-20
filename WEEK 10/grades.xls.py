# DataFrame into excel
# place it in data folder
# exclude index column

import pandas as pd
import os

# list of data
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
# crate your dataframe
df = pd.DataFrame(listData, columns=['name', 'subject', 'grade'])

# Define the path to the 'data' folder
path = './data/'
os.makedirs(path, exist_ok=True)

# define Excel file path
excel_filename = os.path.join(path, 'grades.xlsx')

# Writing DataFrame to Excel file without index column 
df.to_excel(excel_filename, sheet_name='data', index=False)

print(f" file saved at: {os.path.abspath(excel_filename)}")

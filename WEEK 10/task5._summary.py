import pandas as pd
import os

# Sample data
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

# Define the path to the 'data' folder (make sure it exists)
path = './data/'
os.makedirs(path, exist_ok=True)

# Excel file path
excel_filename = os.path.join(path, 'grades.xlsx')

# Write the data to an Excel file without the index column in sheet 'data'
df.to_excel(excel_filename, sheet_name='data', index=False)

# Create a summary of the DataFrame using describe()
summary_df = df.describe()

# Append the summary to another sheet 'summary' using ExcelWriter
with pd.ExcelWriter(excel_filename, engine='openpyxl', mode='a') as writer:
    summary_df.to_excel(writer, sheet_name='summary')

print(f" file saved at: {os.path.abspath(excel_filename)}")

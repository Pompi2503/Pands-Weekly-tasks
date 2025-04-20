import pandas as pd

# Set the correct path to your file
logFilename = '../data/access.txt'  

# Try reading it (use a space separator and no header)
df = pd.read_csv(logFilename, sep=' ', header=None)

# Show the first few lines to make sure it loaded
print(df.head())

# First row (index 0)
print(df.iloc[0])  # First row (index 0)


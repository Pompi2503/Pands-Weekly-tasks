import pandas as pd

# Make sure the path and filename match your setup
logFilename = './data/access.txt'

# Assign column names 
colNames = [
    'ip',
    'dash1',         
    'userId',        
    'time',
    'timezone',
    'method',
    'url',
    'protocol',
    'status_code',
    'size_of_response',
    'referer',
    'user_agent'
]

# Read log file, allow extra spaces, use Python engine for better handling of irregular spacing
df = pd.read_csv(logFilename, sep=' ', header=None, names=colNames, engine='python')

print("First 5 rows of log file with meaningful column names:")
print(df.head())

# Drop the columns that contain only dashes (i.e., 'dash1' and 'userId')
# Use `inplace=True` to modify the DataFrame directly
df.drop(columns=['dash1', 'userId'], inplace=True)

# Display cleaned-up data
print("\nData after dropping columns with only dashes:")
print(df.head())

df['time'] = df['time'].apply(lambda x: re.search('[\w:/]+', x).group()) 
# for the task you may want to use a normal function instead of lambda 
''' 
def getNewValue(x): 
    newvalue = re.search('[\w:/]+', x).group() 
    # do your stuff 
    return newvalue 
 
df['time'] = df['time'].apply(getNewValue) 
''' 
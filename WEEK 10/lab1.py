# start with pandas
# Author Deepika Gusain
import pandas as pd
listDAta= [ 
['John', 'math',        
23], 
['John', 'programming', 66], 
['Mary', 'math',        
45], 
['Mary', 'programming', 33], 
['Mark', 'SIEM',        
57], 
['Mark', 'programming', 70], 
['Mark', 'math',        
73], 
['John', 'programming', 61] 
]
# this will move the list data into Dataframe with name, subject and grades as column name
df = pd.DataFrame(listDAta, columns=['name','subject','grade'])
# hed method shows the first three lines of the list
print(df.head(3))

# describe method is used to give details like count, mean, std and min, max on the column with numerical data
print(df.describe())
# this will print class of this Dataframe
print(type(df.describe()))
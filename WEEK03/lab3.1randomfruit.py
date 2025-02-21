# run a program to print random fruit from the list
# Author Deepika Gusain
import random
# allocate items in the List
fruits = ['Apple', 'Orange', 'Banana', 'Pear']
# we want to prepare number between 0 and -1
# generate random number betwen 0 and the last valid index of the list fruits
index = random.randint(0,len(fruits)-1)
# Retrive an element from the List fruits using specified index
fruit =fruits[index]
# Print random fruit from the list
print("A random fruits: {}".format(fruit))





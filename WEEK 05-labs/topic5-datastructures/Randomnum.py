# program to create queue with random num and thenremove and print remaining queue
# Author Deepika Gusain
import random
queue = []  
numberOfNumbers = 10  
rangeTo = 100
# Create a queue and fill it with 10 random num from 1 to 100
for n in range(numberOfNumbers):  
    queue.append(random.randint(0, rangeTo))  
# Printing the initial queue
print(f"Queue is {queue}")  
# Removing elements one by one
while len(queue) != 0:  
    currentNumber = queue.pop(0)  
    print(f"Current Number is {currentNumber} and the queue is {queue}") 
# Queue is now empty
print("The queue is now empty")
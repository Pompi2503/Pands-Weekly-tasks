import numpy as np
import matplotlib.pyplot as plt
minSal = 20000
maxSal = 80000
numberofEntries = 10
salaries = np.random.randint(minSal, maxSal, numberofEntries)
age = np.random.randint(low = 21, high = 65, size = numberofEntries)
plt.scatter(age, salaries)
plt.show()
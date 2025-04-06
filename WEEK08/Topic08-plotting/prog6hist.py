import numpy as np
import matplotlib.pyplot as plt
minSal = 20000
maxSal = 80000
numberofEntries = 10
salaries = np.random.randint(minSal, maxSal, numberofEntries)
plt.hist(salaries)
plt.show()


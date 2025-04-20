# plottask.py
# Author Deepika Gusain
# code generated a histograom of normal distribution and plot of x^3.
# Import Numpy library for numerical calculations (https://numpy.org/doc/stable/)
import numpy as np
# import matplotlib for plotting (https://matplotlib.org/stable/)
import matplotlib.pyplot as plt
# to generate 1000 values from a normal ditribition with mean=5, std=2
# (https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html)
mean = 5
std_dev = 2
num_samples = 1000
normal_data = np.random.normal(mean, std_dev, num_samples)
# to plot function x^3, take 100 values with 0 to 10 using linspace
# (https://numpy.org/doc/stable/reference/generated/numpy.linspace.html)
x = np.linspace(0, 10, 100)
# use element wise power operations (https://numpy.org/doc/stable/user/basics.broadcasting.html)
h_x = x**3
# figure method is used to set figure size for bettwe visualisation 
# Reference: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html)
plt.figure(figsize=(8, 6))

# ploting of histogram with arguments as array of normal_data, bins=30 to divide data in 30 bins
# alpha = .6 to set transparenct to 60%
# color to add blue color
# lable as normal distrbution (https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html)
plt.hist(normal_data, bins=30, alpha=0.6, color='blue', label='Normal Distribution')

# plot fucntion x^3 with x as input feeding to fucntion, color red, and lable (https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html)
plt.plot(x, h_x, color='red', linewidth=2, label='h(x) = x³')

# Add lable to x axis (https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html)
plt.xlabel('X-axis')

# Add lebel to y axis (https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html)
plt.ylabel('Frequency / Function Value')

# add title to the plot (https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html)
plt.title('Histogram and Function Plot')

# Add legend to the plot (https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html)
plt.legend()

# add grid to the plot (https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.grid.html)
plt.grid(True)

# Save a png format file using method savefig (https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html)
plt.savefig('plot.png')

# display plot show method (https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html)
plt.show()
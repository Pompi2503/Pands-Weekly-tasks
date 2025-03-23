
import numpy as np
import matplotlib.pyplot as plt
mean = 5
std_dev = 2
num_samples = 1000
normal_data = np.random.normal(mean, std_dev, num_samples)
x = np.linspace(0, 10, 100)
h_x = x**3
plt.figure(figsize=(8, 6))
plt.hist(normal_data, bins=30, alpha=0.6, color='blue', label='Normal Distribution')
plt.plot(x, h_x, color='red', linewidth=2, label='h(x) = x³')
plt.xlabel('X-axis')
plt.ylabel('Frequency / Function Value')
plt.title('Histogram and Function Plot')
plt.legend()
plt.grid(True)
plt.savefig('plot.png')
plt.show()
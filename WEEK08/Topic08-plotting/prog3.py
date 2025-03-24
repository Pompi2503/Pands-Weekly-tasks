import numpy as np

# Set the seed for reproducibility
np.random.seed(1)

# Generate 10 random salaries between 20000 and 80000
salaries = np.random.randint(20000, 80001, size=10)

# Create a new array with salaries increased by 5000
updated_salaries = salaries + 5000  # NumPy allows element-wise addition

# Print both salary arrays
print("Original Salaries:", salaries)
print("Updated Salaries (with +5000):", updated_salaries)

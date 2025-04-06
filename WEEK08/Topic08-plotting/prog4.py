import numpy as np

# Set the seed for reproducibility
np.random.seed(1)

# Generate 10 random salaries between 20000 and 80000
salaries = np.random.randint(20000, 80001, size=10)

# Increase all salaries by 5% (multiply by 1.05)
updated_salaries = salaries * 1.05  # NumPy automatically applies this to all elements
updated_salaries = updated_salaries.astype(int)  # Convert to integer (remove decimals)

# Print both salary arrays
print("Original Salaries:", salaries)
print("Updated Salaries (with +5% increase):", updated_salaries)

import numpy as np
import matplotlib.pyplot as plt

# Project matrix
P = np.array([[1, 1],
              [1, 0]])

# Initial state vector: [number one-month-old pair, number of two-month-old pair]
v = np.array([1, 1])

# Store the number of one-month-old rabbits for each generation
months = [0]
one_month_old = [v[0]]

# Calculate for 10 generations
for i in range(1, 11):
    v = P @ v  # Matrix multiplication
    months.append(i)
    one_month_old.append(v[0])

# Plot the results
plt.plot(months, one_month_old)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Number of One-Month-Old Rabbit Pairs' )
plt.title('Rabbit Population Growth: First 10 Generations')
plt.grid(True)
plt.xticks(months)
plt.tight_layout()
plt.show()

# Print the values
print("Month | One-Month-Old Pairs")
print("-" * 30)
for i in range(len(months)):
    print(f"{months[i]:2d} | {one_month_old[i]:3d}")

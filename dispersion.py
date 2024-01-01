import numpy as np


# Function to calculate quartiles
def calculate_quartiles(data):
    q1 = np.percentile(data, 25)
    q2 = np.percentile(data, 50)
    q3 = np.percentile(data, 75)
    return q1, q2, q3

# Get input from user
input_str = input("Enter a list of numbers separated by spaces: ")
numbers = [float(x) for x in input_str.split()]

# Calculate statistics
mean = np.mean(numbers)
std_dev = np.std(numbers)
variance = np.var(numbers)
q1, q2, q3 = calculate_quartiles(numbers)

# Display results
print("Mean:", mean)
print("Standard Deviation:", std_dev)
print("Variance:", variance)
print("Quartiles: Q1 =", q1, "Q2 =", q2, "Q3 =", q3)
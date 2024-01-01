from collections import Counter

def calculate_mean(numbers):
    total = sum(numbers)
    mean = total / len(numbers)
    return mean

def calculate_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 0:
        median = (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2
    else:
        median = sorted_numbers[n // 2]
    return median

def calculate_mode(numbers):
    counter = Counter(numbers)
    mode = [number for number, count in counter.items() if count == max(counter.values())]
    return mode

# Input: List of numbers
num_list = [float(x) for x in input("Enter a list of numbers separated by spaces: ").split()]

# Calculate mean, median, and mode using functions
mean = calculate_mean(num_list)
median = calculate_median(num_list)
mode = calculate_mode(num_list)


print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode}")
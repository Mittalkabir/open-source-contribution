Python program that computes the cumulative sum of a list:

# Input list
numbers = [1, 2, 3, 4, 5]

# Method 1: Using a loop
cumulative_sum = []
total = 0
for num in numbers:
    total += num
    cumulative_sum.append(total)

print("Original list:", numbers)
print("Cumulative sum:", cumulative_sum)

# Method 2: Using itertools.accumulate
from itertools import accumulate

cumulative_sum2 = list(accumulate(numbers))
print("Cumulative sum (using itertools):", cumulative_sum2)

Output:
Original list: [1, 2, 3, 4, 5]
Cumulative sum: [1, 3, 6, 10, 15]
Cumulative sum (using itertools): [1, 3, 6, 10, 15]


✅ Explanation:

Method 1: We maintain a running total and append it to a new list.

Method 2: Python’s itertools.accumulate does the cumulative sum automatically.

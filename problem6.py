import time

# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

n = 100

sum_of_squares = n * (n+1) * (2*n+1) // 6
square_of_sum = n * n * (n+1) * (n+1) // 4
difference = square_of_sum - sum_of_squares

print(difference)
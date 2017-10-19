# https://projecteuler.net/problem=28

# The numbers on the corners added in the nth step:
# 4n^2 -2n + 1, 4n^2 + 1, 4n^2 + 2n + 1, 4n^2 + 4n +1
# We get the following rucurence for s(n) = the sum of numbers on the diagonals:
# s(n) = s(n-1) + 16n^2 + 4n^2 + 4, s(0) = 1
# Solution:
# s(n) = 2*n * (n * (8*n + 15) + 13) // 3 + 1

n = 500

s = 2*n * (n * (8*n + 15) + 13) // 3 + 1

print(s)

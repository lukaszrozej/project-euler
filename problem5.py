import time

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


# 1. My solution:

def gcd(a, b):
	while b != 0:
		a, b = b, a % b
	return a

def lcm_from_1_to(n):
	a = 1
	for b in range(2,n+1):
		a = a * b // gcd(a, b)
	return a

t = time.process_time()
lcm_from_1_to(20)
elapsed_time = time.process_time() - t
print('time: ', elapsed_time)

print( lcm_from_1_to(20) )
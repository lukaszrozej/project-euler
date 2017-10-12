import time

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

# 1. My simple solution

def is_prime(n):
	if n == 1:
		return False
	if n == 2 or n == 3:
		return True
	i = 2
	while i*i <= n:
		if n % i == 0:
			return False
		i += 1
	return True

def nth_prime(n):
	k = 1
	while n > 0:
		k += 1
		if is_prime(k):
			n -= 1
	return k

t = time.process_time()
nth_prime(10001)
elapsed_time = time.process_time() - t
print('time: ', elapsed_time)

print( nth_prime(10001)	)

# 2. 

def is_prime(n):
	if n == 1:
		return False
	if n == 2:
		return True
	if n % 2 == 0:
		return False
	i = 3
	while i*i <= n:
		if n % i == 0:
			return False
		i += 2
	return True

def nth_prime(n):
	k = 5
	counter = 3
	step = 2
	sub_step = 2
	while counter < n:
		k += step
		step += sub_step
		sub_step *= -1
		if is_prime(k):
			counter += 1
	return k

t = time.process_time()
nth_prime(10001)
elapsed_time = time.process_time() - t
print('time: ', elapsed_time)

print( nth_prime(10001)	)

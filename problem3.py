# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

# 1. 

def find_largest_prime_factor(number):
	n = number
	d = 2
	max = 1
	while n >= d:
		if n % d == 0:
			max = d
			while n % d == 0:
				n //= d
		d += 1
	if max == 1:
		return number
	else:
		return max

print(find_largest_prime_factor(600851475143))
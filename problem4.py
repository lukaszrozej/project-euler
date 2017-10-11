import time

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.


# 1. Simple loop

def largest_palindrome_product(n_digits):
	start = 10**(n_digits-1)
	stop = start*10
	max = 0
	for a in range(start, stop):
		for b in range(a, stop):
			p = a*b
			if str(p) == str(p)[::-1]:
				if p > max:
					max = p
	return max

t = time.process_time()
largest_palindrome_product(3)
elapsed_time = time.process_time() - t
print('time: ', elapsed_time)

print( largest_palindrome_product(3) )

# 2. Don't start the b loop from a, start instead from the lowest value that has a chance of giving a product larger then current largest

def largest_palindrome_product(n_digits):
	start = 10**(n_digits-1)
	stop = start*10
	max = 1
	for a in range(start, stop):
		start_b = max // a + 1
		for b in range(start_b, stop):
			p = a*b
			if str(p) == str(p)[::-1]:
				if p > max:
					max = p
	return max

t = time.process_time()
largest_palindrome_product(3)
elapsed_time = time.process_time() - t
print('time: ', elapsed_time)

print( largest_palindrome_product(3) )

# 3. Multiples of 10 aren't palindromes

def largest_palindrome_product(n_digits):
	start = 10**(n_digits-1)
	stop = start*10
	max = 1
	for a in range(start, stop):
		if a % 10 == 0:
			continue
		if a % 5 == 0:
			step = 2
		else:
			step = 1
		start_b = max // a + 1
		for b in range(start_b, stop, step):
			if b % 10 == 0:
				continue
			p = a*b
			if str(p) == str(p)[::-1]:
				if p > max:
					max = p
	return max

t = time.process_time()
largest_palindrome_product(3)
elapsed_time = time.process_time() - t
print('time: ', elapsed_time)

print( largest_palindrome_product(3) )

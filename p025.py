# The Fibonacci sequence is defined by the recurrence relation:

# Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
# Hence the first 12 terms will be:

# F1 = 1
# F2 = 1
# F3 = 2
# F4 = 3
# F5 = 5
# F6 = 8
# F7 = 13
# F8 = 21
# F9 = 34
# F10 = 55
# F11 = 89
# F12 = 144
# The 12th term, F12, is the first term to contain three digits.

# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

# 1. Just lopping until we get 1000 digits

def first_fib_num_digs(bound):
	previous = 1
	current = 1
	n = 2
	while len(str(current)) <= bound:
		current, previous = current + previous, current
		n += 1
	return n

print( first_fib_num_digs(999) )

# 2. Use fomrula for nth Fibonacci number
#  It might not work for numbers other then 1000
#  due to  finite precision

from math import log10, sqrt

def first_fib_num_digs1(bound):
	return int( (bound + log10(5)/2) / log10(1.61803398875) ) + 1 


for n in range(1,1000):
	a = first_fib_num_digs1(n)
	b = first_fib_num_digs(n)
	if a != b:
		print(n, b, a)
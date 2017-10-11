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

print( largest_palindrome_product(3) )
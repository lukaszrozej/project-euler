# Problem 2:
# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

# 1. Every third term is even valued, starting from 2

def sum_even_fibs_below(n):
	prev = 1
	curr = 2
	sum = 0
	while curr <= n:
	    sum += curr
	    curr, prev = curr + prev, curr
	    curr, prev = curr + prev, curr
	    curr, prev = curr + prev, curr
	return sum

print(sum_even_fibs_below(4000000))


# 2. Easy to check by induction that:
# 	F(n) = 4F(n-3) + F(n-6)
#   E(n) - nth even valued Fibonacci number
# 	E(n) = 4E(n-1) + E(n-2),	E(1) = 2, E(2) = 8

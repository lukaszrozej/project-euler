# https://projecteuler.net/problem=579


# WRONG! Sides don't have to be parallel to the axes

def c(n):
	total = 0
	for k in range(1,n+1):
		total += ((n-k+1)**3)
	return total

def s(n):
	total = 0
	for k in range(1,n+1):
		total += ((n-k+1)**3) * ((k+1)**3)
		# total %= 1000000000
	return total

print('c:')
print(c(1))
print(c(2))
print(c(4))
print(c(5))
print(c(10))
print(c(50))

print('s:')
print(s(1))
print(s(2))
print(s(4))
print(s(5))
print(s(10))
print(s(50))

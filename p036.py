# https://projecteuler.net/problem=36

# 1. Check all odd numbers, because palindromes in binary are odd

total = 0
for n in range(1, 1000000, 2):
	dec = format(n, 'd')
	bin = format(n, 'b')
	if bin == bin[::-1] and dec == dec[::-1]:
		total += n

print(total)

# 2. Just check if decimal palindromes are also binary palindromes
# 	so loop through first halves of decimal numbers,
# 	the second halves are first halves reversed

total = 0
for half_n in range(1, 1000):
	s = str(half_n)
	n = int( s + s[::-1] )
	bin = format(n, 'b')
	if bin == bin[::-1]:
		total += n
	n = int( s + s[:-1][::-1] )
	bin = format(n, 'b')
	if bin == bin[::-1]:
		total += n

print(total)

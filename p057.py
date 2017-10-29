# https://projecteuler.net/problem=57

from fractions import Fraction

counter = 0
f = Fraction(1)
for n in range(0,1000):
	f = 1 + 1 / (1+f)
	if len(str(f.numerator)) > len(str(f.denominator)):
		counter += 1

print(counter)
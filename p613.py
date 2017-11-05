# https://projecteuler.net/problem=613

from mpmath import *

mp.pretty = False

a = mpf(3)
b = mpf(4)

def g(x):
	def h(y):
		return ( mpf(3) * pi / mpf(2) - atan((b - y) / x) - atan((a - x) / y) ) / (pi * a * b)
	return quad(h, [0, b - b * x / a])

result = quad(g, [0, a], error=True)

print(result)
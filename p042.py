# https://projecteuler.net/problem=42

from math import sqrt

with open('p042_words.txt') as file:
	words = file.read().replace('"','').split(',')

def value(word):
	return sum(  ord(c) for c in word ) - (ord('A') - 1) * len(word)

def is_triangle_number(n):
	k = int(sqrt(2*n))
	if k*(k+1) == 2*n:
		return True
	return False


print( sum( 1 for word in words if is_triangle_number(value(word)) ) )
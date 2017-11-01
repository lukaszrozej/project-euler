# https://projecteuler.net/problem=59

import numpy as np
from  more_itertools import unique_everseen
from  itertools import product

with open('p059_cipher.txt') as file:
	cipher = list(map(int, file.read().split(',')))


def decipher(cipher, key):
	length = len(key)
	numbers = ( cipher[n] ^ key[n % length] for n in range(0, len(cipher)) )
	characters = map(chr, numbers)
	return ''.join(characters)

lists = [[],[],[]]
for n in range(0, len(cipher)):
	lists[n % 3].append(cipher[n])

for n in range(0,3):
	lists[n] = list( unique_everseen( sorted(lists[n], key=lists[n].count, reverse=True) ) )


key = [0,0,0]

# for chars in product(' e', repeat=3):
# 	for n in range(0,3):
# 		key[n] = ord(chars[n]) ^ lists[n][0]
# 	print('CHARS: ', chars)
# 	print(decipher(cipher, key))

# the most common character is ' '

for n in range(0,3):
	key[n] = ord(' ') ^ lists[n][0]

text = decipher(cipher, key)

s = sum( ord(c) for c in text )

print(text)
print(s)
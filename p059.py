# https://projecteuler.net/problem=59

with open('p059_cipher.txt') as file:
	cipher = list(map(int, file.read().split(',')))


def decipher(cipher, key):
	length = len(key)
	numbers = ( cipher[n] ^ ord(key[n % length]) for n in range(0, len(cipher)) )
	characters = map(chr, numbers)
	return ''.join(characters)

text = 'Hello World'
key = 'abc'
l = list( map(ord, text) )
print(l)
cipher = decipher(l, key)

l = list( map(ord, cipher) )

print(decipher(l, key))
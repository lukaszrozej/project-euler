# https://projecteuler.net/problem=55


def is_lychrel(n):
	s1 = str(n)
	s2 = s1[::-1]
	n = int(s1) + int(s2)
	for count in range(1, 50):
		s1 = str(n)
		s2 = s1[::-1]
		if s1 == s2:
			return False
		n = int(s1) + int(s2)
	return True

print( sum(is_lychrel(n) for n in range(1, 10000)) )
	
# https://projecteuler.net/problem=34

factorials = (1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880)

digits_count = 1
max_number = 1
while max_number < digits_count * factorials[9]:
	digits_count += 1
	max_number *= 10

s = sum( n for n in range(3, max_number) if n == sum( factorials[digit] for digit in map(int, str(n)) ) )

print(s)
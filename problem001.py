# naive version

def sum_multiples1(a, b, limit):
	sum = 0
	for i in range(1, limit):
		if i % a == 0 or i % b == 0:
			sum += i
	return sum

# no loop version (exept the one in lcm)

def least_common_multiple(a, b):
	x, y = a, b
	while x != y:
		if x < y:
			x += a
		else:
			y += b
	return x

def sum_multiples2(a, b, limit):
	limit -= 1

	a_divisors = limit // a
	sum_a = a * (a_divisors + 1) * a_divisors // 2

	b_divisors = limit // b
	sum_b = b * (b_divisors + 1) * b_divisors // 2

	lcm = least_common_multiple(a, b)
	lcm_divisors = limit // lcm
	sum_lcm = lcm * (lcm_divisors + 1) * lcm_divisors // 2

	return sum_a + sum_b - sum_lcm

# quick version specificly for 3, 5 and 1001

print(3 * 333 * 334 // 2 + 5 * 200 * 201 // 2 - 15 * 66 * 67 // 2)


sum_multiples = sum_multiples2

print(
	sum_multiples(2,3,7),
	sum_multiples(3,5,10),
	sum_multiples(3,5,1000),
	sum_multiples(2,7,8),
	sep = '\n'
)
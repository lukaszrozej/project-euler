# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

# 1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

# 1. Using long division:

def period_length(d):
	remainders = []
	r = 1
	while r != 0:
		r *= 10
		if r >= d:
			r %= d
			if r in remainders:
				break
		remainders.append(r)
	if r == 0:
		return 0
	else:
		return len(remainders) - remainders.index(r)

for d in range(1,1000):
	print(d, period_length(d) )

# print( max( (period_length(d), d) for d in range(1, 1000) ) )

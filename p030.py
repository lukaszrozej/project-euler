# https://projecteuler.net/problem=30

#  7 * 9^5 = 413343 has less then 7 digits
#  so it makes sense consider numbers of at most 6 digits

numbers = [ n for n in range(2, 1000000) if n == sum( int(digit)**5 for digit in str(n) ) ]

print( sum(numbers) )
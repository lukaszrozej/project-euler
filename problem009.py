# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a^2 + b^2 = c^2
# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

import time

# 1. My solution:
# If a, b, c is a pythagorean triple, with a^2 + b^2 = c^2
# then for some integers m, n, m > n we have:
#   a = m^2 - n^2
#   b = 2mn
#   c = m^2 + n^2
# So if a + b + c = s (*) for some given s (in this case 1000)
# we have:
#   m^2 - n^2 + 2mn + m^2 + n^2 = s
# so:
#   m(m + n) = s/2
# and we know s is even
# Because m > n we get:
#   m > isqrt(s) / 2
# So to find a, b, c satisfying (*),
# I find m, n by looping over all ms
# from isqrt(s) / 2 to isqrt(s/2)
# and check if s/2 is divisible by m

from math import floor, sqrt

def mul_triple_gicven_sum(s):
    '''
    Returns a product of pythagorean triple a, b, c
    with a + b + c = s.
    If there is more then 1 returns the firs one found.
    If there are none returns none
    '''
    if s % 2 != 0:
        return None
    m = floor(sqrt(s)) // 2
    half_s = s // 2
    while m*m <= half_s:
        q, r = divmod(half_s, m)
        if r == 0:
            n = q - m
            return (m**4 - n**4) * 2 * m * n
        m += 1
    return None

t = time.process_time()
mul_triple_gicven_sum(1000)
elapsed_time = time.process_time() - t
print('time: ', elapsed_time)


print( mul_triple_gicven_sum(2800 + 9600 + 10000) )
print( 2800 + 9600 + 10000 )
print( 2800 * 9600 * 10000 )
# https://projecteuler.net/problem=48

print( sum(n**n for n in range(1, 1001)) % 10**10)
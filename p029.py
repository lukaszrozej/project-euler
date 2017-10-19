# https://projecteuler.net/problem=29

max_a = 100
max_b = 100

terms = { a**b for a in range(2, max_a+1) for b in range(2, max_b+1) }

print( len(terms) )
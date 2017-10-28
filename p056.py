# https://projecteuler.net/problem=56

maximal_sum = max( sum(map(int, str(a**b))) for a in range(1,101) for b in range(1,101) )

print(maximal_sum)

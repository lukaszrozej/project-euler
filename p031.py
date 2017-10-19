# https://projecteuler.net/problem=31

import time

# 1. Simple recursion

def how_many_ways(total, coins):
	if total == 0:
		return 1
	if not coins:
		return 0
	if len(coins) == 1:
		return total % coins[0] == 0
	result = 0
	while total >= 0:
		result += how_many_ways(total, coins[1:])
		total -= coins[0]
	return result

coins = [200, 100, 50, 20, 10, 5, 2, 1]

print(how_many_ways(200, coins))

t = time.process_time()
how_many_ways(200, coins)
elapsed_time = time.process_time() - t
print('time: ', elapsed_time) # 0.00145s

# 2. coins sorted in increasing order
# 	w(t, i) = w(t, i-1) + w(t - coins[i], i) if t >= coins[i]
#   t - total
# 	i - index of max value coins

def how_many_ways1(total, coins):
	ways = []
	for t in range(0, total+1):
		ways.append( int(total % coins[0] == 0) )
	for i in range(1, len(coins)):
		for t in range(coins[i], total+1):
			ways[t] = ways[t] + ways[t - coins[i]]
	return ways[total]

coins = [1, 2, 5, 10, 20, 50, 100, 200]

print( how_many_ways1(200, coins) )

t = time.process_time()
how_many_ways1(200, coins)
elapsed_time = time.process_time() - t
print('time: ', elapsed_time) # 0.00145s

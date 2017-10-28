# https://projecteuler.net/problem=54

import numpy as np

with open('p054_poker.txt') as file:
	games = file.read().split('\n')

values = '23456789TJQKA'

def rank(hand):
	flush = all(card[1] == hand[0][1] for card in hand)

	hand = sorted(map(lambda card: values.index(card[0]), hand), reverse=True)
	unique, counts = np.unique(hand, return_counts=True)
	repetitions = sorted(zip(counts, unique), reverse=True)

	straight = all( d == -1 for d in np.diff(hand) ) and unique.size == 5

	if straight and flush:
		return [8] + hand
	if flush:
		return [5] + hand
	if straight:
		return [4] + hand
	if repetitions[0][0] == 4:
		return [7, repetitions[0][1]] + hand
	if repetitions[0][0] == 3:
		if repetitions[1][0] == 2:
			return [6, repetitions[0][1], repetitions[1][1]] + hand
		else:
			return [3, repetitions[0][1]] + hand
	if repetitions[0][0] == 2:
		if repetitions[1][0] == 2:
			return [2, repetitions[0][1], repetitions[1][1]] + hand
		else:
			return [1, repetitions[0][1]] + hand
	return [0] + hand

counter = 0
for game in games:
	cards = game.split(' ')
	if rank(cards[:5]) > rank(cards[5:]):
		counter += 1

print(counter)
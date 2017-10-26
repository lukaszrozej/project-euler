# https://projecteuler.net/problem=54

with open('p054_poker.txt') as file:
	games = file.read().split('\n')

def rank(hand):
	return hand

counter = 0
for game in games:
	cards = game.split(' ')
	if rank(cards[:5]) > rank(cards[5:]):
		counter += 1

print(counter)
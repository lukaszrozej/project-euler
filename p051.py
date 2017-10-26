# https://projecteuler.net/problem=51

from pyprimesieve import primes
from itertools import combinations, chain
from sympy import isprime
import re

ps = primes(1000000)

def subsets(seq):
    for subset in chain.from_iterable( c for c in (combinations(seq,r) for r in range(1, len(seq)+1)) ):
        yield subset

def replacements(positions, digits, s):
    s = list(s)
    for digit in digits:
        for position in positions:
            s[position] = digit
        yield int(''.join(s))

def positions(c, s):
    return list(m.start() for m in re.finditer(c, s)) 

def find():
    for p in ps:
        s = str(p)
        for pos in subsets( positions('0', s) ):
            if sum( isprime(r) for r in (replacements(pos, '123456789', s)) ) >= 7:
                return p
        for pos in subsets( positions('1', s) ):
            if sum( isprime(r) for r in (replacements(pos, '23456789', s)) ) >= 7:
                return p
        for pos in subsets( positions('2', s) ):
            if sum( isprime(r) for r in (replacements(pos, '3456789', s)) ) >= 7:
                return p

print('ANS: ', find())
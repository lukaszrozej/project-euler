-- https://projecteuler.net/problem=10

import Data.Numbers.Primes

ans = sum $ takeWhile (<2000000) primes
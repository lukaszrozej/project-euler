-- https://projecteuler.net/problem=7

-- import Data.Numbers.Primes

primes = filterPrime [2..] 
  where filterPrime (p:xs) = 
          p : filterPrime [x | x <- xs, x `mod` p /= 0]

ans = head $ drop 10000 primes
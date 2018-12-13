-- https://projecteuler.net/problem=3

n `withoutPrimeFactor` p
  | n `mod` p == 0 = (n `div` p) `withoutPrimeFactor` p
  | otherwise      = n

primeFactorsStartingFrom :: Int -> Int -> [Int]
primeFactorsStartingFrom p n
  | p > n          = []
  | n `mod` p == 0 = p : primeFactorsStartingFrom (p+1) (n `withoutPrimeFactor` p)
  | otherwise      =     primeFactorsStartingFrom (p+1) (n `withoutPrimeFactor` p)

ans = maximum $ primeFactorsStartingFrom 2 600851475143



-- https://projecteuler.net/problem=3

n `fullyDvideBy` p
  | n `mod` p == 0 = (n `div` p) `fullyDvideBy` p
  | otherwise      = n

primeFactors :: Int -> Int -> [Int]
primeFactors p n
  | p > n          = []
  | n `mod` p == 0 = p : primeFactors (p+1) (n `fullyDvideBy` p)
  | otherwise      = primeFactors (p+1) (n `fullyDvideBy` p)

ans = maximum $ primeFactors 2 600851475143



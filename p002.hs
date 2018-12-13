-- https://projecteuler.net/problem=2

fibs = 1:2: zipWith (+) fibs (tail fibs)

ans = sum $ takeWhile (<=4000000) $ filter even fibs
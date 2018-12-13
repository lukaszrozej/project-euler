-- https://projecteuler.net/problem=1

sumMultiples :: Int -> Int -> Int
sumMultiples factor bound
  | factor < 1 || bound < 1 = 0
  | otherwise               = n * (n+1) * factor `div` 2
                              where n = (bound - 1) `div` factor

ans = sumMultiples 3 1000 + sumMultiples 5 1000 - sumMultiples 15 1000


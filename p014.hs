-- https://projecteuler.net/problem=14

import Data.Ord (comparing)
import Data.List (maximumBy)

collatzLength :: Int -> Int
collatzLength n
  | n == 1    = 1
  | even n    = 1 + collatzLength (div n 2)
  | otherwise = 1 + collatzLength (3*n + 1)

main = putStrLn $ show $ maximumBy (comparing collatzLength) [2..999999]

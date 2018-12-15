-- https://projecteuler.net/problem=14

import Data.Ord (comparing)
import Data.List (maximumBy)
import Data.Array

collatzLength :: Int -> Int
collatzLength n
  | n == 1    = 1
  | even n    = 1 + collatzLength (div n 2)
  | otherwise = 1 + collatzLength (3*n + 1)



-- from https://stackoverflow.com/questions/18534989/project-euler-no-14-haskell


collatzMemoized :: Array Integer Int
collatzMemoized = listArray (1, maxNumberToMemoize) $ map collatz [1..maxNumberToMemoize]
  where
    maxNumberToMemoize = 999999

collatz :: Integer -> Int
collatz 1 = 1
collatz n
  | inRange (bounds collatzMemoized) nextValue = 1 + collatzMemoized ! nextValue
  | otherwise = 1 + collatz nextValue
  where
    nextValue = case n of
      1 -> 1
      n | even n -> n `div` 2
        | otherwise -> 3 * n + 1

main = putStrLn $ show $ maximumBy (comparing collatz) [2..999999]
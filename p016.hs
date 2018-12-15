-- https://projecteuler.net/problem=16

import Data.Char

main = print $ sum $ map digitToInt $ show $ 2^1000
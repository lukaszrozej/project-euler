-- https://projecteuler.net/problem=12




triangleNumbers = [ n*(n+1) `div` 2 | n <- [1..]]

numberOfDivisors n = 2 + sum [ 2 | k <- [2..limit], n `mod` k == 0] - if limit*limit == n then 1 else 0
                    where limit = (floor . sqrt . fromIntegral) n

ans = head $ dropWhile ((<=500) . numberOfDivisors) triangleNumbers

main = putStrLn $ show ans
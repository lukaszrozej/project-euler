-- https://projecteuler.net/problem=6

sumOfSquares n = n * (n+1) * (2*n+1) `div` 6

squareOfSum n = n * n * (n+1) * (n+1) `div` 4

ans = squareOfSum 100 - sumOfSquares 100
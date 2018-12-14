-- https://projecteuler.net/problem=9

-- a^2 + b^2 = c^2 <=> a = m^2 - n^2, b = 2mn, c = m^2 + n^2 for some m > n > 0
--
-- a + b + c = 1000 <=> m(m+n) = 500 <=> m | 500 and n = 500/m - m
--
-- 500/m - m > 0 <=> m < sqrt(500)
-- 500/m - m < m <=> m > sqrt(250)

m = head [m | m  <- [(ceiling $ sqrt 250)..(floor $ sqrt 500)], 500 `mod` m == 0]

n = 500 `div` m - m

a = m^2 - n^2
b = 2*m*n
c = m^2 + n^2

ans = a*b*c

-- https://projecteuler.net/problem=5

-- Least comon multiple of numbers 1..n
-- On the website n = 20, but that's too easy


myLCM n =
  let
    highestPower p = last $ takeWhile (<= n) $ iterate (*p) p
    multiply acc p = if acc `mod` p == 0
                     then acc
                     else acc * highestPower p
  in
    foldl1 multiply [1..n]

ans = myLCM 20

--just found out this is simpler although a little bit slower:

ans1 = foldl1 lcm [1..20]
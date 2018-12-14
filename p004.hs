-- https://projecteuler.net/problem=4

products = [ a*b | a <- [999,998..100], b <- [a,a-1..100]]

isPalindromic n =
  let
    string = show n
  in
    string == reverse string

ans = maximum $ filter isPalindromic products
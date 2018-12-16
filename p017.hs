-- https://projecteuler.net/problem=17

import Data.Char (isAlpha)

ones :: Char -> String
ones '0' = ""
ones '1' = "one"
ones '2' = "two"
ones '3' = "three"
ones '4' = "four"
ones '5' = "five"
ones '6' = "six"
ones '7' = "seven"
ones '8' = "eight"
ones '9' = "nine"

teens :: Char -> String
teens '1' = "eleven"
teens '2' = "twelve"
teens '3' = "thirteen"
teens '4' = "fourteen"
teens '5' = "fifteem"
teens '6' = "sixteen"
teens '7' = "seventeen"
teens '8' = "eighteen"
teens '9' = "nineteen"

tens :: Char -> String
tens '1' = "ten"
tens '2' = "twenty"
tens '3' = "thirty"
tens '4' = "forty"
tens '5' = "fifty"
tens '6' = "sixty"
tens '7' = "seventy"
tens '8' = "eighty"
tens '9' = "ninety"

hundreds :: Char -> String
hundreds n = ones n ++ " hundred"

thousand :: Char -> String
thousand n = ones n ++ " thousand"

digitsToWords :: String -> String
digitsToWords n = case n of
  [x]             -> ones x
  ['0',x]         -> ones x
  ['1','0']       -> "ten"
  ['1',x]         -> teens x
  [x,y]           -> tens x ++ "-" ++ ones y
  [x,'0','0']     -> hundreds x
  [x,y,z]         -> hundreds x ++ " and " ++ digitsToWords [y,z]
  [x,'0','0','0'] -> thousand x
  x:xs            -> thousand x ++ " " ++ digitsToWords xs

numToWords :: Int -> String
numToWords = digitsToWords . show

letterCount :: Int -> Int
letterCount = length . (filter isAlpha) . numToWords

ans = sum $ map letterCount [1..1000]
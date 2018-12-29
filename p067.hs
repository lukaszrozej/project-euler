-- https://projecteuler.net/problem=67

import Data.List

import System.Environment

main = do
  s     <- readFile "p067_triangle.txt"
  putStrLn $ show $ ans s

lineToList :: String -> [Int]
lineToList line = map read $ words line :: [Int]

toTriangle :: String -> [[Int]]
toTriangle = map lineToList . lines


maxSumR :: [Int] -> [Int] -> [Int]
maxSumR [x] [y]           = [x+y]
maxSumR (x1:x2:xs) (y:ys) = max x1 x2 + y : maxSumR (x2:xs) ys

maxSum :: [Int] -> [Int] -> [Int]
maxSum xs ys = 0:maxSumR xs ys 

ans :: String -> Int
ans s = maximum $ foldl' maxSum [0] $ toTriangle s

-- https://projecteuler.net/problem=19

import Data.Time (fromGregorian)
 
import Data.Time.Calendar.WeekDate (toWeekDate)

startsWithSunday (year, month) =
  let (_, _, weekDay) = toWeekDate $ fromGregorian year month 1
  in weekDay == 7

months = [(year, month) | year <- [1901..2000], month <- [1..12] :: [Int]]

ans = length $ filter startsWithSunday months

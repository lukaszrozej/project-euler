# You are given the following information, but you may prefer to do some research for yourself.

# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

# 1. Using calendar:

from calendar import weekday

sundays_count = 0
for year in range(1901, 2001):
    for month in range(1, 13):
        if weekday(year, month, 1) == 6:
            sundays_count += 1

print( sundays_count )

# 2. Using nothin, just looping over days

sundays_count = 0
weekday = 0
for year in range(1900, 2001):
    for month in range(1, 13):
        if month == 2:
            days_in_month = 28
            if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                days_in_month += 1
        elif month in (4, 6, 9, 11):
            days_in_month = 30
        else:
            days_in_month = 31
        for day in range(1, days_in_month + 1):
            if year >= 1901 and day == 1 and weekday == 6:
                sundays_count += 1
            weekday = (weekday + 1) % 7

print( sundays_count )

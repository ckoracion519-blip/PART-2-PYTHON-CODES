# MODULE 2: CALENDAR MODULE

## Introduction
The Calendar module provides functions for displaying
calendars and working with dates and years.

## Example 1: Display a Month

import calendar

year = 2026
month = 11

print(calendar.month(year, month))

*Output:*
text
   November 2026
Mo Tu We Th Fr Sa Su
                   1
 2  3  4  5  6  7  8
 9 10 11 12 13 14 15
16 17 18 19 20 21 22
23 24 25 26 27 28 29
30

## Example 2: Check Leap Year

import calendar

year = 2024

if calendar.isleap(year):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")

*Output:*
text
2024 is a leap year.

## Example 3: Number of Days in a Month

import calendar

year = 2026
month = 11

result = calendar.monthrange(year, month)

print("First weekday:", result[0])
print("Number of days:", result[1])

*Output:*
text
First weekday: 6
Number of days: 30

## Conclusion
The Calendar module helps programmers display monthly
calendars, identify leap years, and determine the number
of days in a specific month

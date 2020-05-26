
"""
Given a date, return the corresponding day of the week for that date.

The input is given as three integers representing the day, month and year respectively.

Return the answer as one of the following values {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}.

 

Example 1:

Input: day = 31, month = 8, year = 2019
Output: "Saturday"
Example 2:

Input: day = 18, month = 7, year = 1999
Output: "Sunday"
Example 3:

Input: day = 15, month = 8, year = 1993
Output: "Sunday"
 

Constraints:

The given dates are valid dates between the years 1971 and 2100.
"""

class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        # Jan 1 1971 is a Friday
        year_add_days = (year - 2020) * 365
        leap_year_add_days = (year - 1972)//4 + 1
        month_add_days = {1:0,
                         2:31,
                         3:59,
                         4:90,
                         5:120,
                         6:151,
                         7:181,
                         8:212,
                         9:243,
                         10:273,
                         11:304,
                         12:334}
        if year%4==0 and year!=2100:
            leap_year_add_days -=1
            for i in range(3,13):
                month_add_days[i]+=1
        add_days = year_add_days + leap_year_add_days + month_add_days[month]+day-1
        temp = add_days % 7
        day_in_week = {0: 'Friday',
                      1: 'Saturday',
                      2: 'Sunday',
                      3: 'Monday',
                      4: 'Tuesday',
                      5: 'Wednesday',
                      6: 'Thursday'}
        return day_in_week[temp]
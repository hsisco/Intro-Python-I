"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
    `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime

l = sys.argv
system = len(l)
print(l[2], l[1])

if system == 1:
    m = datetime.now().month
    y = datetime.now().year
    print(calendar.month(m, y))
elif system == 2:
    m = datetime.now().month
    print(calendar.month(m, l[2]))
elif system == 3:
    print(calendar.month(l[1], l[2]))
else:
    print("Please input numerical month and year")



def curr_month(*argv):
    for x in argv:

    # year=datetime.now().year, month=datetime.now().month
    # c = calendar.TextCalendar()
    # c.prmonth(year, month)
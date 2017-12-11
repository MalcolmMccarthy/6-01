'''
created by malcolm and roman
in novemember 2017
enum practice
'''

from enum import *

# enumerated type of days

weekdays = Enum('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

print(len(weekdays))
print(weekdays.Monday.index)
print(weekdays[3])
print(weekdays.Monday)

print('Wednesday' in weekdays)
weekday_selected = 'Tuesday'
if weekday_selected in weekdays:
    print(weekday_selected + 'is a valid weekday')
else:
    print('not a weekday')
    weekday_selected = int(input('enter your favourite day of the week: '))
print('your favourite day if the week is: ' + weekday_selected)




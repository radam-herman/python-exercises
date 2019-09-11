# 4.3_control_structures_exercises.py
# 9-11-19

## ex 1
# Conditional Basics
# a - prompt the user for a day of the week, print out whether the day is Monday or not
print('Enter a day of the week')
# input()

day_of_week_input = 'Monday'

if day_of_week_input.lower() == 'monday':
    print('You entered Monday, yeah!')
else:
    print("you didn't input Monday")

# b - prompt the user for a day of the week, print out whether the day is a weekday or a weekend
# list Weekday and Weekend TUPLES
weekday = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday')
weekend = ('saturday', 'sunday')

day_o_week = 'monday'
if day_o_week.lower in weekday:
    print("You entered a weekday")
elif day_o_week.lower in weekend:
    print("Yay, you entered a weekend day")

# c - create variables and make up values for
#    the number of hours worked in one week
#    the hourly rate
#    how much the week's paycheck will be
#       write the python code that calculates the weekly paycheck.
#       You get paid time and a half if you work more than 40 hours






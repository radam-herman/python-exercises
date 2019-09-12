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

hours_by_day_per_week = [8, 9, 7, 10, 11]
hours_worked_per_week = [day_hours for day_hours in hours_by_day_per_week]
print(hours_worked_per_week)

# 2 Loop Basics 
#### --- WHILE Loops -----  #####
# Create an integer variable i with a value of 5.
#  Create a while loop that runs so long as i is less than or equal to 15
#   Each loop iteration, output the current value of i, then increment i by one.
#   
  # HAVING PROBLEMS RUNNING THIS IN THIS IDE - 
      # RAN THIS IN iPYTHON AND IT WORKED FINE
i = 5
while i <= 15:
    print(i)
    i += 1

# -- Create a while loop that will count by 2's starting with 0 and ending at 100. 
      # Follow each number with a new line.

i = 0
while i <= 100:
    print(i)
    i += 2

# -- Alter your loop to count backwards by 5's from 100 to -10.

i = 100
while i >= -10:
    print(i)
    i -= 5

# -- Create a while loop that starts at 2, and displays the number squared on each line 
#       while the number is less than 1,000,000. Output should equal:

# Write a loop that uses print to create the output shown below.
# 100
#95
#90
#85
#80

### --- For Loops -----  #####

# Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.
   # For example, if the user enters 7, your program should output:

number_to_multiply = input("Enter your value for the times table: ")
# print(number_to_multiply)
for n in range(1, 11):
    # print('this is n: ', n)
    product = int(number_to_multiply) * n
    print(number_to_multiply, " X ", n, " = ", product )




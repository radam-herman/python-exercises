#  4.4_function_exercises.py

# 1 - Define a function named is_two. It should accept one input and 
# return True if the passed input is either the number or the string 2, False otherwise.
def is_two(stuff):
    if stuff == int(2) or stuff == str(2):
        return True
    else:
        return False

  # note - couldn't get assertions to actually work in iPython
assert is_two(2) == True, "1 this asserted correctly"
assert is_two("2") == True, "2 this asserted correctly"
assert is_two(5) == False, "3 this asserted correctly"

# 2 -- Define a function named is_vowel. It should return True if the passed string is a vowel, 
# False otherwise.
def is_vowel(vowel):
    vowels = ("AaEeIiOoUu")
    if vowel in vowels:
        return True
    else:
        return False

is_vowel("x")
is_vowel("a")


# 3 -- Define a function named is_consonant. 
# It should return True if the passed string is a consonant, 
# False otherwise. Use your is_vowel function to accomplish this.

def is_consonant(vowel):
    vowels = ("AaEeIiOoUu")
    if vowel in vowels:
        return False
    else:
        return True

is_consonant("x")
is_consonant("u")

        ## could also use a .lower() with vowels = ("aeiou")

# 4 -- Define a function that accepts a string that is a word. 
# The function should capitalize the first letter of the word if the word starts with a consonant.

def capitalize_first(word):
    vowels = ("AaEeIiOoUu")
    if word[0] in vowels:
        print("This starts with a vowel, not a consonant")
    else:
        print("this is a good one ", word.capitalize())

capitalize_first("uber")

capitalize_first("car")



# 5 -- Define a function named calculate_tip. It should accept a tip percentage 
# (a number between 0 and 1) and the bill total, and return the amount to tip.

def calculate_tip(tip_percent = .1, bill_total):
    if tip_percent < 0 or tip_percent > 1:
        print("Please try again between 0 and 1 - like .2")




Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.
Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.
Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).
Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.
# 10 - Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
# anything that is not a valid python identifier should be removed
# leading and trailing whitespace should be removed
# everything should be lowercase
# spaces should be replaced with underscores
# for example:
#   Name will become name
#   First Name will become first_name
#   % Completed will become completed
# 11 - Write a function named cumsum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
#   cumsum([1, 1, 1]) returns [1, 2, 3]
#   cumsum([1, 2, 3, 4]) returns [1, 3, 6, 10]

# --- Bonus ---- |||||||||||||||||||||||||||||||


# 1 - Create a function named twelveto24. It should accept a string 
# in the format 10:45am or 4:30pm and return a string that is the representation 
# of the time in a 24-hour format. Bonus write a function that does the opposite.

# 2 - Create a function named col_index. It should accept a spreadsheet column name, and return the index number of the column.
#   col_index('A') returns 1
#   col_index('B') returns 2
#   col_index('AA') returns 27
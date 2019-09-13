#  4.4_function_exercises.py

# 1 - Define a function named is_two. It should accept one input and 
# return True if the passed input is either the number or the string 2, False otherwise.
def is_two(stuff):
    if stuff == int(2) or stuff == str(2):
        return True
    else:
        return False

    ###  simplified
def is_two(stuff):
    return stuff == 2 or stuff == '2'

    ####

def is_two(stuff):
    return x in [2, "2", "two"]



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
    ### fm Zach
def is_vowel(c):
     return len(c) == 1 and c.lower in 'aeiou'



# 3 -- Define a function named is_consonant. 
# It should return True if the passed string is a consonant, 
# False otherwise. Use your is_vowel function to accomplish this.


    ### was suppoesed to use previous funxion
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

        ####
def cap_if_const(word):
    if is_const(word[0]):
        return work.capitalize()
    return word
   ### abridged if/then
 return word.capitalize() if is_consonant(word[0]) else word


# 5 -- Define a function named calculate_tip. It should accept a tip percentage 
# (a number between 0 and 1) and the bill total, and return the amount to tip.

# can't get the default method to work 
# def calculate_tip( bill_total, tip_percent = '.1'):

calculate_tip(.5, 10)

def calculate_tip( bill_total, tip_percent ):
    if float(tip_percent) < 0 or float(tip_percent) > 1:
        print("Please try again between 0 and 1 - like .2")
    else:
        the_tip = (float(tip_percent) * float(bill_total))
        print("here's the tip: ", the_tip)


#  6  Define a function named apply_discount. It should accept a original price, and a discount percentage,
 and return the price after the discount is applied.




# 7 Define a function named handle_commas. It should accept a string that is a number that contains commas
# in it as input, and return a number as output.

def handle_commas(number):
    actually_a_nmber = number.replace(',','')
    print(actually_a_nmber)


handle_commas("1,000,000")

def handle_commas(s):
    return float(s.replace(',', ""))


    "".join([c for c in s if c != ","])
    "".join(c)

# 8 Define a function named get_letter_grade. It should accept a number and return the letter grade associated 
# with that number (A-F).

def nbr_to_letter(nbr2):
    if int(nbr2) > 90:
        print(nbr2, " is the grade of - A")
    elif int(nbr2) > 80:
        print(nbr2, " is the grade of - B")
    elif int(nbr2) > 70:
        print(nbr2, " is the grade of - C")
    elif int(nbr2) > 60:
        print(nbr2, " is the grade of - D")
    else:
        print(nbr2, " is the grade of - F")

nbr_to_letter(40)


 # dictionary solution



# 9 Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

def remove_vowels(letters):
    letters_to_remove = [ 'A','a','E','e','I','i','O','o','U','u' ]
    # new_removed = []
    for i in letters_to_remove:
        letters = letters.replace( i, '')
    print(letters)

remove_vowels('Table')

remove_vowels('big bad wolf')

# 10 - Define a function named normalize_name. It should accept a string and return 
# a valid python identifier, that is:
#       - anything that is not a valid python identifier should be removed
#       - leading and trailing whitespace should be removed
#       - everything should be lowercase
#       - spaces should be replaced with underscores
# for example:
#   Name will become name
#   First Name will become first_name
#   % Completed will become completed



def normalize_name(any_name):
    number_check = [ '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' ]
    symbols_check = [ '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '=', '+', '[', '{', '}', '|', '\'', ',', '.', '<', '>', '/', '?' ]
    any_name = any_name.strip().lower()
    if any_name[0].isdigit() == True:
        any_name = any_name[1:]
        print("cannot begin with a number")
    for i in any_name:
        if i in symbols_check:
            any_name = any_name.replace(i, "")
            print("you can't use symbols ", i, " was removed")
        if i == ' ':
            any_name.replace(" ", "_")
            print("replaced spaces with underscores")
        else:
            print("no bad symbols found")
    print(any_name)


normalize_name("% Completed")
normalize_name("First Name")

chk = "first name"
chk.replace(" ", "_")


        ## RESEARCH ESCAPE CHARACTERS to resolve - '\]'

   #### some better solutions
   # solution: 
    # is identifier
def rem_spc_char(s):
    return ''.join([c for c in s if c.isalpha() or c == ' '

def normalize_name(s):
    return rem_spc_char(s).lower().strip().replace(' ', "_")

def cumsum(xs):
    sums = [xs[0]]
    for x in xs[1:]:
        sums.append(sums[-1] + x)
    return sums

def lookup_letter(c):
    return 'abcdefghijklmnopqrstuvwxyz'.index(c) + 1

# 11 - Write a function named cumsum that accepts a list of numbers and returns a list that is the cumulative sum 
# of the numbers in the list.
#   cumsum([1, 1, 1]) returns [1, 2, 3]
#   cumsum([1, 2, 3, 4]) returns [1, 3, 6, 10]
number_list = [1, 2, 3]

number_list = [2, 6, 10]

def cumulative_fx(given_list):
    cumulative_sum_list = []
    adder_number = 0
    for number in given_list:
        adder_number += number
        cumulative_sum_list.append(adder_number)
    print(cumulative_sum_list)

# --- Bonus ---- |||||||||||||||||||||||||||||||


# 1 - Create a function named twelveto24. It should accept a string 
# in the format 10:45am or 4:30pm and return a string that is the representation 
# of the time in a 24-hour format. Bonus write a function that does the opposite.

def twelveto24(time12):
    for i time12:
        if 'am' in time12:
    
    else:
        pass




# 2 - Create a function named col_index. It should accept a 
# spreadsheet column name, and return the index number of the column.
#   col_index('A') returns 1
#   col_index('B') returns 2
#   col_index('AA') returns 27
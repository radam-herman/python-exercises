# 4.5_import_exercises.py
#

# 1 Importing from own file

import functions_exercises
print(functions_exercises.handle_commas('10,000,000'))

import funcions_exercises as 



# For the following exercises, read about and use the itertools module 
# from the standard library to help you solve the problem.

import itertools

# 1 How many different ways can you combine the letters 
# from "abc" with the numbers 1, 2, and 3?

import itertools
letters = ['a','b','c']
numbers = [1, 2, 3]
# result = itertools.product(['a','b','c'], [1, 2, 3])
itertools.product(letters, numbers)
for i in itertools.product(letters, numbers):
    print(i)





import itertools as it
it.combinations(('abcd', '123'))



# 
# 
# 
# How many different ways can you combine two of the letters from "abcd"?

import itertools

letters = ['a','b','c','d']
result = itertools.combinations(letters, 2)
print(len(result))

count = 0
for each in result:
    count += 1
    print(each, " count is ", count)
    #print(count, " this many combinations")




## Use the load function from the json module to open this file, 
# it will produce a list of dictionaries. Using this data, write some code
#  that calculates and outputs the following information:

from json import load
users = load(open('profiles.json', "r"))

   # "r" is redundant



# just some random json code fm searching
# parsed_json = (json.load(functions_exercises))
# print(json.dumps(parsed_json, indent=4, sort_keys=True))

# Total number of users
len(users)
        ## ans - 19

Number of active users




Number of inactive users
Grand total of balances for all users
Average balance per user
User with the lowest balance
User with the highest balance
Most common favorite fruit
Least most common favorite fruit
Total number of unread messages for all users
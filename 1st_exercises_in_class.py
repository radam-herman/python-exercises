type(99.9) # class float
type("False")
type(False)
type('0')
type(0)
type(True)
type('True')
type([{}])
type({'a': []})
# """>>> type(99.9) # class float
<class 'float'>
>>> type("False")
<class 'str'>
>>> type(False)
<class 'bool'>
>>> type('0')
<class 'str'>
>>> type(0)
<class 'int'>
>>> type(True)
<class 'bool'>
>>> type('True')
<class 'str'>
>>> type([{}])
<class 'list'>
>>> type({'a': []})
<class 'dict'>"""

# """ What data type would best represent:
A term or phrase typed into a search box?
     string
If a user is logged in?
     boolean
A discount amount to apply to a user\'s shopping cart?
     float
Whether or not a coupon code is valid?
     boolean
An email address typed into a registration form?
     string
The price of a product?
    float
A Matrix?
    dictionary
The email addresses collected from a registration form?
    string
Information about applicants to Codeup\'s data science program?"""
    dictionary

"""For each of the following code blocks, 
read the expression and predict what the result
 of evaluating it would be, 
 then execute the expression in your Python REPL."""

'1' + 2
     TypeError: can only concatenate str (not "int") to str
6 % 4
     2
type(6 % 4)
    class 'int'
type(type(6 % 4))
    class 'type'
'3 + 4 is ' + 3 + 4
     TypeError: can only concatenate str (not "int") to str
0 < 0
     False
'False' == False
     False
True == 'True'
     False
5 >= -5
     True
!False or False
     SyntaxError: invalid syntax
True or "42"
     True
!True && !False
     SyntaxError: invalid syntax
6 % 5
     1
5 < 4 and 1 == 1
     False
'codeup' == 'codeup' and 'codeup' == 'Codeup'
     False
4 >= 0 and 1 !== '1'
     SyntaxError: invalid syntax
6 % 3 == 0
     True
5 % 2 != 0
     True
[1] + 2
    TypeError: can only concatenate list (not "int") to list
[1] + [2]
    [1, 2]
[1] * 2
    [1, 1]
[1] * [2]
    TypeError: can't multiply sequence by non-int of type 'list'
[] + [] == []
    True
{} + {}
    TypeError: unsupported operand type(s) for +: 'dict' and 'dict'

"""Write some Python code, 
that is, variables and operators,
 to describe the following scenarios. 
 Do not worry about the real operations to get the values, 
 the goal of these exercises is to understand how real world conditions 
 can be represented with code.

-- You have rented some movies for your kids: 
The little mermaid (for 3 days), Brother Bear (for 5 days, they love it),
 and Hercules (1 day, you don't know yet if they're going to like it). 
 If price for a movie per day is 3 dollars, how much will you have to pay?

# use a list of days, each index value is a movie's days rented
# yield total_days_rented
# will loop thru, sum the list and multiply by rental_rate
# for total_rental_cost

# each movies days_rented
days_rented = [3, 5, 1 ]
total_days_rented = 0
# make loop
for adding_days_rented in days_rented:
    total_days_rented += adding_days_rented
print(total_days_rented)

# rental_cost = 3 per day
rental_cost = 3

#getting total_rental_cost
total_rental_cost = rental_cost * total_days_rented
print(total_rental_cost)




Suppose you're working as a contractor for 3 companies: 
Google, Amazon and Facebook, they pay you a different rate per hour. 
Google pays 400 dollars per hour, Amazon 380, and Facebook 350. 
How much will you receive in payment for this week? 
You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.

# list hours per contract
amazon_hrs = 4
google_hrs = 6
facebook_hrs = 10
# list pay per contract
amazon_pay = amazon_hrs * 380
google_pay = google_hrs * 480
facebook_pay = facebook_hrs * 350
# calculate total pay
total_pay = amazon_pay + google_pay + facebook_pay
print(total_pay)

A product offer can be applied only 
if people buys more than 2 items, and the offer has not expired. 
Premium members do not need to buy a specific amount of products."""

if member = 'Premium':
    product_offer = True
if purchased_items >= 2 and prodcut_offer_expiration = False:
    product_offer = True
else:
    product_offer = False


""" ### A student can be enrolled to a class 
only if the class is not full and 
the class schedule does not conflict with her current schedule."""

if class_capacity = max_size_of_class or overlapping (class_sched, current_sched):
    enrollment = False
else enrollment = True


"""Use the following code to follow the instructions below:

username = 'codeup'
password = 'notastrongpassword'
Create a variable that holds a boolean value for each of the following conditions:

the password must be at least 5 characters
the username must be no more than 20 characters
the password must not be the same as the username
bonus neither the username or password can start or end with whitespace"""

username = 'codeup'
password = 'notastrongpassword'

# setting variables for constraints
password_min_length = 5
password_max_length = 20
if password < password_min_length or password > password_max_length:
    check = False
else:
    check = True
password_duplication_check(password):
    if username = password:
        check = False
    else:
        check = True

# bonus TRIM function/check
  
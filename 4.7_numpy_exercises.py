# 4.7_numpy_exercises.py

# Use the following code for the questions below:

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

# 1 How many negative numbers are there?
    ## this will get BOOL MASK
        # evens = a % 2 == 0 
        # evens
        # array([ True,  True,  True, False,  True, False,  True,  True,  True,
        # True, False, False])
  neg = a[a < 0]
  len(neg)
  >>> 4

# 2 How many positive numbers are there?

pos = a[a > 0] % 2 == 0]
len(pos)
>>> 5

# 3 How many even positive numbers are there?

pos_even = a[(a > 0) & (a % 2 == 0)]
len(pos_even) 
>>> 3

# 4 If you were to add 3 to each data point, how many positive numbers would there be?
pos_add_3 = (a + 3)[a > 0] 
len(pos_add_3)
>>> 5

# 5 If you squared each number, what would the new mean and standard deviation be?
# In [26]: old_mean = a.mean()                                                    

# In [27]: old_mean                                                               
# Out[27]: 3.0

# In [28]: old_std = a.std()                                                      

# In [29]: old_std                                                                
# Out[29]: 8.06225774829855
sqr_a = a ** 2
sqr_a.mean()
>>> 74.0

sqr_a.std()
>>> 144.0243035046516


# 6 A common statistical operation on a dataset is centering. 
# This means to adjust the data such that the center of the data is at 0. 
# This is done by subtracting the mean from each data point. Center the data set.

center_a = a - 3 
    ## or
ctr_a = a - (a.mean())
 ## both yield
>>> array([  1.,   7.,   9.,  20.,  -5.,  -4.,  -3.,  -3.,  -3.,  -9.,   0.,
       -10.])

# 7 Calculate the z-score for each data point. Recall that the z-score is given by: 
# Z = (x − μ) / σ

z_scores = (a - a.mean())/ a.std() 
>>> array([ 0.12403473,  0.86824314,  1.11631261,  2.48069469, -0.62017367,
       -0.49613894, -0.3721042 , -0.3721042 , -0.3721042 , -1.11631261,
        0.        , -1.24034735])



#  ||||||||||||||||||||||||||||||||||||||||||||||||||
#    ADDING EXTRA FOR PT 1
#  ||||||||||||||||||||||||||||||||||||||||||||||||||



import numpy as np
# Life w/o numpy to life with numpy

## Setup 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use python's built in functionality/operators to determine the following:
# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list
sum_of_a = 0
for numbers in a:
    sum_of_a += numbers

sum_of_a 
>>> 55

# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list
min_of_a  = a[0] # also tested with min = 1000
for number in a: 
    if min_of_a  > number: 
    min_of_a  = number

min_of_a
>>> 1

# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list
max_of_a = a[0] # start with a number from the array, if anything is larger then it's the new max 
for number in a: 
    if max_of_a < nbr: 
        max_of_a = nbr

max_of_a
>>> 10

# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list
mean_of_a

sum_of_a
for numbers in a:
    sum_of_a += numbers
mean_of_a = sum_of_a / len(a)

mean_of_a
>>> 11
# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together
product_of_a = 1

for number in a:
    product_of_a *= number

product_of_a
>>> 3628800

# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]
squares_of_a = []
for number in a:
    squares_of_a.append(number ** 2)

a
>>> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares_of_a
>>> [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers

odds_in_a = []
for number in a:
    if number % 2 != 0:
        odds_in_a.append(number)

odds_in_a

>>> [1, 3, 5, 7, 9]

# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.

evens_in_a = []
for number in a:
    if number % 2 == 0:
        evens_in_a.append(number)

evens_in_a
>>> [2, 4, 6, 8, 10]

## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
## Setup 2: Consider what it would take to find the 
# sum, min, max, average, sum, product, and list of squares for this list of two lists.
b = [
    [3, 4, 5],
    [6, 7, 8]
]

# Exercise 1 - refactor the following to use numpy. 
# Use sum_of_b as the variable. **Hint, you'll first need to make sure that the "b" variable is a numpy array**
sum_of_b = 0
for row in b:
    sum_of_b += sum(row)

b = np.array([
    [3, 4, 5],
    [6, 7, 8]
])

b.sum()
>>> 33


# Exercise 2 - refactor the following to use numpy. 
min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1]) 

min_of_b = b.min()
>>> 3

# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])

max_of_b = b.max()
>>> 8


# Exercise 4 - refactor the following using numpy to find the mean of b
mean_of_b = (sum(b[0]) + sum(b[1])) / (len([b[0]]) + len(b[1]))

mean_of_b = b.mean()

mean_of_b
>>> 5.5


# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
product_of_b = 1
for row in b:
    for number in row:
        product_of_b *= number

product_b = b.prod()        

product_b
>>> 20160

# Exercise 6 - refactor the following to use numpy to find the list of squares 
squares_of_b = []
for row in b:
    for number in row:
        squares_of_b.append(number**2)

squares_b = np.square(b)

squares_b
>>>
array([[ 9, 16, 25],
       [36, 49, 64]])


# Exercise 7 - refactor using numpy to determine the odds_in_b
odds_in_b = []
for row in b:
    for number in row:
        if(number % 2 != 0):
            odds_in_b.append(number)

odds_in_b = b[b % 2 != 0]

odds_in_b
>>> array([3, 5, 7])


# Exercise 8 - refactor the following to use numpy to filter only the even numbers
evens_in_b = []
for row in b:
    for number in row:
        if(number % 2 == 0):
            evens_in_b.append(number)

evens_in_b = b[b % 2 == 0]
evens_in_b
>>> array([4, 6, 8])

# Exercise 9 - print out the shape of the array b.
print(b)
>>>
[[3 4 5]
 [6 7 8]]

# Exercise 10 - transpose the array b.

transpose_b = b.transpose()

transpose_b
>>>
array([[3, 6],
       [4, 7],
       [5, 8]])

# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)
b_reshape = np.reshape(b, (1, 6))

b_reshape
>>>
array([[3, 4, 5, 6, 7, 8]])t


# Exercise 12 - reshape the array b to be a list of 6 lists, 
# each containing only 1 number (6 x 1)

b_reshape_2 = np.reshape(b, (6,1))

b_reshape_2
>>>array([[3],
       [4],
       [5],
       [6],
       [7],
       [8]])



## Setup 3
c = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# HINT, you'll first need to make sure that the "c" variable is 
# a numpy array prior to using numpy array methods.

# Exercise 1 - Find the min, max, sum, and product of c.

c.min()
>>> 1

c.max()
>>> 9

c.sum()
>>> 45

c.prod()
>>> 362880

# Exercise 2 - Determine the standard deviation of c.

c.std()
>>> 2.581988897471611

# Exercise 3 - Determine the variance of c.


# Exercise 4 - Print out the shape of the array c
print(c)
>>>
[[1 2 3]
 [4 5 6]
 [7 8 9]]

# Exercise 5 - Transpose c and print out transposed result.
c.transpose()
>>>array([
       [1, 4, 7],
       [2, 5, 8],
       [3, 6, 9]])

# Exercise 6 - Multiply c by the c-Transposed and print the result.
c_transpose = c.transpose()

multiply = c * c_transpose

multiply
>>>
array([[ 1,  8, 21],
       [ 8, 25, 48],
       [21, 48, 81]])

# Exercise 7 - Write the code necessary to sum up the result of 
# c times c transposed. Answer should be 261

sum_of = np.sum(multiply)

sum_of
>>> 261


# Exercise 8 - Write the code necessary to determine 
# the product of c times c transposed. Answer should be 131681894400.

product_of = np.prod(multiply)

product_of
>>> 131681894400


## Setup 4
d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]

dna = np.array([
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
])

# Exercise 1 - Find the sine of all the numbers in d
np.sin(dna)
>>>
array([[ 0.89399666, -0.98803162,  0.85090352,  0.        ,  0.58061118,
        -0.80115264],
       [ 0.85090352, -0.89399666,  0.98803162, -0.17604595,  0.89399666,
         0.        ],
       [-0.30481062,  0.85090352, -0.85090352,  0.89399666, -0.85090352,
        -0.80115264]])

# Exercise 2 - Find the cosine of all the numbers in d

np.cos(dna)
>>>
array([[-0.44807362,  0.15425145,  0.52532199,  1.        ,  0.81418097,
        -0.59846007],
       [ 0.52532199, -0.44807362,  0.15425145,  0.98438195, -0.44807362,
         1.        ],
       [-0.95241298,  0.52532199,  0.52532199, -0.44807362,  0.52532199,
        -0.59846007]])

# Exercise 3 - Find the tangent of all the numbers in d
np.tan(dna)
>>>array([[-1.99520041, -6.4053312 ,  1.61977519,  0.        ,  0.71312301,
         1.33869021],
       [ 1.61977519,  1.99520041,  6.4053312 , -0.17883906, -1.99520041,
         0.        ],
       [ 0.32004039,  1.61977519, -1.61977519, -1.99520041, -1.61977519,
         1.33869021]])

# Exercise 4 - Find all the negative numbers in d
   ''' running into problems here - 
    1) negative fx will only return unique apparently, ie 2nd -45 not listed??
    2) the array re
neg_dna = np.negative(dna)

>>>array([[ -90,  -30,  -45,    0, -120, -180],
       [ -45,   90,   30, -270,  -90,    0],
       [ -60,  -45,   45,  -90,   45, -180]])
       '''

dna[dna < 0]

# Exercise 5 - Find all the positive numbers in d

np.positive(dna)
>>> array([-90, -30, -45, -45])

# Exercise 6 - Return an array of only the unique numbers in d.
np.unique(dna)
>>>
array([-90, -45, -30,   0,  30,  45,  60,  90, 120, 180, 270])
len(np.unique(dna))
>>> 11
'''
len(dna) ### careful - this only returns each array!!!!!
'''
# Exercise 7 - Determine how many unique numbers there are in d.
  ## see above 

# Exercise 8 - Print out the shape of d.
print(dna)                                                            
[[ 90  30  45   0 120 180]
 [ 45 -90 -30 270  90   0]
 [ 60  45 -45  90 -45 180]]

# Exercise 9 - Transpose and then print out the shape of d.
transpose_d = dna.transpose()

transpose_d
>>>
array([[ 90,  45,  60],
       [ 30, -90,  45],
       [ 45, -30, -45],
       [  0, 270,  90],
       [120,  90, -45],
       [180,   0, 180]])

# Exercise 10 - Reshape d into an array of 9 x 2

reshape_d = np.reshape(dna, (9,2))

reshape_d

>>>
array([[ 90,  30],
       [ 45,   0],
       [120, 180],
       [ 45, -90],
       [-30, 270],
       [ 90,   0],
       [ 60,  45],
       [-45,  90],
       [-45, 180]])
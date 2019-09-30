# pandas_series.py

# 1 - Use pandas to create a Series from the following data:
["kiwi", "mango", "strawberry", "pineapple", "gala apple", 
"honeycrisp apple", "tomato", "watermelon", "honeydew", 
"kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"]

import pandas as pd

# a -- Name the variable that holds the series fruits.
fruits = pd.Series(["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"])
#

# b -- Run .describe() on the series to see what describe returns for a series of strings.
In [135]: fruits.describe()                                                     
Out[135]: 
count       17
unique      13
top       kiwi
freq         4
dtype: object

# c -- Run the code necessary to produce only the unique fruit names.
unique_fruits = fruits.value_counts()
len(unique_fruits)
unique_fruits.index
>>>Index(['kiwi', 'mango', 'pineapple', 'strawberry', 'honeydew', 'watermelon',
       'blackberry', 'gala apple', 'blueberry', 'papaya', 'honeycrisp apple',
       'tomato', 'gooseberry'],
      dtype='object')

unique_fruits2 = fruits.unique()
unique_fruits2

# d -- Determine how many times each value occurs in the series.
fruits.value_counts()
>>>
In [136]: fruits.value_counts()                                                 
Out[136]: 
kiwi                4
mango               2
pineapple           1
strawberry          1
honeydew            1
watermelon          1
blackberry          1
gala apple          1
blueberry           1
papaya              1
honeycrisp apple    1
tomato              1
gooseberry          1
dtype: int64


# e -- Determine the most frequently occurring fruit name from the series.
unique_fruits.idxmax()
>>> Out[156]: 'kiwi'

# f -- Determine the least frequently occurring fruit name from the series.
In [157]: unique_fruits.idxmin()                                                
Out[157]: 'pineapple'

# g -- Write the code to get the longest string from the fruits series.
fruits.str.len()
>>>
Out[161]: 
0      4
1      5
2     10
3      9
4     10
5     16
6      6
7     10
8      8
9      4
10     4
11     4
12     5
13     9
14    10
15    10
16     6
dtype: int64

fruits.str.len().idxmax()
>>>
Out[162]: 5

    ### using above as a mask
fruits[fruits.str.len().idxmax()]
>>>
Out[164]: 'honeycrisp apple'

# h -- Find the fruit(s) with 5 or more letters in the name.

        # DID NOT WORK -- fruits.str.len(5>)
    #THIS DID WORK
fruits[fruits.str.len() > 5]
>>>
Out[166]: 
2           strawberry
3            pineapple
4           gala apple
5     honeycrisp apple
6               tomato
7           watermelon
8             honeydew
13           blueberry
14          blackberry
15          gooseberry
16              papaya
dtype: object


# i -- Capitalize all the fruit strings in the series.
cap_fruits = fruits.str.capitalize()
>>>
In [152]: cap_fruits                                                            
Out[152]: 
0                 Kiwi
1                Mango
2           Strawberry
3            Pineapple
4           Gala apple
5     Honeycrisp apple
6               Tomato
7           Watermelon
8             Honeydew
9                 Kiwi
10                Kiwi
11                Kiwi
12               Mango
13           Blueberry
14          Blackberry
15          Gooseberry
16              Papaya
dtype: object

j -- Count the letter "a" in all the fruits (use string vectorization)
fruits.str.contains('a')
>>>
Out[169]: 
0     False
1      True
2      True
3      True
4      True
5      True
6      True
7      True
8     False
9     False
10    False
11    False
12     True
13    False
14     True
15    False
16     True
dtype: bool

In [170]: fruits[fruits.str.contains('a')]                                      
Out[170]: 
1                mango
2           strawberry
3            pineapple
4           gala apple
5     honeycrisp apple
6               tomato
7           watermelon
12               mango
14          blackberry
16              papaya
dtype: object

fruits[fruits.str.contains('a').count()]
fruits[len (fruit for fruit in fruits if chr for chr in fruit if chr.lower() in 'aeiou')]

k -- Output the number of vowels in each and every fruit.
    # hint ZIP

fruits['fruit_vowel_count'] = fruits[fruit_vowel for fruit_vowel ]





l -- Use the .apply method and a lambda function to find the fruit(s) 
containing two or more "o" letters in the name.


fruits[fruits.str.contains('p') > 1]

# m -- Write the code to get only the fruits containing "berry" in the name
In [172]: fruits[fruits.str.contains('berry')]                                  
Out[172]: 
2     strawberry
13     blueberry
14    blackberry
15    gooseberry
dtype: object

# n -- Write the code to get only the fruits containing "apple" in the name
In [174]: fruits[fruits.str.contains('apple')]                                  
Out[174]: 
3           pineapple
4          gala apple
5    honeycrisp apple
dtype: object

o -- Which fruit has the highest amount of vowels?



# 2 Use pandas to create a Series from the following data:


['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23']
#
import pandas as pd
money = pd.Series(['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23'])
#

# What is the data type of the series?
>>>
In [191]: type(money)                                                           
Out[191]: pandas.core.series.Series


# Use series operations to convert the series to a numeric data type.

new_money = money.str.replace('$','')
new_money2 = new_money.str.replace(',','') # NOTE - stacking did not work so ran separately

>>>
Out[197]: 
0      796459.41
1         278.60
2      482571.67
3     4503915.98
4      2121418.3
5      1260813.3
6       87231.01
7     1509175.45
8     4138548.00
9     2848913.80
10     594715.39
11    4789988.17
12     4513644.5
13    3191059.97
14    1758712.24
15    4338283.54
16    4738303.38
17    2791759.67
18     769681.94
19     452650.23
dtype: object
'''
new_money2 = new_money2.astype('float')
In [213]: new_money2.dtype                                                      
Out[213]: dtype('float64')
'''
>>>
In [225]: new_money2.sort_values(ascending=False)                               
Out[225]: 
11    4789988.17
16    4738303.38
12    4513644.50
3     4503915.98
15    4338283.54
8     4138548.00
13    3191059.97
9     2848913.80
17    2791759.67
4     2121418.30
14    1758712.24
7     1509175.45
5     1260813.30
0      796459.41
18     769681.94
10     594715.39
2      482571.67
19     452650.23
6       87231.01
1         278.60
dtype: float64


# What is the maximum value? 
>>>'''
In [215]: new_money2.max()                                                      
Out[215]: 4789988.17
'''

# The minimum?

>>>'''
In [214]: new_money2.min()                                                      
Out[214]: 278.6
'''

# Bin the data into 4 equally sized intervals and show how many values fall into each bin.
>>>
In [227]: bin_money = new_money2.sort_values(ascending=False)                   

In [228]: bin_money.dtype                                                       
Out[228]: dtype('float64')

'''
In [229]: pd.cut(bin_money, 4)                                                  
Out[229]: 
11     (3592560.778, 4789988.17]
16     (3592560.778, 4789988.17]
12     (3592560.778, 4789988.17]
3      (3592560.778, 4789988.17]
15     (3592560.778, 4789988.17]
8      (3592560.778, 4789988.17]
13    (2395133.385, 3592560.778]
9     (2395133.385, 3592560.778]
17    (2395133.385, 3592560.778]
4     (1197705.993, 2395133.385]
14    (1197705.993, 2395133.385]
7     (1197705.993, 2395133.385]
5     (1197705.993, 2395133.385]
0        (-4511.11, 1197705.993]
18       (-4511.11, 1197705.993]
10       (-4511.11, 1197705.993]
2        (-4511.11, 1197705.993]
19       (-4511.11, 1197705.993]
6        (-4511.11, 1197705.993]
1        (-4511.11, 1197705.993]
dtype: category
Categories (4, interval[float64]): [(-4511.11, 1197705.993] < (1197705.993, 2395133.385] <
                                    (2395133.385, 3592560.778] < (3592560.778, 4789988.17]]
'''
import matplotlib.pyplot as plt
import pandas as pd
money = pd.Series(['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23'])
#
new_money = money.str.replace('$','')
new_money2 = new_money.str.replace(',','')
new_money2 = new_money2.astype('float')

bin_money = new_money2.sort_values(ascending=False) 

bin_money.plot.hist()
    # place any title reorg stuff here between plot and show

    
plt.show()
Plot a histogram of the data. Be sure to include a title and axis labels.



# 3 - Use pandas to create a Series from the following exam scores:

[60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78]
What is the minimum exam score? The max, mean, median?
Plot a histogram of the scores.
Convert each of the numbers above into a letter grade. For example, 86 should be a 'B' and 95 should be an 'A'.
Write the code necessary to implement a curve. I.e. that grade closest to 100 should be converted to a 100, and that many points should be given to every other score as well.


# 4 - Use pandas to create a Series from the following string:

'hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy'
What is the most frequently occuring letter? Least frequently occuring?
How many vowels are in the list?
How many consonants are in the list?
Create a series that has all of the same letters, but uppercased
Create a bar plot of the frequencies of the 6 most frequently occuring letters.


# |||||||||||||||||||||||||||||||||||||||||||||||||||||||
# |||||||||||||||||||||||||||||||||||||||||||||||||||||||
        # DATAFRAMES EXERCISES APPENDED BELOW
# |||||||||||||||||||||||||||||||||||||||||||||||||||||||
# |||||||||||||||||||||||||||||||||||||||||||||||||||||||

# For several of the following exercises, you'll need to load several datasets 
# using the pydataset library. (If you get an error when trying to run the import 
# below, use pip to install the pydataset package.)

from pydataset import data

# When the instructions say to load a dataset, you can pass the name of the dataset
#  as a string to the data function to load the dataset. 
# You can also view the documentation for the data set by passing 
#      the show_doc keyword argument.

# data('mpg', show_doc=True) # view the documentation for the dataset
mpg = data('mpg') # load the dataset and store it in a variable

All the datasets loaded from the pydataset library will be pandas dataframes.

# 1 - Copy the code from the lesson to create a dataframe full of student grades.
# a - Create a column named passing_english that indicates whether 
#       each student has a passing grade in reading.

# b - Sort the english grades by the passing_english column. How are duplicates handled?
# c - Sort the english grades first by passing_english and then by student name.
#        All the students that are failing english should be first, 
#       and within the students that are failing english they should be 
#       ordered alphabetically. The same should be true for the students 
#       passing english. (Hint: you can pass a list to the .sort_values method)
# d - Sort the english grades first by passing_english, and then by the actual
#        english grade, similar to how we did in the last step.
# e - Calculate each students overall grade and add it as a column on the dataframe.
#        The overall grade is the average of the math, english, and reading grades.


# 2 - Load the mpg dataset. Read the documentation for the dataset and use it 
# for the following questions:

# How many rows and columns are there?
# What are the data types of each column?
# Summarize the dataframe with .info and .describe
# Rename the cty column to city.
# Rename the hwy column to highway.
# Do any cars have better city mileage than highway mileage?
# Create a column named mileage_difference this column should contain 
#       the difference between highway and city mileage for each car.
# Which car (or cars) has the highest mileage difference?
# Which compact class car has the lowest highway mileage? The best?
# Create a column named average_mileage that is the mean of the city and highway mileage.
# Which dodge car has the best average mileage? The worst?

# 3 - Load the Mammals dataset. Read the documentation for it, and 
#   use the data to answer these questions:
# How many rows and columns are there?
# What are the data types?
# Summarize the dataframe with .info and .describe
# What is the the weight of the fastest animal?
# What is the overal percentage of specials?
# How many animals are hoppers that are above the median speed? What percentage is this?
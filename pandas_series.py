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


e -- Determine the most frequently occurring fruit name from the series.
unique_fruits.max().index()

f -- Determine the least frequently occurring fruit name from the series.

g -- Write the code to get the longest string from the fruits series.

h -- Find the fruit(s) with 5 or more letters in the name.

i -- Capitalize all the fruit strings in the series.

j -- Count the letter "a" in all the fruits (use string vectorization)

k -- Output the number of vowels in each and every fruit.
    # hint ZIP

l -- Use the .apply method and a lambda function to find the fruit(s) 
containing two or more "o" letters in the name.


m -- Write the code to get only the fruits containing "berry" in the name

n -- Write the code to get only the fruits containing "apple" in the name

o -- Which fruit has the highest amount of vowels?



# 2 Use pandas to create a Series from the following data:


['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23']
What is the data type of the series?
Use series operations to convert the series to a numeric data type.
What is the maximum value? The minimum?
Bin the data into 4 equally sized intervals and show how many values fall into each bin.
Plot a histogram of the data. Be sure to include a title and axis labels.
Use pandas to create a Series from the following exam scores:


[60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78]
What is the minimum exam score? The max, mean, median?
Plot a histogram of the scores.
Convert each of the numbers above into a letter grade. For example, 86 should be a 'B' and 95 should be an 'A'.
Write the code necessary to implement a curve. I.e. that grade closest to 100 should be converted to a 100, and that many points should be given to every other score as well.
Use pandas to create a Series from the following string:


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
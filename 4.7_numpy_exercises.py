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

# 4.6.1_matplotlib
# forgot to copy to VSCode to make py file

''' #1
Use matplotlib to plot the following equation:
y = x^2 − x + 2 

Add an anotation for the point 0, 0, the origin.
'''
import matplotlib.pyplot as plt
import math

x = list(range(-49, 50))
y = [((n ** 2) - n + 2) for n in x]
plt.scatter(x, y)
plt.title('A Quadratic Distribution, $y = x^2$')
plt.xlabel('$x$')
plt.ylabel('$x^2$')
# includes annotation for ORIGIN
plt.annotate('Origin', xy=(0, 0), xytext=( -18, 500),
             arrowprops={'facecolor': 'blue'})
plt.show()

''' #2
Create and label 4 separate charts for the following equations 
(choose a range for x that makes sense): 
NOTE: You can use functions from the math module to help 
implement some of the equations.
'''

# 2.1  y = √x
x = range(1, 1000)
y = [n ** .5 for n in x]
plt.plot(x, y)
# plt.savefig('my-figure')
plt.show()


#2.2 y = x^3 aka x ** 3
x = range(1, 1000)
y = [n ** 3 for n in x]
plt.plot(x, y)
# plt.savefig('my-figure')
plt.show()


#2.3 y = tan (x)
x = range(1, 1000)
y = [math.tan(n) for n in x]
plt.plot(x, y)
# plt.savefig('my-figure')
plt.show()
# THIS ONE NEEDS SOME FURTHER WORK - DID NOT USE PI AND
# SOLUTIONS SEEMED TO USE DUE TO NATURE OF TRIG FUNCTIONS


#2.4 y = 2^x aka 2 ** x
x = range(1, 10)
y = [2 ** n for n in x]
plt.plot(x, y)
# plt.savefig('my-figure')
plt.show()


''' #3
Combine the figures you created in the last step into one large figure with 4 subplots.
'''
plt.figure(figsize=(12, 8))
# plot the first subplot
plt.subplot(2,2,1)
#y1 = [n ** .5 for n in x]
x = range(-100, 100)
y = [n ** .5 for n in x]
plt.plot(x, y)
# plt.savefig('my-figure')
plt.title('sqrt x')

# the second subplot
plt.subplot(2,2,2)
x = range(-100, 100)
y = [n ** 3 for n in x]
plt.plot(x, y)
plt.title('x ** 3')

# the third subplot
plt.subplot(2,2,3)
x = range(-100, 100)
y = [math.tan(n) for n in x]
plt.plot(x, y)
plt.title('tan x')
  ## run with pi in the range

# the fourth subplot
plt.subplot(2,2,4)
x = range(-10, 10)
y = [2 ** n for n in x]
plt.plot(x, y)
plt.title('powr of x')

plt.show()

''' #4
Comine the figures you created in the last step into one figure 
where each of the 4 equations has a different color for the points. 
Be sure to include a legend.
'''
# WASNT ABLE TO GET IT TO WORK WITH ALL 4
x = range(-10, 10)
y1 = [n ** .5 for n in x]
y2 = [n ** 3 for n in x]
#y3 = [math.tan(n) for n in x]
#y4 = [2 ** n for n in x]

plt.figure(figsize=(14, 6)) # (width, height)

plt.plot(x, y1, c='blue', label='$sqrt X$')
plt.plot(x, y2, c='orange', label='$x** 3$')
#plt.plot(x, y3, c='green', label='$tan X$')
#plt.plot(x, y4, c='red', label='$X pwr$')
# 
# 
# 

plt.legend(loc='upper right')
plt.title('Various X curves')
plt.xlabel('$x$')

plt.show()

''' BONUS
Write the code necessary to write your name on a chart. Use box letters.
'''

''' BONUS BONUS
Bonus: use curves for letters in your name that have curves in them.
'''
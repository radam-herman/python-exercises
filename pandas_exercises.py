# ADVANCED DATAFRAMES pandas_exercises

#If you get an error when trying to run the import below,
#  use pip to install the pydataset package.

from pydataset import data

mpg = data('mpg') # load the dataset and store it in a variable
# data('mpg', show_doc=True) # view the documentation for the dataset

# 1 - 
On average, which manufacturer has the best miles per gallon?

manu_best_milage = ['manufacturer','hwy']
mpg[manu_best_milage].head()
>>>
Out[24]: 
  manufacturer  hwy
1         audi   29
2         audi   29
3         audi   31
4         audi   30
5         audi   26

>>>
In [25]: mpg[manu_best_milage].sort_values(by='hwy').head()                          
Out[25]: 
    manufacturer  hwy
55         dodge   12
66         dodge   12
127         jeep   12
70         dodge   12
60         dodge   12

>>> '''
In [26]: mpg[manu_best_milage].sort_values(by='hwy', ascending=False).head()         
Out[26]: 
    manufacturer  hwy
222   volkswagen   44
213   volkswagen   44
223   volkswagen   41
197       toyota   37
106        honda   36
'''

# How many different manufacturers are there?
>>>
In [16]: mpg.manufacturer.value_counts()                                             
Out[16]: 
dodge         37
toyota        34
volkswagen    27
ford          25
chevrolet     19
audi          18
hyundai       14
subaru        14
nissan        13
honda          9
jeep           8
pontiac        5
land rover     4
mercury        4
lincoln        3

>>>  '''
In [19]: len(mpg.manufacturer.value_counts())                                        
Out[19]: 15
Name: manufacturer, dtype: int64
'''


# How many different models are there?

>>>
In [23]: mpg.model.value_counts()                                                    
Out[23]: 
caravan 2wd               11
ram 1500 pickup 4wd       10
mustang                    9
dakota pickup 4wd          9
civic                      9
jetta                      9
grand cherokee 4wd         8
a4 quattro                 8
impreza awd                8
f150 pickup 4wd            7
camry                      7
tiburon                    7
durango 4wd                7
camry solara               7
toyota tacoma 4wd          7
sonata                     7
a4                         7
passat                     7
altima                     6
new beetle                 6
4runner 4wd                6
forester awd               6
explorer 4wd               6
c1500 suburban 2wd         5
grand prix                 5
gti                        5
corolla                    5
corvette                   5
malibu                     5
mountaineer 4wd            4
pathfinder 4wd             4
range rover                4
k1500 tahoe 4wd            4
navigator 2wd              3
expedition 2wd             3
maxima                     3
a6 quattro                 3
land cruiser wagon 4wd     2
Name: model, dtype: int64
'''
>>>
In [22]: len(mpg.model.value_counts())                                               
Out[22]: 38
'''

Do automatic or manual cars have better miles per gallon?



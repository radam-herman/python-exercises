# 4.9_seaborn_exercises.py

# note: Use the iris database to answer the following quesitons


# Exercise 1 - What does the distribution of petal lengths look like?

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns

iris_set = sns.load_dataset('iris')

iris_set.dtypes

iris_set.head()

iris_set.tail()

# Is there a correlation between petal length and petal width?

sns.relplot(x='petal_length', y='petal_width', data=iris_set)

# With color - selected species
# pedal length vs width alternate

sns.relplot(x='petal_length', y='petal_width', hue='species', data=iris_set)

# === sepal differences ====

sns.relplot(x='sepal_length', y='sepal_width', hue='species', data=iris_set)

# === box plots of iris set

iris_set.dtypes

plt.figure(figsize=(12, 10))
plt.suptitle('Boxplots with Seaborn')

plt.subplot(221)
sns.boxplot(data=iris_set, y='sepal_length')
plt.title('sepal_length')

plt.subplot(222)
sns.boxplot(data=iris_set, y='sepal_width')
plt.title('sepal_width')

plt.subplot(223)
sns.boxplot(data=iris_set, y='petal_length')
plt.title('petal_length')

plt.subplot(224)
sns.boxplot(data=iris_set, y='petal_width')
plt.title('petal_width')

plt.subplots_adjust(hspace=0.4)

# === distribution example

sns.distplot(iris_set.sepal_length)

sns.distplot(iris_set.sepal_width)

sns.distplot(iris_set.petal_length)

sns.distplot(iris_set.petal_width)

# Would it be reasonable to predict species based on sepal width and sepal length?
# -- Given the more distinct partition for the characteristics, 
# it appears reasonable to be able to predict species.

# Which features would be best used to predict species?
# -- petal length and width seem best for predicting the species

# Exercise 2 - 
# - Using the lesson as an example, use seaborn's load_dataset function to load 
# the anscombe data set. 
# - Use pandas to group the data by the dataset column, 
# and calculate summary statistics for each dataset.
# 
#  What do you notice?
# Plot the x and y values from the anscombe data. Each dataset should be 
# in a separate column.

anscombe_set = sns.load_dataset('anscombe')

anscombe_set.dtypes

anscombe_set.head(4)

anscombe_set.tail(4)

import pandas as pd
import numpy as np

sns.relplot(x='x', y='y', hue='dataset', data=anscombe_set)


set_0 = pd.DataFrame(anscombe_set)

type(set_0)

set_0.info()

set_0.describe()

set_0.dtypes

set_0.shape

set_0.columns

set_0.index

# -- BUILDING THE SETS 
## actually had each category with it's own set...
#### not necessary as below will show with groupby

set_0.groupby('dataset').describe()

sns.relplot(x='x', y='y', col='dataset', data=set_0)

### tryng to distinguish between plots
  ### using shape
sns.relplot(x='x', y='y', style='dataset', data=set_0)


  ### using color
sns.relplot(x='x', y='y', style='dataset', hue='dataset', data=set_0)


sns.pairplot(set_0)

# !pip install pydataset
# had problems - fixed - there were two Python installs

#  INSECT SPRAY SET 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns

from pydataset import data
insect_spray = data('InsectSprays')

insect_spray.head()

# -- READING SHOWING DOCUMENTATION
data("InsectSprays", show_doc=True)

insect_spray.groupby('spray').describe()

#  -- BOX PLOTS ---
plt.figure(figsize=(12, 10))  # this makes it larger than default
sns.boxplot(data=insect_spray, y='count', x='spray')

# -- Load the swiss dataset and read it's documentation. 
# Create visualizations to answer the following questions:

from pydataset import data
swiss_set = data('swiss')

data("swiss", show_doc=True)

swiss_set.head()

# Create an attribute named is_catholic that holds a boolean 
    # value of whether or not the province is Catholic. 
    #        (Choose a cutoff point
    # for what constitutes catholic)
                # df['passing_math'] = df.math > 70  from 
                # https://ds.codeup.com/4-python/7.4.3-dataframes/

swiss_set.describe()

swiss_set['is_catholic'] = swiss_set.Catholic > 42

swiss_set.head()

swiss_set.shape

type(swiss_set)

# Does whether or not a province is Catholic influence fertility?

sns.boxplot(data=swiss_set, y='Fertility', x='is_catholic')

## Using the chipotle dataset from the previous exercise, create 
# a bar chart that shows the 4 most popular items and the revenue 
# produced by each.




## -- Load the sleepstudy data and read it's documentation. 
# -- Use seaborn to create a line chart of all the individual subject's 
# reaction times
# and a more prominant line showing the average change in reaction time.

from pydataset import data
sleep_set = data('sleepstudy')

# sleep_set.describe
# data("sleepstudy", show_doc=True)

sleep_set.head(10)

sleep_set.groupby('Days').describe()

# sleep_set['daily_mean'] = sleep_set.groupby('Days').mean()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns

plt.figure(figsize=(12, 10))  # this makes it larger than default
sns.relplot(x='Days', y='Reaction', data=sleep_set)
plt.title('Sleep Dep Reaction Time by Days')
plt.xlabel('Days')
plt.ylabel('Reaction Time (ms)')

# --- Distribution glance

sns.distplot(sleep_set.Reaction)


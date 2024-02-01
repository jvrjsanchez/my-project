# imports
import builtins
import datetime as dt
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

#plot config
sns.set_style(style='whitegrid')
#%matplotlib qt5

#%% builtin instances
str1 = "hello world"
int1 = 1
float1 = 3.14
bool1 = True
list1 = ['Hello', 'Hello', 1, 3.14, True]
tuple1 = ('Hello', 'Hello', 1, 3.14, True)
se1t1 = {'Hello', 'Hello', 1, 3.14, True}
dict1 = {'r': 'red', 'g': 'green', 'b': 'blue'}

# standard modules
datetime1 = dt.datetime.now()
timedelta1 = dt.timedelta(days=0)

# scientific libraries
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])
xy = np.array([[1,2],
               [2,4],
               [3,6],
               [4,8],
               [5,10]])

dict2 = {'x': np.array([1, 2, 3, 4, 5]),
         'y': np.array([2, 4, 6, 8, 10])}
dataFrame1 = pd.DataFrame(data= {'x': np.array([1, 2, 3, 4, 5]),
                                 'y': np.array([2, 4, 6, 8, 10])})

#plotting
plt.plot(x,y)
plt.show()


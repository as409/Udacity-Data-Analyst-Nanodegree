
# coding: utf-8

# In[3]:

import pandas as pd
data = pd.read_csv('~/Desktop/dand/chopstick-effectiveness.csv')
data


# In[5]:

newtable=data.groupby('Chopstick.Length')['Food.Pinching.Efficiency'].mean().reset_index()
newtable


# In[7]:

get_ipython().magic(u'pylab inline')
from matplotlib import pyplot as plt
plt.scatter(x=newtable['Chopstick.Length'], y=newtable['Food.Pinching.Efficiency'])
plt.xlabel('length in mm')
plt.ylabel('efficiency')
plt.title('chopsticks')
plt.show()


# In[ ]:




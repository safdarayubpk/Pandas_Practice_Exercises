#!/usr/bin/env python
# coding: utf-8

# # Practice Assignment :: 01_	PIAIC91502

# ## How to import pandas and check the version?

# In[22]:


import pandas as pd


# In[23]:


pd.__version__


# ## import useful libraries

# In[4]:


import numpy as np


# In[5]:


import matplotlib.pyplot as plt


# ## How to create a series from a list, numpy array and dict?

# In[6]:


# Creat a series from a list
list_1 = ['safdar','gohar','khawar']
a = pd.Series(list_1)
a


# In[9]:


# Create a series from numpy array
arr = np.arange(11,22,2)
b = pd.Series(arr)
b


# In[12]:


# Create a series from dict

dic = {'Fruite':['apple','banana','grape'],'Shop':['shop1','shop2','shop3']}
c = pd.Series(dic)
display(c)

di = {'Name':'safdar','Age':34,'City':'kohat'}
d = pd.Series(di)
display(d)


# ## How to convert the index of a series into a column of a dataframe?

# ## hint::
# ### Convert the series ser into a dataframe with its index as another column on the dataframe.

# In[3]:


fruite = pd.Series(['apple','grape','banana'])
fruite


# In[10]:


df =fruite.to_frame()
df


# In[11]:


df =fruite.to_frame().reset_index()
df


# # How to combine many series to form a dataframe?

# In[13]:


city = pd.Series(['kohat','peshawar'], index=['a','b'], name= 'Cities_names')
country = pd.Series(['Pakistan','Afghanistan'], index=['a','b'], name='Country_names')
city


# In[14]:



country


# In[17]:


pd.concat([city,country],axis=1)


# # How to calculate the number of characters in each word in a series?

# In[20]:


languages = pd.Series(['English','Spanish','Urdu'])
print('Languages ')
languages


# In[22]:


count = languages.map(lambda x: len(x))
print('Length of words in all languages names')
count


# # How to filter valid emails from a series?

# ## Desired Output::
# 1    rameses@egypt.com
# 
# 2            matt@t.com
# 
# 3    narendra@modi.com
# 

# In[15]:


emails = pd.Series(['rameses@egypt.com', 'matt@t.co', 'narendra@modi.com'])
pattern ='[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,4}'


# In[16]:


import re
pattern ='[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,4}'
mask = emails.map(lambda x: bool(re.match(pattern, x)))
emails[mask]

emails.str.findall(pattern, flags=re.IGNORECASE)


# # How to replace missing spaces in a string with the least frequent character?

# ## Input::
# ###  my_str = 'dbc deb abed gade'
# ## Desired Output::
# ### 'dbccdebcabedcgade'  # least frequent is 'c'

# In[4]:


my_str = 'dbc deb abed gade'
print("Original series:")
print(my_str)
ser = pd.Series(list(my_str))
element_freq = ser.value_counts()
print(element_freq)
current_freq = element_freq.dropna().index[-1]
result = "".join(ser.replace(' ', current_freq))
print(result)


# # How to swap two rows of a dataframe?

# In[6]:


df = pd.DataFrame(['safdar','gohar'])
display(df)

df.reindex([1,0])


# # How to get the positions where values of two columns match?

# In[18]:


df = pd.DataFrame({'city_1': np.random.choice(['kohat','multan','peshawar'], 8),
                   'city_2': np.random.choice(['kohat','multan','peshawar'], 8) })
display(df)
match_positions = df.index[df.city_1 == df.city_2].tolist()
display(match_positions)


# # How to replace both the diagonals of dataframe with 0?

# In[23]:


df = pd.DataFrame(np.random.randint(1,100,100).reshape(10, -1))

diagonals_0 = df.where(df.values != np.diag(df),0,df.where(df.values != np.flipud(df).diagonal(0),0,inplace=True))

diagonals_0


# # How to get the particular group of a groupby dataframe by key?

# ### This is a question related to understanding of grouped dataframe.

# In[21]:


df = pd.DataFrame({'col1': ['kohat', 'peshawar', 'multan'] * 3,
                   'col2': np.random.rand(9),
                   'col3': np.random.randint(0, 15, 9)})

df_grouped = df.groupby(['col1'])

display(df)
display(df_grouped.get_group('kohat'))


# # Which column contains the highest number of row-wise maximum values?

# ### Obtain the column name with the highest number of row-wise maximum’s in df.

# In[29]:


data = {'Name' : ['safdar', 'joseph', 'samina'],'AI' : [85, 75, 95],'CNC' : [35, 45, 13],'IOT' : [71, 61, 99]}

frame = pd.DataFrame(data)
display(frame)
frame['HighScore'] = frame[['AI','CNC','IOT']].max(axis=1)
display(frame)


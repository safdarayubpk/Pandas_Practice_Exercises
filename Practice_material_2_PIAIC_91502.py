#!/usr/bin/env python
# coding: utf-8

# # Roll NO.__PIAIC_91502
# 
# # Download dataset form  this website
# 
# ## https://www.kaggle.com/faressayah/stanford-open-policing-project?select=police_project.csv

# ## Description::

# On a typical day in the United States, police officers make more than 50,000 traffic stops. Our team is gathering, analyzing, and releasing records from millions of traffic stops by law enforcement agencies across the country. Our goal is to help researchers, journalists, and policymakers investigate and improve interactions between police and the public.
# 

# ## Importing libraries::

# In[21]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# # Use Pandas' read_csv function  open it as a DataFrame

# In[3]:


df = pd.read_csv('police_project.csv')
df


# # What does each row represent?
# 
# #### hint::
# head : Return the first n rows. (By default return first 5 rows.)

# In[4]:


df.head()


# # How to get the basic statistics of all the columns?

# In[5]:


df.describe()


# # How to check the shape of dataset?

# In[7]:


df.shape


# # Check the type of columns?

# In[8]:


df.dtypes


# # Locating missing Values?
# #### detecting missing values
# #### calculates the sum of each column
# 

# In[10]:


print("Detecting missing values")
display(df.isnull().values.any())


# In[12]:


display("calculates the sum of each column")
n_missings_each_col = df.apply(lambda x: x.isnull().sum())
n_missings_each_col.argmax()


# # Dropping Column that only contains missing values.

# In[13]:


df.dropna(axis=1)


# # Do the men or women speed more often?

# In[22]:


sns.catplot('driver_gender', data=df, kind="count", height=7)


# # Which year had the least number of stops?

# In[42]:


df.head()


# In[26]:


print(df.stop_date.dtype)
print(df.stop_time.dtype)


# In[27]:


df.stop_date


# In[28]:


df['stop_date'] = pd.to_datetime(df.stop_date, format="%Y-%M-%d")
df["year"] = df.stop_date.dt.year
df.dtypes


# In[29]:


df.year.value_counts()


# In[30]:


plt.figure(figsize=(12, 8))
df.year.value_counts().plot(kind="bar")


# # Does gender affect who gets searched during a stop?

# In[38]:


df.search_conducted.value_counts()


# In[39]:


df.loc[df.search_conducted, 'driver_gender'].value_counts()


# In[40]:


df.groupby(['violation', 'driver_gender']).search_conducted.mean()


# In[41]:


plt.figure(figsize=(12, 12))

plt.subplot(2, 2, 1)
df.search_conducted.value_counts().plot(kind="bar")
plt.title("Searched Cases")

plt.subplot(2, 2, 2)
df.loc[df.search_conducted, 'driver_gender'].value_counts().plot(kind="bar")
plt.title("Searched Men and Women")

plt.subplot(2, 2, 3)
df.groupby(['violation', 'driver_gender']).search_conducted.mean().plot(kind="bar")


# 
# # How does drug activity change by time of day?

# In[31]:


df.columns


# In[32]:


df.drugs_related_stop.value_counts()


# In[33]:


df["stop_time"] = pd.to_datetime(df.stop_time, format="%H:%M").dt.hour
df.head()


# In[34]:


df.loc[df.sort_values(by="stop_time").drugs_related_stop, 'stop_time'].value_counts()


# In[35]:


plt.figure(figsize=(12, 12))

plt.subplot(2, 2, 1)
df.loc[df.sort_values(by="stop_time").drugs_related_stop, 'stop_time'].value_counts().sort_index().plot(kind="bar")

plt.subplot(2, 2, 2)
df.loc[df.sort_values(by="stop_time").drugs_related_stop, 'stop_time'].value_counts().sort_index().plot()


# # Do most stops occur at night?

# In[36]:


df.stop_time.sort_index().value_counts().sort_index()


# In[37]:


plt.figure(figsize=(12, 12))

plt.subplot(2, 2, 1)
df.stop_time.sort_index().value_counts().sort_index().plot()

plt.subplot(2, 2, 2)
df.stop_time.sort_index().value_counts().sort_index().plot(kind="bar")


# 

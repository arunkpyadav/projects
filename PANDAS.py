#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd


# In[5]:


1# panda stands for panel data and is the core library
2# for data manipulation and data analysis.
3# it consist single dimensional and multidimensional data structure
4# single dimensional data structure called as series object
5# multi dimensional data structure called as data frame.



# In[6]:


# series object is one dimensional labeled array

s1=pd.Series([1,2,3,4,5])


# In[7]:


s1


# In[8]:


type(s1)


# In[9]:


#CHANGING INDEX VALUE


# In[10]:


s2=pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])


# In[11]:


s2


# In[ ]:


#creating series objecct from dictionary


# In[12]:


s3=pd.Series({'k1':20,'k2':30,'k3':40})


# In[13]:


s3


# In[18]:


#changing index value position with dictionery


# In[19]:


s3=pd.Series({'k1':20,'k2':30,'k3':40},index=['k2','k3','k1','d'])


# In[20]:


s3


# In[ ]:


#extracting individual element


# In[22]:


s4=pd.Series([1,2,3,4,5])


# In[23]:


s4[4] #extracting 


# In[24]:


s4+5


# In[25]:


s4*3


# In[26]:


#PANDAS DATAFRAME
#DATA DRAME IS 2 DIMENSIONAL LABELLED DATA STRUCTURE
#A DATA FRAME COMPRISES OF ROWS AND COLUMNS


# In[27]:


d1=pd.DataFrame({'Name':['Arun','vedant','rahul'],'marks':[95,3,88]})


# In[28]:


d1


# In[31]:


#READ CSV FILE AND EXTRACTING DATA


iris=pd.read_csv('iris.csv')


# In[32]:


iris.head()


# In[33]:


iris.tail()


# In[34]:


iris.shape


# In[35]:


iris.describe()


# In[40]:


# iloc method in pandas


# In[44]:


iris.iloc[5:11,2:]   #iloc method


# In[ ]:


# LOCK METHOD


# In[47]:


iris.loc[5:11,('PetalLengthCm','PetalWidthCm','Species')]


# In[52]:


iris.drop([2,3],axis=0)


# In[57]:


iris.min


# In[58]:


iris.median


# In[59]:


#half method
def double_make(s):
    return s*2


# In[63]:


iris.head()


# In[62]:


iris['PetalLengthCm'].apply(double_make)


# In[65]:


iris['Species'].value_counts()


# In[68]:


iris.sort_values(by='PetalWidthCm')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





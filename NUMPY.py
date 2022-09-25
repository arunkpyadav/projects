#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[ ]:


#single dimension Array

#multi dimensional Array


# In[3]:


n1=np.array([1,2,3,4,5,6])


# In[4]:


n1


# In[5]:


type(n1)  #nd.array means numpy dimensional 
array


# In[11]:


n2=np.array([[2,3,4,54,5],[34,45,65,43,45]])  #miltidimensional array


# In[12]:


n2


# In[13]:


type(n2)


# In[ ]:


#Numpy with zeros
   
  
   


# In[14]:


n3=np.zeros((2,2))


# In[15]:


n3


# In[17]:


n4=np.zeros((5,5))


# In[18]:


n4


# In[19]:


n5=np.full((3,3),55)


# In[20]:


n5


# In[23]:


np.arange(1,30,5)


# In[42]:


n6=np.random.randint(20,200)  #np.random.randint it will give random number between values


# In[43]:


n6


# In[62]:


n7=np.array([[1,2,3,4,5],[2,3,4,5,6]])


# In[63]:


n7


# In[64]:


n7.shape = (5,2) #changing shape using .shape method


# In[65]:


n7


# In[66]:


#vstack   hstack columnstack of numpy


# In[71]:


n8=np.array([1,2,3,4])
n9=np.array([5,6,7,8])


# In[74]:


s=np.vstack((n8,n9))


# In[75]:


s


# In[76]:


np.hstack((n8,n9))


# In[77]:


np.column_stack((n8,n9))


# In[81]:


n10=np.array([1,20,30,40])


# In[84]:


n11=([50,60,70,1,20])


# In[85]:


np.intersect1d(n10,n11)


# In[86]:


np.setdiff1d(n10,n11)


# In[90]:


s2=np.sum([n8,n9])


# In[91]:


s2


# In[92]:


s3=np.sum([n8,n9],axis=0)


# In[95]:


#NUMPY MATHEMATICS
n8+1


# In[96]:


n8*2


# In[97]:


#NUMPY MATH FUNCTIONS MEAN,STANDARD DEVIATION,Median
np.mean(n8)


# In[98]:


np.median(n8)


# In[99]:


np.std(n8)


# In[100]:


# NUMPY SAVE & LOAD
np.save('my_numpy',n8)


# In[101]:


np.load('my_numpy.npy')


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Matplotlib is a python library used for data visualization
#You can create bar-plots, scatter-plots, histograms and a lot 
#more with matplotlib


# In[2]:


import numpy as np
from matplotlib import pyplot as plt


# In[3]:


x=np.arange(1,15)


# In[4]:


y=2*x


# In[5]:


plt.plot(x,y,color='r',linestyle=':',linewidth=5)
plt.title('x vs y')
plt.xlabel('This is x axis')
plt.ylabel('This is y axis')


# In[6]:


x


# In[7]:


y1=2*x


# In[8]:


y2=4*x


# In[19]:


plt.plot(x,y1,color='b',linestyle='-',linewidth=3)
plt.plot(x,y2,color='g',linestyle=':',linewidth=3)
plt.title('x vs y1 & y2')
plt.xlabel('This is x axis')
plt.ylabel('This is y axis')


# In[20]:


#with subplot that is two chart in single screen


# In[28]:


plt.subplot(2,1,1)
plt.plot(x,y1,color='b',linestyle='-',linewidth=4)

plt.subplot(2,1,2)
plt.plot(x,y2,color='g',linestyle=':',linewidth=4)
plt.title('x vs y1 & y2')
plt.xlabel('This is x axis')
plt.ylabel('This is y axis')
plt.grid(True)


# In[30]:


student={'Arun':88,'Rahul':76,'vedant':95}


# In[31]:


Name=list(student.keys())


# In[32]:


marks=list(student.values())


# In[41]:


#plotting bar chart with dictionary

plt.bar(Name,marks,color='r')
plt.title('Names vs Marks')
plt.xlabel('Name of the students')
plt.ylabel('Marks of the students')
plt.show()


# In[42]:


#bar chart in horizontal view


plt.barh(Name,marks,color='b')
plt.title('Names vs Marks')
plt.xlabel('Name of the students')
plt.ylabel('Marks of the students')
plt.show()


# In[50]:


a=(2,3,4,5,7,6,8,9,4)


# In[51]:


b=[2,3,4,6,4,5,7,8,5]


# In[60]:


plt.scatter(a,b,marker='*',color='r',s=150)
plt.show()


# In[61]:


c=(3,7,9,5,8,3,6,7,8)


# In[63]:


plt.scatter(a,b,color='g',s=200)
plt.scatter(a,c,marker='*',color='y',s=200)
plt.show()


# In[66]:


plt.subplot(1,2,1)
plt.scatter(a,b,color='g',s=200)
plt.subplot(1,2,2)
plt.scatter(a,c,marker='*',color='y',s=200)
plt.show()


# In[67]:


data= [1,3,3,3,3,4,5,6,6,6,5,5,7,8,5,9]


# In[72]:


plt.hist(data,color='r')
plt.show()


# In[75]:


import pandas as pd
iris=pd.read_csv('iris.csv')


# In[78]:


iris.head()


# In[89]:


#histogram with iris data set

plt.hist(['PetalLengthCm',],color='g')


# In[92]:


#boxplot 
one=[1,2,3,4,5,6,7,8,9]
two=[1,2,3,4,5,4,3,2,1]
three=[3,4,5,6,7,8,6,5,4]
data=list([one,two,three])


# In[95]:


plt.boxplot(data)
plt.show()


# In[96]:


plt.violinplot(data)
plt.show()


# In[98]:


#pie chart with matplot library

fruit=['apple','orange','mango','banana']
price=[200,300,250,350]


# In[104]:


plt.pie(price,labels=fruit,autopct='%0.1f%%')
plt.show()


# In[109]:


plt.pie(price,labels=fruit,radius=3)
plt.pie([1],colors='w',radius=1.5)
plt.show()


# In[ ]:





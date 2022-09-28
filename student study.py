#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd

import matplotlib.pyplot as plt


# In[23]:


math=pd.read_csv('maths.csv')


# In[24]:


math.head()


# In[6]:


math.shape


# In[7]:


math.describe()


# In[8]:


math['age'].value_counts()


# In[9]:


#Age group for study
plt.figure(figsize=(8,5))
plt.bar(math['age'].value_counts().keys(),math['age'].value_counts())


# In[10]:


#occupation
math['Fjob'].value_counts()


# In[11]:


plt.pie(math['Fjob'].value_counts(),labels=math['Fjob'].value_counts().keys(),autopct='%0.1f%%')
plt.show()


# In[12]:


math['Mjob'].value_counts()


# In[13]:


plt.pie(math['Mjob'].value_counts(),labels=math['Mjob'].value_counts().keys(),autopct='%0.1f%%')
plt.show()


# In[14]:


#Determining gender of the students
math['sex'].value_counts()


# In[15]:


plt.bar(math['sex'].value_counts().keys(),math['sex'].value_counts())
plt.title('GENDER VS NUMBER OF STUDENTS')
plt.xlabel('GENDER')
plt.ylabel('NUMBER OF THE STUDENT')
plt.show()


# In[16]:


#school counts
math['school'].value_counts()


# In[17]:


plt.bar(math['school'].value_counts().keys(),math['school'].value_counts())
plt.show()


# In[18]:


math['school']==math['sex']


# In[19]:


math['address'].value_counts()


# In[21]:


plt.pie(math['address'].value_counts(),labels=math['address'].value_counts().keys(),autopct='%0.1f%%')


# In[22]:


math['absences'].value_counts()


# In[ ]:





# In[ ]:





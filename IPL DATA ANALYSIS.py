#!/usr/bin/env python
# coding: utf-8

# In[22]:


import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt


# In[25]:


ipl=pd.read_csv('matches.csv')


# In[26]:


ipl.head()


# In[27]:


ipl.shape


# In[29]:


#player of the match 
ipl['player_of_match'].value_counts()


# In[33]:


#top 10 player of the match 
ipl['player_of_match'].value_counts()[0:10]


# In[34]:


#top 10 player of the match 
ipl['player_of_match'].value_counts()[0:10].keys()


# In[35]:


list(ipl['player_of_match'].value_counts()[0:10])


# In[36]:


list(ipl['player_of_match'].value_counts()[0:10].keys())


# In[45]:


plt.figure(figsize=(15,10))
plt.bar(list(ipl['player_of_match'].value_counts()[0:10].keys()),list(ipl['player_of_match'].value_counts()[0:10]))
plt.show()


# In[48]:


ipl["result"].value_counts()


# In[49]:


ipl['toss_winner'].value_counts()


# In[51]:


list(ipl['toss_winner'].value_counts())


# In[52]:


list(ipl['toss_winner'].value_counts().keys())


# In[68]:


plt.figure(figsize=(50,20))
plt.bar(list(ipl['toss_winner'].value_counts().keys()),list(ipl['toss_winner'].value_counts()),color='g')


# In[64]:


batting_first=ipl[ipl['win_by_runs']!=0]


# In[65]:


batting_first.head()


# In[67]:


plt.figure(figsize=(10,5))
plt.hist(batting_first['win_by_runs'])


# In[69]:


batting_first['winner'].value_counts()


# In[84]:


list(batting_first['winner'].value_counts()[0:5])


# In[75]:


list(batting_first['winner'].value_counts()[0:5].keys())


# In[83]:


plt.figure(figsize=(20,10))
plt.bar(list(batting_first['winner'].value_counts()[0:5].keys()),list(batting_first['winner'].value_counts()[0:5]),color='r')
plt.title('winner by batting first')


# In[87]:


plt.figure(figsize=(10,5))
plt.pie(list(batting_first['winner'].value_counts()[0:5]),labels=list(batting_first['winner'].value_counts()[0:5].keys()),autopct='%0.1f%%')
plt.show()


# In[90]:


batting_second=ipl[ipl['win_by_wickets']!=0]


# In[91]:


batting_second.head()


# In[93]:


batting_second['winner'].value_counts()


# In[95]:


list(batting_second['winner'].value_counts()[0:5])


# In[97]:


list(batting_second['winner'].value_counts()[0:5].keys())


# In[100]:


plt.figure(figsize=(15,10))
plt.bar(list(batting_second['winner'].value_counts()[0:5].keys()),list(batting_second['winner'].value_counts()[0:5]))


# In[108]:


plt.figure(figsize=(15,5))
plt.bar(list(batting_second['winner'].value_counts()[0:5].keys()),list(batting_second['winner'].value_counts()[0:5]))


# In[117]:


plt.figure(figsize=(10,7))
plt.pie(list(batting_second['winner'].value_counts()[0:8]),labels=list(batting_second['winner'].value_counts()[0:8].keys()),autopct='%0.1f%%')
plt.show()


# In[118]:


ipl.head()


# In[119]:


ipl['season'].value_counts()


# In[120]:


ipl['city'].value_counts()


# In[121]:


ipl['toss_winner'].value_counts()


# In[122]:


np.sum(ipl['toss_winner']==ipl['winner'])


# In[ ]:





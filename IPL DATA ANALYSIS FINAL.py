#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns


# In[3]:


ipl=pd.read_csv('matches.csv')


# In[4]:


#printing first 5 records of the match
ipl.head()


# In[5]:


#printing winner with thier win number of matches.
ipl['winner'].value_counts()


# In[6]:


ipl.shape


# In[7]:


list(ipl['winner'].value_counts())


# In[8]:


ipl['player_of_match'].value_counts()[0:10]
ipl['player_of_match'].value_counts()[0:10].keys()


# In[9]:


#top 10 player of the match
list(ipl['player_of_match'].value_counts()[0:10])


# In[10]:


list(ipl['player_of_match'].value_counts()[0:10].keys())


# In[11]:


#printing bar chart for player of the matches with respect to their number of win
plt.figure(figsize=(30,20))
plt.bar(list(ipl['player_of_match'].value_counts()[0:10].keys()),list(ipl['player_of_match'].value_counts()[0:10]),color='blue')
plt.title('PLAYER OF THE MATCH VS NO OF WIN ')
plt.xlabel('player Name')
plt.ylabel('No. of win')

plt.show()


# In[12]:


plt.pie(ipl['player_of_match'].value_counts()[0:10],labels=ipl['player_of_match'].value_counts()[0:10].keys(),autopct='%0.1f%%')
plt.show()


# In[15]:


#how many matches are done at one stadium.
ipl['venue'].value_counts()


# In[16]:


list(ipl['winner'].value_counts().keys())


# In[17]:


plt.figure(figsize=(20,20))
plt.pie(list(ipl['winner'].value_counts()),labels=list(ipl['winner'].value_counts().keys()),autopct='%0.1f%%')
plt.show()


# In[18]:


ipl['toss_winner'].value_counts()


# In[19]:


plt.figure(figsize=(40,30))
plt.bar(ipl['toss_winner'].value_counts().keys(),ipl['toss_winner'].value_counts())
plt.show()


# In[20]:


plt.figure(figsize=(20,20))
plt.pie(ipl['toss_winner'].value_counts(),labels=ipl['toss_winner'].value_counts().keys(),autopct='%0.1f%%')
plt.show()


# In[21]:


a=ipl['winner']==ipl['toss_winner']


# In[22]:


#True values will be toss winner == match winner
#false values will be toss winner != match winner
a.value_counts()


# In[23]:


#Total matches
a.count()


# In[24]:


b=ipl['winner']==ipl['toss_winner']


# In[25]:


b.value_counts()


# In[26]:


batting_first=ipl[ipl['win_by_runs']!=0]


# In[27]:


batting_first.head()


# In[43]:


batting_first['winner'].value_counts()


# In[49]:


plt.figure(figsize=(30,30))
plt.pie(batting_first['winner'].value_counts(),labels=batting_first['winner'].value_counts().keys(),autopct='%0.1f%%')
plt.show()


# In[50]:


a=ipl['result'].value_counts()


# In[51]:


b=ipl['result'].value_counts().keys()


# In[48]:


plt.figure(figsize=(10,7))
plt.bar(b,a)
plt.show()


# In[52]:


ipl.head()


# In[57]:


batting_second=ipl[ipl['win_by_wickets']!=0]


# In[69]:


#teams win in second innings
batting_second['winner'].value_counts()


# In[70]:


batting_second['winner'].value_counts().keys()


# In[75]:


plt.figure(figsize=(20,20))
plt.pie(batting_second['winner'].value_counts(),labels=batting_second['winner'].value_counts().keys(),autopct='%0.1f%%')
plt.show()


# In[81]:


dl=ipl['dl_applied']==1


# In[82]:


dl.value_counts()


# In[87]:


#Number of the matches of the played in the cities 
ipl['city'].value_counts()


# In[88]:


ipl['season'].value_counts()


# In[90]:


ipl['season'].value_counts().keys()


# In[96]:


#bar chart for how many matches played in a season
plt.bar(ipl['season'].value_counts().keys(),ipl['season'].value_counts())


# In[97]:


ipl.head()


# In[99]:


ipl['toss_decision'].value_counts()


# In[104]:


#toss winner will win match ---checking possibility
toss=ipl['winner']==ipl['toss_winner']


# In[105]:


toss.value_counts()


# In[112]:


#51.92 percentage chances are if u win toss u can win match as well
(392/755)*100


# In[114]:


ipl['toss_decision'].value_counts()


# In[ ]:





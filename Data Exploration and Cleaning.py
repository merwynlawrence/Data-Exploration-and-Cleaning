#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd

data = pd.read_csv("new_york_tree_census_2015.csv")
data


# In[8]:


pd.set_option('display.max_columns', None) #set maximum columns to be displayed to make all coulmns readable
data


# In[9]:


data.columns


# In[73]:


data_subset = data[['tree_id', 'tree_dbh', 'stump_diam',
                  'curb_loc', 'status', 'health', 'spc_latin', 'steward','sidewalk', 'problems', 'root_stone',
                  'root_grate', 'root_other', 'trunk_wire', 'trnk_light', 'trnk_other','brch_light', 'brch_shoe', 'brch_other']]

# take a subset of data with required columns into anew dataset


# In[74]:


data_subset.isna().sum() #find missing values


# In[75]:


data_subset[data_subset['health'].isna()] # shows the data with health column having missing values


# In[76]:


data_subset.describe()


# In[77]:


# output shows we have only 3 coulms with numeric variables others are categorical
   #including diameter of tree and diameter of stump


# In[78]:


data_subset.dtypes


# In[79]:


data_subset.hist(bins=60, figsize = (20,10) )


# In[80]:


#stump diameter shows that most values are around 0 
#but singe the graph max value on x axis is 140 this indicates an entry around that range
#similarly for tree_dbh the max value is around 400
#this needs to be further checked


# In[81]:


big_trees = data_subset[data_subset['tree_dbh']>50]


# In[82]:


big_trees[['tree_id', 'tree_dbh']].plot(kind='scatter', x='tree_id', y='tree_dbh', figsize=(20,10))


# In[83]:


big_trees = data_subset[data_subset['stump_diam']>50]

big_trees[['tree_id', 'stump_diam']].plot(kind='scatter', x='tree_id', y='stump_diam', figsize=(20,10))


# In[84]:


pd.DataFrame(data_subset['spc_latin'].value_counts()).plot(kind='bar', figsize=(20,10))
# shows a bar chart witht he most common trees in decending


# In[85]:


data_subset['steward'].value_counts() # to check the categorical values 


# In[86]:


data_subset['curb_loc'].value_counts() #shows us the categorical values


# In[87]:


dead = data_subset[data_subset['status'] == 'Dead'] # to find the trees with status Dead
dead


# In[88]:


stumps = data_subset[data_subset['status'] == 'Stump'] # to find the trees with status Stump


# In[89]:


stumps


# In[90]:


# by lookin  at the above two results we can assume that the trees with status stump and dead have the missing information in coulmns
#status	health	spc_latin	spc_common	steward	sidewalk	problems
#ie the information hasnt been recoded


# In[91]:


mask = ((data_subset['status'] == 'Stump') | (data_subset['status'] == 'Dead'))
#data_subset.fillna('not applicable')


# In[92]:


data_subset.loc[mask ] = data_subset.loc[mask].fillna('not applicable') 
   
#     #Fill missing values to non applicable 
#     #These columns were vereefied in the code data_subset.isna().sum()
#     #tree_id           0
# #block_id          0
# #created_at        0
# tree_dbh          0
# stump_diam        0
# curb_loc          0
# status            0
# health        31616
# spc_latin     31619
# spc_common    31619
# steward       31615
# sidewalk      31616
# problems      31664
# root_stone        0
# root_grate        0
# root_other        0
# trunk_wire        0
# trnk_light        0
# trnk_other        0
# brch_light        0
# brch_shoe         0
# brch_other        0


# In[93]:


data_subset[data_subset['status']=='Stump']


# In[94]:


data_subset.isna().sum()


# In[95]:


data_subset.isna().sum()


# In[96]:


data_subset[data_subset['problems'].isna()]


# In[97]:


#fill missing values with below 
data_subset['problems'].fillna('None', inplace=True)
data_subset['health'].fillna('Good', inplace=True)
data_subset['spc_latin'].fillna('No Observation', inplace=True)
data_subset['sidewalk'].fillna('NoDamage', inplace=True)


# In[98]:


data_subset.head(20)


# In[99]:


data_subset['sidewalk'].value_counts()


# In[100]:


data_subset.isna().sum()


# In[101]:


#we finally have removed the missing values from the dataset


# In[106]:


data_subset_new = data_subset[(data_subset['tree_dbh']<=60) | (data_subset['stump_diam']<=60)]
data_subset_new


# In[108]:


data_subset_alive = data_subset_new[data_subset_new['status']=='Alive']


# In[112]:


data_subset_alive


# In[109]:


data_subset_dead_or_stump = data_subset_new[(data_subset_new['status']=='Dead') | (data_subset_new['status']=='Stump')]


# In[110]:


data_subset_dead_or_stump


# In[ ]:





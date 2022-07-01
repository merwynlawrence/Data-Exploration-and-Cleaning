#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[5]:


titanic = pd.read_csv('titanic_train.csv') #read a csv %%file


# In[4]:





# In[6]:


type(titanic) #find the datatype 


# In[7]:


type(titanic['Name']) #find the datatype of a column


# In[8]:


titanic.loc[4] #fetch the rows by row number


# In[10]:


#filtering the dataset
#eg find all passengers whose age is greater than 30
titanic[titanic['Age']>30]


# In[12]:


# find passenger with age >30 and who paid fare >30
titanic[(titanic['Age']>30)  & (titanic['Fare'] > 30)]


# In[14]:


# find * whereclass of cabin is 1 or 3

titanic[titanic['Pclass'].isin(['1','3'])]
#or


# In[15]:


titanic[~titanic['Pclass'].isin(['1','3'])] # ~ not equal


# In[17]:


#Find the total fare paid by the family

titanic['total fare per family']= (titanic['SibSp'] + titanic['Parch']+1)* titanic['Fare']
titanic['total fare per family']


# In[18]:


titanic


# In[19]:


#change column names

titanic.rename(columns = { 'Fare' : 'Ticket Fee'})


# In[22]:


#reset the index

filtered_titanic  = titanic[titanic['Age'] == 30].reset_index(drop=True) # drip = true when you dont need the old index


# In[23]:


filtered_titanic


# In[24]:


# sorting the values

titanic.sort_values(by = 'Fare', ascending =False)


# In[25]:


# lower case
titanic['Name'].str.lower()


# In[30]:


# string search

titanic[titanic['Name'].str.contains("Will")].reset_index()


# In[31]:


# concat information / Add information
pd.concat([titanic, new_df])


# In[34]:


#merge two dfs

datatoadd = { "Pclass" :  [1,2,3], "Total Cabin Amount" : [350, 200, 100]}

extra_info = pd.DataFrame(columns = ['Pclass', 'Total Cabin Amount'], data = datatoadd)
extra_info


# In[35]:


titanic.merge(extra_info, how='left', on='Pclass')


# In[36]:


##Aggregations

titanic.describe()


# In[40]:


titanic['Age'].value_counts() #Find the distribution of passengers by age 


# In[ ]:





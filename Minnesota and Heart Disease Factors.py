#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


## reading the csv file into a pandas dataframe and then printing the first 10 results to visualize the data

df = pd.read_csv("C:\\Users\\16126\\Documents\\Data Engineering Project\\Behavioral_Risk_Factor_Data__Heart_Disease___Stroke_Prevention.csv")
df.head()


# In[3]:


## exploring the data

df.info()


# In[4]:


## dropping irrelevant columns

df.drop(['priorityarea1','priorityarea2','priorityarea3','priorityarea4','indicatorid', 'breakoutcategoryid', 'indicatorid', 'topicid', 'categoryid','datavaluefootnote','datavaluefootnotesymbol','confidencelimitlow', 'confidencelimithigh', 
         'datavalue','datavaluetype','datavalueunit','datasource','locationabr','breakoutid', 'locationid'], inplace=True, axis=1)


# In[5]:


## transposing the dataframe

df_t = df.T
print(df_t)


# In[6]:


df_t.reset_index()


# In[7]:


## checking for null values 

df_t.isnull().sum()


# In[8]:


## checking for duplicates 

df_t.duplicated()


# In[9]:


## checking the list of states that are present in the dataframe
df.locationdesc.value_counts().reset_index()


# In[10]:


df.indicator.value_counts().reset_index()


# In[11]:


## finding the top 10 indicators 

df.indicator.value_counts()[:10]


# In[12]:


## changing the names to be able to read easier

df['indicator'] = df['indicator'].replace(['Prevalence of current smoking among US adults (18+) (Percentage); BRFSS'],'Smoking')
df['indicator'] = df['indicator'].replace(['Prevalence of obesity among US adults (20+) (Percentage); BRFSS'],'Obesesity')
df['indicator'] = df['indicator'].replace(['Nutrition and Weight Status Objective 9: Prevalence of obesity among US adults (20+) (Percentage); BRFSS'],'Obese Adults')
df['indicator'] = df['indicator'].replace(['Nutrition and Weight Status Objective 8: Prevalence of healthy weight among US adults (20+) (Percentage); BRFSS'],'healthy adults')
df['indicator'] = df['indicator'].replace(['Prevalence of diabetes among US adults (18+) (Percentage); BRFSS'],'diabetes')
df['indicator'] = df['indicator'].replace(['Prevalence of physical inactivity among US adults (18+) (Percentage); BRFSS'],'physical actvity')
df['indicator'] = df['indicator'].replace(['Prevalence of high total cholesterol among US adults (20+) (Percentage); BRFSS'],'cholesterol')
df['indicator'] = df['indicator'].replace(['Heart Disease and Stroke Objective 6: Prevalence of cholesterol screening in the past 5 years among US adults (20+) (Percentage); BRFSS'],'cholesterol screening')
df['indicator'] = df['indicator'].replace(['Heart Disease and Stroke Objective 7: Prevalence of high total cholesterol among US adults (20+) (Percentage); BRFSS'],'high cholesterol')
df['indicator'] = df['indicator'].replace(['Prevalence of consuming fruits and vegetables <5 times per day among US adults (18+) (Percentage); BRFSS'],'fruits and veggies')


# In[13]:


df.indicator.value_counts()[:10].reset_index()


# In[14]:


## checking the category values

df.category.value_counts()[:10].reset_index()


# In[15]:


## checking the states that are included in the dataframe

df.locationdesc.value_counts().reset_index()


# In[16]:


## checking the values of the topic column

df.topic.value_counts().reset_index()


# In[17]:


## making a new dataframe that only includes the state of Minnesota

df_minnesota = df.groupby('locationdesc').get_group('Minnesota').reset_index()
df_minnesota


# In[18]:


## dropping irrelevant columns

df_minnesota.drop(['category','index', 'indicator','breakoutcategory','breakout','geolocation'], inplace=True, axis=1)
df_minnesota


# In[19]:


## exploring the data and what values are in the topic coloumn
   
   df_minnesota['topic'].value_counts()


# In[21]:


## visualizing the data of the new dataframe

df_minnesota['topic'].value_counts()[:20].plot(kind='barh')


# In[22]:


## creating a new dataframe that will group the data by the year 

dfu = df_minnesota.groupby(['year']).topic.value_counts().unstack()
dfu


# In[23]:


## filling the NaN values with o

dfu.fillna(0)


# In[24]:


## plotting the findings

ax = dfu.plot.bar()
ax.set_title('Leading Causes of Heart Attacks per Year in Minnesota',color='black')
ax.set_ylabel('Number of People', color='black')
ax.set_xlabel('Year', color='black')
ax.legend(bbox_to_anchor=(1.0, 1.0))
ax.plot()


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# # Project: Investigate a Dataset (TMDb movie data)
# Table of Contents
# Introduction
# Data Wrangling
# Exploratory Data Analysis
# Conclusions

# # Introduction
# In this project I have investigated TMDb movies dataset which contains informationabout 10,000 movies ,including user ratings and revenue.

# In[1]:


# Use this cell to set up import statements for all of the packages that you
#   plan to use.
import numpy as np
import pandas as pd
import csv
from datetime import datetime
import matplotlib.pyplot as plt

# Remember to include a 'magic word' so that your visualizations are plotted
#   inline with the notebook. See this page for more:
#   http://ipython.readthedocs.io/en/stable/interactive/magics.html


# # Data Wrangling
# In this section I will load the data get its information and check for duplicates and clean it

# # General Properties
# Loading the data

# In[2]:


movies_df=pd.read_csv('tmdb-movies.csv')
movies_df.head()


# In[3]:


movies_df.shape


# statistical describtion

# In[4]:


movies_df.describe()


# data types

# In[5]:


movies_df.info()


# duplicated rows

# In[6]:


sum(movies_df.duplicated())


# # Data Cleaning (making the data reasier and more accurate to deal with)
# remove unnecessary columns (according to the planned questions)
# remove duplicates
# remove zeros

# # remove unnecessary columns
# columns to be removed: id, imdb_id, budget, revenue, homepage, tagline, cast, overview, keywords, release_date, vote_count,vote_average

# In[7]:


columns_delete=['id', 'imdb_id', 'budget', 'revenue', 'homepage', 'tagline', 'cast', 'overview', 'keywords', 'release_date', 'vote_count','vote_average']
movies_df.drop(columns_delete, axis=1, inplace=True)
movies_df.head()


# In[8]:


movies_df.shape


# # remove duplicates

# In[9]:


movies_df.drop_duplicates(keep = 'first', inplace = True)
movies_df.shape


# # remove zero values

# In[10]:


movies_df=movies_df[movies_df!=0].dropna()
movies_df.reset_index(drop=True, inplace=True)
movies_df.shape


# # Exploratory Data Analysis

# I will invetigate relation between the different variables and their highest and lowest values

# # Q1 which movie had the highest and the lowest profit ?

# In[12]:


movies_df['profit'] = movies_df['revenue_adj'] - movies_df['budget_adj']
movies_df.head()


# In[13]:


movies_df.sort_values(['profit'],ascending=False)


# # Highest profit
# Star Wars

# # Lowest profit
# The warrior's way

# # Q2longest and shortest runtime?
# longest runtime

# In[14]:


movies_df.loc[movies_df['runtime'].idxmax()]


# shortest runtime

# In[15]:


movies_df.loc[movies_df['runtime'].idxmin()]


# # longest runtime
# Carlos (338)

# # shortest runtime
# kid's story (15)

# # Q3Highest and lowest popularity?

# Highest popularity

# In[16]:


movies_df.loc[movies_df['popularity'].idxmax()]


# In[17]:


movies_df.loc[movies_df['popularity'].idxmin()]


# # Q4generes with highest and lowest popularity?

# In[18]:


movies_df.groupby(['genres']).mean().sort_values(['popularity'],ascending=False)


# # Most popular generes
# Adventure|Drama|Science Fiction

# # least popular genere
# Drama|Comedy|Romance|Foreign

# # Q5 number of movies released each year?

# In[19]:


movies_df['count'] = 1
movies_df.groupby(['release_year']).count().sort_values(['count'])


# # Q6 revenue W.R.T director?

# In[20]:


movies_df.groupby(['director']).mean().sort_values(['revenue_adj'],ascending=False)


# # director that brings the highest revenue
# Irwin Winkler
# 
# 

# # director that brings the lowest revenue
# Shinichiro Watanabe

# # Q7 What is revenu relation to budget?

# In[21]:


# x-axis
plt.xlabel('Revenue in Dollars')
# y-axis
plt.ylabel('Budget in Dollars')
# Title of the histogram
plt.title('Relationship between revenue and budget')
plt.scatter(movies_df['revenue_adj'], movies_df['budget_adj'], alpha=0.5)
plt.show()


# notes Relationship between revenue and budget movie a steady sttate and not increased

# # Conclusions
# We can conclude that the action genere is the most popular and profitable genere as the movies with the highest profit and popularity are of action genere

# We can also conclude that the number of movies released each year has increaed significantly

# We can see also that most movies are in the low budget low revenue area

# # References

# https://bit.ly/3sQNCEX

# https://bit.ly/3fF09r1

# https://bit.ly/2PImjxZ

# https://bit.ly/3moo5jY

# https://bit.ly/3fN5zAv

# In[ ]:





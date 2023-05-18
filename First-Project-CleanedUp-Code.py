#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from pathlib import Path
import matplotlib
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('video_games.csv')


# In[2]:


file = Path('video_games.csv')


# In[3]:


df = pd.read_csv(file, encoding="ISO-8859-1")


# In[4]:


df.head()


# In[5]:


df.columns
game_sales_df = df[['Name', 'NA_Sales', 'EU_Sales', 'Other_Sales', 'Global_Sales']]
game_sales_df


# In[6]:


#Highest Selling game of all time
highest_sales_row = df.nlargest(1, 'Global_Sales')
highest_selling_game = highest_sales_row['Name'].iloc[0]
print("The highest selling game of all time is:", highest_selling_game)


# In[7]:


#Lowest Selling game of all time
lowest_sales_row = df.nsmallest(1, 'Global_Sales')
lowest_selling_game = lowest_sales_row['Name'].iloc[0]
print("The lowest selling game of all time is:", lowest_selling_game)


# In[10]:


#50 HIGHEST selling games of all time
game_sales_df = df[['Name', 'Global_Sales', 'Platform']]
game_sales_df
top_50 = game_sales_df.sort_values('Global_Sales', ascending=False).head(50)

print(top_50)


# In[ ]:





# In[ ]:


#Bar graph for 50 HIGHEST selling games of all time

plt.bar(top_50['Name'], top_50['Global_Sales'])
plt.xticks(rotation=90)
plt.xlabel('Name')
plt.ylabel('Global Sales (millions)')
plt.title('Top 50 Highest Selling Games of All Time')
plt.show()


# In[15]:


#bar graph for top 50 selling games. Replaced game names with pub(Publishers)
plt.bar(top_50['Platform'], top_50['Global_Sales'])
plt.xticks(rotation=90)
plt.xlabel('Platform')
plt.ylabel('Global Sales (millions)')
plt.title('Top 50 Highest Selling Games of All Time')

plt.tight_layout()
plt.show()


# In[12]:


#top 5 publishers 
df = pd.read_csv('video_games.csv')

publisher_releases = df['Publisher'].value_counts()

print(publisher_releases)


# In[13]:


#bargraph for top 5 publishers

df = pd.read_csv('video_games.csv')

publisher_releases = df['Publisher'].value_counts()


top_publishers = publisher_releases.head(5)

plt.bar(top_publishers.index, top_publishers.values)
plt.xlabel('Publisher')
plt.ylabel('Number of Releases')
plt.title('Top 5 Publishers by Number of Releases')
plt.xticks(rotation = 30, ha = 'right')

plt.show()


# In[14]:


#top5 publishers highest selling game
df = pd.read_csv('video_games.csv')

top_publishers = publisher_releases.head(5)
top_games = {}

for publisher in top_publishers.index:
    
    publisher_df = df[df['Publisher'] == publisher]
    
    top_game = publisher_df.loc[publisher_df['Global_Sales'].idxmax(), 'Name']
    
    top_games[publisher] = top_game

for publisher, game in top_games.items():
    print(f"Publisher: {publisher}\tNumber One Selling Game: {game}")


# In[ ]:





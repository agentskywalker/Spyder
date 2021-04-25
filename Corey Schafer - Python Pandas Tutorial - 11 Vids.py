# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 19:37:24 2021


Corey Schafer - Python Pandas Tutorial - 11 Videos 
https://www.youtube.com/watch?v=ZyhVh-qRZPA&list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS

Stack Overflow Annual Developer Survey - sample csv dataset
https://insights.stackoverflow.com/survey

@author: Skywalker
"""

#%% Vid 1 - Python Pandas Tutorial (Part 1): Getting Started with Data Analysis
# - Installation and Loading Data
# pip install pandas

import pandas as pd

df = pd.read_csv("data2019/survey_results_public.csv")

# dataframe is rows and columns
df

#%%
# Get count of rows and columns - using shape attribute
df.shape


#%%
# See all list of Data rows, columns and datatypes - using info() method
df.info()


#%% Update options to display all columns
pd.set_option("display.max_columns", 85)
df

#%% Read the schema CSV in a new data frame
schema_df = pd.read_csv("data2019/survey_results_schema.csv")
schema_df.shape
schema_df.info()
schema_df

#%% - Update options to display a fixed rows, e.g, 65
pd.set_option("display.max_rows", 85)  # Now we can see all 85 rows
schema_df

#%% Display only 5 rows from top
df.head()

# Display only n rows from top
df.head(9)

#%% Display only 5 rows from bottom
df.tail()

#%% Display only n rows from bottom
df.tail(9)

#%% ########## Video 2 ##################################################
############## DataFrame and Series Basics - Selecting Rows and Columns
#########################################################################


#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

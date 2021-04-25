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


#%% Display the list of columns in the DataFrame
df.columns

df["Hobbyist"]
df.loc[0:2, "Hobbyist":"Employment"]


#%% ########## Video 2 ##################################################
############## DataFrame and Series Basics - Selecting Rows and Columns
#########################################################################

import pandas as pd

df = pd.read_csv("data2019/survey_results_public.csv")
schema_df = pd.read_csv("data2019/survey_results_schema.csv")
pd.set_option("display.max_columns", 85)
pd.set_option("display.max_rows", 85)

df.head()


#%% person -> dictionary
#   people -> all values in the dictionary as List


person = {"first": "Corey", "last": "Schafer", "email": "CoreyMSchafer@gmail.com"}

people = {"first": ["Corey"], "last": ["Schafer"], "email": ["CoreyMSchafer@gmail.com"]}

people = {
    "first": ["Corey", "Jane", "John"],
    "last": ["Schafer", "Doe", "Doe"],
    "email": ["CoreyMSchafer@gmail.com", "JaneDoe@email.com", "JohnDoe@email.com"],
}

people["email"]


#%% Use the List

import pandas as pd

df = pd.DataFrame(people)
df

# Access a single column of a dictionary using key
# df['email']        # syntax 1
df.email  # syntax 2

#%% See type of email

type(df["email"])

#%% Example- filtered down DataFrame

df[["last", "email"]]


#%% See list of columns of a DataFrame

df.columns

#%% See Rows of a DataFrame
########## iloc lets us search by using index ############
# See the first row of the DF
# Here, we see the column name as index
df.iloc[0]

#%% See the 1st and 3rd row from the DF
df.iloc[[0, 2]]

#%% Get a specific column from rows
# E.g. get email address from row 1 and 3
# index for row 1 and 3 are 0,2
# index for column 3/email is 2
df.iloc[[0, 2], 2]

#%% ########## loc lets us search by using labels ############
# for rows label is index
# for columns label is column name

# See the entire DF
df

df.loc[0]

df.loc[[0, 2]]

df.loc[[0, 2], "email"]

df.loc[[0, 2], ["email", "first"]]  # give col names and order


#%% Let's work on Pandas

import pandas as pd

df = pd.read_csv("data2019/survey_results_public.csv")
schema_df = pd.read_csv("data2019/survey_results_schema.csv")
pd.set_option("display.max_columns", 85)
pd.set_option("display.max_rows", 85)

# df.head()

#%%

df.shape
df.columns

#%%

df["Hobbyist"]

df["Hobbyist"].value_counts()

#%% Entire survey result for a single person
df.loc[0]
df.loc[0, "Hobbyist"]  # Get response for Hobbyist for 1st person/row
df.loc[[0, 3, 4], "Hobbyist"]  # Get selective response for Hobbyist for few rows
df.loc[0:4, "Hobbyist"]  # Get a range of response for Hobbyist for 1-5 rows

# Get a range of response for columns from Hobbyist to Employment for 1-5 rows
df.loc[0:4, "Hobbyist":"Employment"]


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

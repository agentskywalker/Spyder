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

from os import replace
from numpy import apply_along_axis
from numpy.lib.shape_base import expand_dims
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


#%% ################ Video 3 ##################################################
# Python Pandas Tutorial (Part 3): Indexes - How to Set, Reset, and Use Indexes
###############################################################################
# Create and use custom indexed

people = {
    "first": ["Corey", "Jane", "John"],
    "last": ["Schafer", "Doe", "Doe"],
    "email": ["CoreyMSchafer@gmail.com", "JaneDoe@email.com", "JohnDoe@email.com"],
}

import pandas as pd

df = pd.DataFrame(people)
df

df["email"]

df.set_index("email")  # Does NOT update the actual panda
df.set_index("email", inplace=True)  # Updates the actual panda

df

# df.loc[0]      # Gives error after updating the index
df.iloc[0]  # Does not give error
df.loc["CoreyMSchafer@gmail.com", "last"]  # Works using the email as index

# Reset Index
df.reset_index(inplace=True)
df.loc[0]

#%% Index operations using Stack Overflow data file

import pandas as pd

# Default index is gone and the column Respondent is used as index
df = pd.read_csv("data2019/survey_results_public.csv", index_col="Respondent")

# Default index is gone and the column Column is used as index
schema_df = pd.read_csv("data2019/survey_results_schema.csv", index_col="Column")
pd.set_option("display.max_columns", 85)
pd.set_option("display.max_rows", 85)

df.head()
schema_df


#%% Only 1 command comes in display in the interactive window
############# Check for corresponding settings #######

# schema_df.loc["MainBranch"]
# schema_df.loc["SOVisit1st"]
schema_df.loc["ITperson"]


#%%
# schema_df.loc["MgrIdiot", 'QuestionText']
schema_df.loc["ITperson", "QuestionText"]

#%% Sort the index alphabetically - TEMPORARILY

schema_df.sort_index()
schema_df.sort_index(ascending=False)


#%% Sort the index alphabetically - PERMANENTLY
schema_df.sort_index(inplace=True)
schema_df

#%% ################ Video 4 ##################################################
# Python Pandas Tutorial (Part 4): Filtering - Using Conditionals to Filter Rows and Columns
###############################################################################

people = {
    "first": ["Corey", "Jane", "John"],
    "last": ["Schafer", "Doe", "Doe"],
    "email": ["CoreyMSchafer@gmail.com", "JaneDoe@email.com", "JohnDoe@email.com"],
}

import pandas as pd

df = pd.DataFrame(people)

df

df["last"] == "Doe"  # Returns True/false result <-- Filter mask


#%% Type 1
filt = (df["last"] == "Schafer") | (df["first"] == "John")
df[filt]

#%% Type 2
df[(df["last"] == "Schafer") | (df["first"] == "John")]

#%% Type 3 - Best way

df.loc[filt, "email"]


#%% Operators
# & -> and
# | -> or
filt = (df["last"] == "Doe") & (df["first"] == "John")
df.loc[filt, "email"]

#%% All rows where fname is NOT Schafer, and lname is NOT John
#   Achieved by ~ before filt
filt = (df["last"] == "Schafer") | (df["first"] == "John")
df.loc[~filt, "email"]

#%%

import pandas as pd

# Default index is gone and the column Respondent is used as index
df = pd.read_csv("data2019/survey_results_public.csv", index_col="Respondent")

# Default index is gone and the column Column is used as index
schema_df = pd.read_csv("data2019/survey_results_schema.csv", index_col="Column")
pd.set_option("display.max_columns", 85)
pd.set_option("display.max_rows", 85)

df.head()

#%%
schema_df

#%%

high_salary = df["ConvertedComp"] > 50000
df.loc[high_salary]  # see all columns for the filter

#%%
# see selected columns for the filter
df.loc[high_salary, ["Country", "ConvertedComp", "JobSeek", "LanguageWorkedWith"]]

#%% See results from only specific country

countries = ["United States", "India", "United Kingdom", "Germany", "Canada"]
filt = df["Country"].isin(countries)  # step 1. create a filter
df.loc[filt, "Country"]  # step 2. apply the filter on the DF


#%% only get persons who said Python as a programming language skill

df["LanguageWorkedWith"]  # E.g. C++;HTML/CSS;Java;JavaScript;Python;SQL;VBA


#%%
# search string for Python
# Skip where the value is NaN/Not applicable
filt = df["LanguageWorkedWith"].str.contains("Python", na=False)
df.loc[filt, "LanguageWorkedWith"]

filt  # provide only True/False values
df.loc[filt]

#%% ################ Video 5 ##################################################
# Python Pandas Tutorial (Part 5): Updating Rows and Columns - Modifying Data Within DataFrames
###############################################################################
people = {
    "first": ["Corey", "Jane", "John"],
    "last": ["Schafer", "Doe", "Doe"],
    "email": ["CoreyMSchafer@gmail.com", "JaneDoe@email.com", "JohnDoe@email.com"],
}

import pandas as pd

df = pd.DataFrame(people)

df

df.columns

#%% Change names of all columns
df.columns = ["first_name", "last_name", "email"]
df.columns

#%% Change column names to UC
df.columns = [x.upper() for x in df.columns]
df


#%% Replace underscore with spaces in Column names
df.columns = df.columns.str.replace("_", " ")
df

#%% Revert
df.columns = df.columns.str.replace(" ", "_")
df.columns = [x.lower() for x in df.columns]
df

#%% Rename Column names
df.rename(columns={"first_name": "first", "last_name": "last"}, inplace=True)
df

#%% ROW OPERATIONS
#   Update data for row 3

df.loc[2] = ["John", "Smith", "JohnSmith@email.com"]
df

#%% Update selective data for row 3
df.loc[2, ["last", "email"]] = ["Archer", "JohnArcher@email.com"]
df

#%% Update selective data for ONLY 1 COLUMN in row 3
df.loc[2, "last"] = "Cipher"
df

#%% Revert
df.at[2, "last"] = "Archer"
df

#%% Filtering a row using a column value

filt = df["email"] == "JohnArcher@email.com"
df[filt]

# Filtering a column using a filtered row
df[filt]["last"]

#%% Trying to set on a Temp copy/view -- so error
# SettingWithCopyWarning:
# A value is trying to be set on a copy of a slice from a DataFrame.
# Try using .loc[row_indexer,col_indexer] = value instead
df[filt]["last"] = "Mohapatra"

#%% Correct way to use filter to set column value
df.loc[filt, "last"] = "Mohapatra"
df

#%% Retrieve and Format values without saving
df["email"].str.lower()

#%% Retrieve and Format values with saving. Update multiple rows at once
df["email"] = df["email"].str.lower()
df
#%% 4 popular methods for Data Update
# apply
# map
# applymap
# replace
########################################################
#%% apply method with series objects
# call a function on a series
# check length of the email addresses
df["email"].apply(len)


#%% Update using a function and save
def update_email(email):
    return email.upper()


df["email"] = df["email"].apply(update_email)  # pass the function only.
# DO NOT give () after update-email function. () will execute the function
df

#%% Change email to lower case using lambda function
df["email"] = df["email"].apply(lambda x: x.lower())
df

#%% apply method with data frames
# check length of the email addresses
df["email"].apply(len)

# check number of rows in the df
df.apply(len, axis="columns")

len(df["email"])

#%% Get the minimum value
df.apply(pd.Series.min)

#%% Get the minimum value
df.apply(lambda x: x.min())

#%% ######## applymap method ###############
df.applymap(len)


#%%
df.applymap(str.lower)

#%% ######## map method ###############
# Change the values
df["first"].map({"Corey": "Chris", "Jane": "Mary"})
# ISSUE: The values which do not qualify, they will be changes to NaN (not a number)
#%% ######## Replace method ###############
# Change the values
df["first"].replace({"Corey": "Chris", "Jane": "Mary"})

# To Save:: df['first'] = df['first'].replace({'Corey': 'Chris', 'Jane': 'Mary'})

#%% Functions on real world values
import pandas as pd

df = pd.read_csv("data2019/survey_results_public.csv")
schema_df = pd.read_csv("data2019/survey_results_schema.csv")
pd.set_option("display.max_columns", 85)
pd.set_option("display.max_rows", 85)

df.head()

#%% Rename a column ConvertedComp to SalaryUSD
df.rename(columns={"ConvertedComp": "SalaryUSD"}, inplace=True)

#%% Check new column name and values
df["SalaryUSD"]

#%% This has Yes/No values
df["Hobbyist"]

#%% Convert Hobbyist to boolean values
df["Hobbyist"].map({"Yes": True, "No": False})

#%% Save
df["Hobbyist"] = df["Hobbyist"].map({"Yes": True, "No": False})
df
#%% ################ Video 5 ##################################################
# Python Pandas Tutorial (Part 6): Add/Remove Rows and Columns From DataFrames
###############################################################################
people = {
    "first": ["Corey", "Jane", "John"],
    "last": ["Schafer", "Doe", "Doe"],
    "email": ["CoreyMSchafer@gmail.com", "JaneDoe@email.com", "JohnDoe@email.com"],
}

import pandas as pd

df = pd.DataFrame(people)
df

#%% Combine Fname and Lname
df["first"] + " " + df["last"]

#%% Add new column Full name
df["full_name"] = df["first"] + " " + df["last"]
df

# We can use apply function
# Using a dot(.) on the df will add an attribute, and not a column. So use []

#%% Remove columns using drop method
df.drop(columns=["first", "last"])

#%% Save
df.drop(columns=["first", "last"], inplace=True)
df
#%% Split a value using a separator
df["full_name"].str.split(" ")

#%% Split up and shown in columns
df["full_name"].str.split(" ", expand=True)

#%% Add new columns
df[["first", "last"]] = df["full_name"].str.split(" ", expand=True)
df
#%% Add rows to DF
########### append method #################
df.append({"first": "Tony"}, ignore_index=True)

#%%
people = {
    "first": ["Tony", "Steve"],
    "last": ["Stark", "Rogers"],
    "email": ["IronMan@avenge.com", "Cap@avenge.com"],
}
df2 = pd.DataFrame(people)
df2

#%% Append df2 to df
df.append(df2, ignore_index=True)

#%% Save
df = df.append(df2, ignore_index=True)

#%% Combine 2 DFs by appending rows
df

#%% Remove Rows
df.drop(index=4)
# to save use inplace=True

#%% Drop using condition
# last name = Doe
# df.drop(index=df[df['last'] == 'Doe'].index) # not so easy to read
filt = df["last"] == "Doe"
df.drop(index=df[filt].index)

#%% ######################## ##################################################
# Python Pandas Tutorial (Part 7): Sorting Data
###############################################################################
people = {
    "first": ["Corey", "Jane", "John", "Adam"],
    "last": ["Schafer", "Doe", "Doe", "Doe"],
    "email": [
        "CoreyMSchafer@gmail.com",
        "JaneDoe@email.com",
        "JohnDoe@email.com",
        "A@email.com",
    ],
}

import pandas as pd

df = pd.DataFrame(people)
df

#%% Sort ASC by default
df.sort_values(by="last")

#%% Sort DESC
df.sort_values(by="last", ascending=False)

#%% Use multiple columns while sorting
df.sort_values(by=["last", "first"], ascending=False)

#%% Mixed ASC and DESC sorting
# Last Name DESC, First Name ASC order
df.sort_values(by=["last", "first"], ascending=[False, True], inplace=True)

#%%
df

#%% Sort by index
df.sort_index()

#%% Sort only 1 column
df["last"].sort_values()

#%%
import pandas as pd

df = pd.read_csv("data2019/survey_results_public.csv")
schema_df = pd.read_csv("data2019/survey_results_schema.csv")
pd.set_option("display.max_columns", 85)
pd.set_option("display.max_rows", 85)

df.head()
#%% Sort by country ASC, salary DESC. Save the result to df.
df.sort_values(by=["Country", "ConvertedComp"], ascending=[True, False], inplace=True)

#%%
df.head()

#%% Check first 50 rows
df[["Country", "ConvertedComp"]].head(50)

#%% Check 10 highest salaries in the survey
df["ConvertedComp"].nlargest(10)

#%% Check 10 smallest salaries in the survey
df["ConvertedComp"].nsmallest(10)

#%% Check 10 highest salaries in the survey and Get the entire rows
df.nlargest(10, "ConvertedComp")

#%% Check 10 smallest salaries in the survey and Get the entire rows
df.nsmallest(10, "ConvertedComp")

#%% ###########################################################################
# Python Pandas Tutorial (Part 8): Grouping and Aggregating - Analyzing and Exploring Your Data
###############################################################################
#%%
import pandas as pd

df = pd.read_csv("data2019/survey_results_public.csv")
schema_df = pd.read_csv("data2019/survey_results_schema.csv")
pd.set_option("display.max_columns", 85)
pd.set_option("display.max_rows", 85)

df.head()

#%%

df.head()

#%%
df["ConvertedComp"].head(15)

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


#%%

#%%

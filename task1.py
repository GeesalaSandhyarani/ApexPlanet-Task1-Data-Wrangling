# importing pandas library as pd - for data processing
import pandas as pd
# create a variable named df(dataframe-- which guve rows and coloumns) and store the path of excel in python (which reads the excel using pandas )
df = pd.read_excel("Sales_Dataset.xlsx")
# printing head - view first 5 rows 
print(df.head())
# info- which is used to collect the information about the datatypes of coloumns,Dataset structure, data types, non-null values
print(df.info())
# describe is used to know the statistics like person min age max age , memory usage
print(df.describe())
'''if the given dataset which is stored in df has null values -sum the values ,its check for the missing values then sum how many null values are there here
age and city'''
print(df.isnull().sum())
# If any record exists more than once, it is a duplicate entry, then it will sum them
print(df.duplicated().sum())
#  calculating mean and median for Age, mode for City
print(df["Age"].mean())
print(df["Age"].median())
print(df["City"].mode())
# fillna is used to fill the missing values -- which refers to fill not available values in dataset
df['Age']=df['Age'].fillna(df['Age'].median())
# calculating the mode for city column and returning the most repeated city
df["City"] = df["City"].fillna(df["City"].mode()[0])
# df.shape command gives(rows,columns)-- here it is 1000 rows and 12 columns
print(df.shape)
#printing list of column names
print(df.columns)
print(df["Age"].min())
print(df["Age"].max())
print(df["Age"].value_counts())
print(df.isnull().sum())
df.to_excel("Cleaned_Sales_Dataset.xlsx", index=False)
print("Duplicate Rows:", df.duplicated().sum())
import pandas as pd

csv_1 = pd.read_csv("C:\\Users\\tejud\\OneDrive\\Documents\\Desktop\\CTVed\\Coding with Harry Potter\\Python\\Pandas\\Biggg Data.csv")

# print(csv_1)

# to get the index of the dataframe
# print(csv_1.index)

# to get the columns of the dataframe
# print(csv_1.columns)

# describe() function is used to get the statistical summary of the dataframe
# print(csv_1.describe())

# to get the first 5 rows of the dataframe
# print(csv_1.head())  

# to get the last 5 rows of the dataframe
# print(csv_1.tail()) 

# print(csv_1.head(3)) 
# print(csv_1.tail(3)) 

 # to get the specific rows of the dataframe
# print(csv_1[:2]) 
# print(csv_1[6:10]) 

# print(type(csv_1))

# print(csv_1.index.array)

# to get the values of the dataframe in the form of numpy array
# print(csv_1.to_numpy())

# import numpy as np
# v = np.array(csv_1)
# print(v)

# to sort the dataframe by index in ascending order
# axis=0 means we want to sort the rows and axis=1 means we want to sort the columns
# inplace=True means we want to sort the dataframe in place and not return a new dataframe
# ascending=True means we want to sort in ascending order and ascending=False means we want to sort in descending order
# print(csv_1.sort_index(axis=0, ascending=False))

# to change the data from the dataframe
# not a proper way to change the data in the dataframe but it works
# csv_1["DEALSIZE"][0] = "Large"
# print(csv_1)

# proper way to change the data in the dataframe
# csv_1.loc[0, "DEALSIZE"] = "Small"
# print(csv_1)

# to get the specific rows and columns of the dataframe
# print(csv_1.loc[[2,3],[ "ORDERDATE","DEALSIZE"]])
# print(csv_1.loc[[2,3],:])

# to get the specific rows and columns of the dataframe using iloc
# iloc is used to get the specific rows and columns of the dataframe by index
# print(csv_1.iloc[2:4, 1:2]) 

# drop() function is used to drop the specific rows and columns of the dataframe
# print(csv_1.drop("ORDERNUMBER", axis=1))

# in the missing values it show NAN which means Not a Number and it is used to represent the missing values in the dataframe
# print(csv_1.loc[[0,2],[ "ORDERNUMBER","STATE"]])

# dropna() function is used to drop the rows with missing values
# print(csv_1.dropna())

# print(csv_1.dropna(axis=1))

# how parameter is used to specify the condition for dropping the rows or columns                        
# print(csv_1.dropna(how='any')) # any means if there is any missing value in the row or column then it will be dropped

# print(csv_1.dropna(how='all')) # all means if there are all missing values in the row or column then it will be dropped

# print(csv_1.dropna(how='subset')) # subset means if there are missing values in the specified columns then it will be dropped

# this will drop the rows where there are missing values in the DEALSIZE column
# print(csv_1.dropna(subset=['DEALSIZE'])) 

# inplace=True means we want to drop the rows in place and not return a new dataframe
# print(csv_1.dropna(inplace=True)) 

# thresh parameter is used to given number NAN values to drop the rows or columns
# print(csv_1.dropna(thresh=2)) 


# fillna() function is used to fill the missing values in the dataframe
# print(csv_1.fillna("python"))

# print(csv_1.fillna({"DEALSIZE": "python","ORDERNUMBER": "java"}))

 # ffill means forward fill and it will fill the missing values with the previous value
# print(csv_1.fillna(method="ffill"))

# bfill means backward fill and it will fill the missing values with the next value
# print(csv_1.fillna(method="bfill"))

# axis=0 means we want to fill the missing values in the rows and axis=1 means we want to fill the missing values in the columns
# print(csv_1.fillna(method="ffill", axis=0))

# fill all missing values with a specific value
# print(csv_1.fillna(12,inplace=True))

# limit parameter is used to specify the number of missing values to fill
print(csv_1.fillna("python", limit=2))


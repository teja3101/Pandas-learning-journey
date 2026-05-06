import pandas as pd

csv_1 = pd.read_csv("C:\\Users\\tejud\\OneDrive\\Documents\\Desktop\\CTVed\\Coding with Harry Potter\\Python\\Pandas\\Biggg Data.csv")
# print(csv_1)

# dropna() function is used to drop the rows with missing values
# print(csv_1.dropna())

# drop by column
# print(csv_1.dropna(axis=1))

# how parameter is used to specify the condition for dropping the rows or columns                        
# print(csv_1.dropna(how='any')) # any means if there is any missing value in the row or column then it will be dropped

# print(csv_1.dropna(how='all')) # all means if there are all missing values in the row or column then it will be dropped

# print(csv_1.dropna(subset=['STATE'])) # subset means if there are missing values in the specified columns then it will be dropped

# inplace=True means we want to drop the rows in place and not return a new dataframe
# print(csv_1.dropna(inplace=True)) 
# inplace=False means  
# print(csv_1.dropna(inplace=False)) 

# thresh parameter is used to given number NAN values to drop the rows or columns
# print(csv_1.dropna(thresh=1)) 
# print(csv_1.dropna(thresh=2)) 


# fillna() function is used to fill the missing values in the dataframe
# print(csv_1.fillna("python"))

# we should pass data in dictionary for particular columns fill val in rows
# print(csv_1.fillna({"DEALSIZE": "python","ORDERNUMBER": "java"}))

 # ffill means forward fill and it will fill the missing values with the previous value
# print(csv_1.fillna(method='ffill'))    #old version support
# print(csv_1.ffill())                     #new version support

# bfill means backward fill and it will fill the missing values with the next value
# print(csv_1.fillna(method="bfill"))
# print(csv_1.bfill()) 

# axis=0 means we want to fill the missing values in the rows and axis=1 means we want to fill the missing values in the columns
# print(csv_1.ffill(axis=0))

# fill all missing values with a specific value
# print(csv_1.fillna(12))9

# limit parameter is used to specify the number of missing values to fill
print(csv_1.fillna("python", limit=2))
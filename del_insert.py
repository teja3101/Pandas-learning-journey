import pandas as pd

# INSERT - add new column to dataframe

var = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
# print(var)

# <---------------- to add new column to dataframe we have multiple methods>----------------->

# method 1 - using insert() method to add new column to dataframe>----------------
# index num of A=0 and B=1
var.insert(1, 'C', [7,8,9])
# print(var)

# When i want to add duplicate cpy of another clm
var.insert(2, 'D', var['A'])
# print(var)

# ValueError - data should be equivalnet to the length of the dataframe
# var.insert(1, 'E', [7,8,9,10])
# print(var)

# method 2 - using slicing to add new column to dataframe>-----------------
var["Python"] = var['A'][:2]
# print(var)

# method 3 - using assign() method to add new column to dataframe>-----------------
var = var.assign(Java=[31,21,52])
# print(var)    

# method 4 - using assignment operator to add new column to dataframe>-----------------
var['C++'] = [11,22,33]
# print(var)

# <------------------- to add rows to dataframe we have multiple methods>----------------->

# method 1 - using loc[] method to add new row to dataframe>-----------------
var.loc[2] = [32,45,67,89,90,12,89]
# print(var)

# method 2 - using append() method to add new row to dataframe>-----------------
var1 = pd.DataFrame({'A': [10], 'B': [20], 'C': [30], 'D': [40], 'Python': [50], 'Java': [60], 'C++': [70]})
var = var._append(var1, ignore_index=True)   
# print(var1)

# method 3 - using concat() method to add new row to dataframe>-----------------
var2 = pd.DataFrame([[11,22,33,44,55,66,77]], columns=['A', 'B', 'C', 'D', 'Python', 'Java', 'C++'])
var2 = pd.DataFrame([[34,56,78,90,12,34,56]], columns=var.columns)
# print(var2)

# DELETE - delete column from dataframe

# method 1 - using pop() method>---------------------
# var1 = var.pop('A')
# this will return the deleted column
# print(var1) 
# this will return the dataframe after deletion of column A
# print(var) 

# method 2 - using drop() method>------------------------
var.drop('A',axis=1, inplace=True)
# print(var)

# method 3 - using del() method>--------------------------
del var['B']
# print(var)

# method 4 - using condition>------------------------------
var = var[var['C++']>89]
print(var)
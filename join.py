import pandas as pd

# Join >-------------------------------

# var = pd.DataFrame({
#     'A': [1,2,3,4], 
#     'B': [5,6,7,8]
# }, index=['a','b','c','d'])

# var1 = pd.DataFrame({
#     'c': [10,20,30], 
#     'D': [50,70,80]
# }, index=['a','b','c'])

# print(var.join(var1))

# print(var1.join(var, how='outer'))
# print(var1.join(var, how='inner'))

# print(var1.join(var, how='right'))
# print(var1.join(var, how='left'))

var = pd.DataFrame({
    'A': [1,2,3,4], 
    'B': [5,6,7,8]
}, index=['a','b','c','d'])

var1 = pd.DataFrame({
    'B': [10,20,30], 
    'D': [50,70,80]
}, index=['a','b','c'])

print(var1.join(var, how='outer', lsuffix='_12', rsuffix='_13'))


# Append >-------------------------------

# In recent versions of Pandas, append() is removed. Instead of append(), use pd.concat()
# a = var.append(var1)
# print(a)

# print(var.append(var1), ignore_index = True)
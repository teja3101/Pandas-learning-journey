import pandas as pd

# GroupBy >-------------------------------

var = pd.DataFrame({
    'name': ['a','b','c','d','a','b','a','b','a','c','c'],
    'S1': [12,13,14,12,13,14,15,23,25,16,10],
    'S2': [23,24,25,26,27,28,29,30,25,34,35]
})

# print(var)

var_new = var.groupby('name')
# # print(var_new)
# for x,y in var_new:
#     print(x)
#     print(y)
#     print()       
    

# for particular data fetching
# print(var_new.get_group('a'))

# aggregate function
# print(var_new.min())
# print(var_new.max())
# print(var_new.mean())

# convert into list
li = list(var_new)
print(li)


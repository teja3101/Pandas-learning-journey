import pandas as pd

# merge >--------------------------------------------
# var1 = pd.DataFrame({'A':[1,2,3,4], 'B':[11,12,13,14]})
# # var2 = pd.DataFrame({'A':[1,2,3,4], 'B':[21,22,23,24]})
# var2 = pd.DataFrame({'A':[1,2,3,4], 'B1':[21,22,23,24]})

# print(pd.merge(var1,var2))

# merge data with common data
# print(pd.merge(var1,var2, on='A'))

# print(pd.merge(var2,var1, on='A'))

# print(pd.merge(var1,var2, how = 'inner'))
# print(pd.merge(var1,var2, how = 'left'))
# print(pd.merge(var1,var2, how = 'right'))
# print(pd.merge(var1,var2, how = 'outer'))

# print(pd.merge(var1,var2, how = 'outer', indicator = True))

# print(pd.merge(var1,var2, left_index=True, right_index=True))

# if you want to change the clm name 
# print(pd.merge(var1,var2, left_index=True, right_index=True, suffixes=('name','python')))

# concat >--------------------------------------------
# sr1 = pd.Series([1,2,3,4])
# sr2 = pd.Series([11,12,13,14])

# print(pd.concat([sr1,sr2]))

# d1 = pd.DataFrame({'A':[1,2,3,4], 'B':[11,12,13,14]})
d1 = pd.DataFrame({'O':[1,2,3,4], 'B':[11,12,13,14]})
d2 = pd.DataFrame({'A':[1,2,3,4], 'c':[21,22,23,24]})

# print(pd.concat([d1,d2]))

# print(pd.concat([d1,d2], axis=1))

# print(pd.concat([d1,d2], axis=1, join='outer'))

# print(pd.concat([d1,d2], axis=1, keys=["d1","d2"]))

# print(pd.concat([d1,d2], axis=1, keys=["d1","d2"]))

# print(pd.concat([d1,d2]))

print(pd.concat([d1,d2]))
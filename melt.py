# reshape >-------------

import pandas as pd

var = pd.DataFrame({
    'days': [1,2,3,4,5,6],
    'stdname': ['a','b','c','d','e','f'],
    'eng': [10,20,30,40,50,60],
    'math': [15,25,35,45,55,65],
    'sci': [20,30,40,50,60,70]
})

# print(var)

# convert all data into vertical form 
# print(pd.melt(var))

# work as a id variable
# print(pd.melt(var, id_vars=['eng']))

print(pd.melt(var, id_vars=['eng'], var_name='python', value_name='marks'))


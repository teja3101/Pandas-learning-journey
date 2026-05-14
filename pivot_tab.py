import pandas as pd

var = pd.DataFrame({
    'days': [1,1,1,1,2,2],
    'stdname': ['a','b','a','a','b','b'],
    'eng': [10,20,30,40,50,60],
    'math': [15,25,35,45,55,65],
    'sci': [20,30,40,50,60,70]
})

# print(var)

# print(var.pivot(index='days', columns='stdname'))

# print(var.pivot(index='days', columns='stdname', values='eng'))

# aggfunc used when there are multiple values for the same index and column combination. It specifies how to aggregate those values. Common aggregation functions include 'mean', 'sum', 'min', 'max', etc.
# print(var.pivot_table(index='stdname', columns='days', aggfunc='mean'))
# print(var.pivot_table(index='stdname', columns='days', aggfunc='sum'))

print(var.pivot_table(index='stdname', columns='days', aggfunc='mean', margins=True, margins_name='Total'))
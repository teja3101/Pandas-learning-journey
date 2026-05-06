import pandas as pd

# l = [1,2,3,4,5]
# var = pd.DataFrame(l)
# print(var)
# print(type(var))

# d = {
#     "name":['python','c','java'], 
#     "por":[12,34,56],
#     "rank":[1,2,4]
# }
# var = pd.DataFrame(d)
# print(var)

# if lenght of data is not same then it will give error
# d = {
#     "name":['python','c','java'], 
#     "por":[12,56],
#     "rank":[1,2]
# }
# var = pd.DataFrame(d)
# print(var)

# d = {
#     "name":['python','c','java'], 
#     "por":[12,34,56],
#     "rank":[1,2,4]
# }
# var = pd.DataFrame(d,columns=["name"])
# var = pd.DataFrame(d)
# print(var)
# print(var["name"][2])

# list_1 = [[1,2,3],[4,5,6],[7,8,9]]
# var = pd.DataFrame(list_1)
# print(var)

# list_1 = [[1,2,5,3],[4,5,6],[7,8,9]]
# var = pd.DataFrame(list_1)
# print(var)

# by using multiple series we can create dataframe
sr = {"s1":pd.Series([1,2,3,4,5]), "s2":pd.Series([6,7,8,9,10])}
var = pd.DataFrame(sr)
print(var)
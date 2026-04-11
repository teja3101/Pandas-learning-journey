import pandas as pd

# var = pd.DataFrame({"A": [1, 2, 3, 6, 7],"B": [4, 5, 6, 8, 9]})
# print(var)

# create "C" column to store the sum of "A" and "B" columns
# var["C"] = var["A"] + var["B"]
# print(var)

# var["D"] = var["A"] - var["B"]
# print(var)

# var["E"] = var["A"] * var["B"]
# print(var)

# var["F"] = var["A"] / var["B"]
# print(var)

# to filter the data we can use boolean indexing
var = pd.DataFrame({"A": [10, 20, 30, 60, 70],"B": [14, 25, 26, 48, 69]})
# var["python"] = var["A"] < 50
var["python"] = (var["A"] < 50) & (var["B"] < 50)
print(var)
import pandas as pd

dis = {'a':[1,2,3,4], 'b':[4,3,6,7], 'c':[3,5,6,7]}
d = pd.DataFrame(dis)
# print(d)

#index=False means that the index column will not be included in the CSV file. If you want to include the index, you can simply omit this parameter or set it to True.
# d.to_csv("new_data.csv", index=False)   

 #header=False means that the column names will not be included in the CSV file. If you want to include the column names, you can simply omit this parameter or set it to True.
d.to_csv("new_data1.csv", index=False,header=['t','c','d']) 
import pandas as pd

# to read the csv file
# csv_1 = pd.read_csv("C:\\Users\\tejud\\OneDrive\\Documents\\Desktop\\CTVed\\Coding with Harry Potter\\Python\\Pandas\\Biggg Data.csv")
# print(csv_1)

# to read only first 2 rows of the csv file
# csv_2 = pd.read_csv("C:\\Users\\tejud\\OneDrive\\Documents\\Desktop\\CTVed\\Coding with Harry Potter\\Python\\Pandas\\Biggg Data.csv",nrows=2)
# print(csv_2)
# print(type(csv_2))

# to read only specific columns of the csv file
# csv_3 = pd.read_csv("C:\\Users\\tejud\\OneDrive\\Documents\\Desktop\\CTVed\\Coding with Harry Potter\\Python\\Pandas\\Biggg Data.csv", usecols=["CUSTOMERNAME","ADDRESSLINE1"])
# print(csv_3)

# csv_4 = pd.read_csv("C:\\Users\\tejud\\OneDrive\\Documents\\Desktop\\CTVed\\Coding with Harry Potter\\Python\\Pandas\\Biggg Data.csv", usecols=[0,3])
# print(csv_4)

# skip the first 2 rows of the csv file
# csv_5 = pd.read_csv("C:\\Users\\tejud\\OneDrive\\Documents\\Desktop\\CTVed\\Coding with Harry Potter\\Python\\Pandas\\Biggg Data.csv", skiprows=2, usecols=[0,3])
# print(csv_5)

# index_col = 0 will make the first column as index of the dataframe
# csv_6 = pd.read_csv("C:\\Users\\tejud\\OneDrive\\Documents\\Desktop\\CTVed\\Coding with Harry Potter\\Python\\Pandas\\Biggg Data.csv", index_col="CUSTOMERNAME")
# print(csv_6)

# header = None will make the first row as data and not as header of the dataframe
# csv_7 = pd.read_csv("C:\\Users\\tejud\\OneDrive\\Documents\\Desktop\\CTVed\\Coding with Harry Potter\\Python\\Pandas\\Biggg Data.csv", header=2, index_col=0)
# print(csv_7)

# name of the columns in the dataframe
# csv_8 = pd.read_csv("C:\\Users\\tejud\\OneDrive\\Documents\\Desktop\\CTVed\\Coding with Harry Potter\\Python\\Pandas\\Biggg Data.csv", names=["Columns"])
# print(csv_8)

# if we want to add prefix to the columns of the dataframe
# csv_9 = pd.read_csv("C:\\Users\\tejud\\OneDrive\\Documents\\Desktop\\CTVed\\Coding with Harry Potter\\Python\\Pandas\\Biggg Data.csv", names=None, prefix="Col")
# print(csv_9)

# if we want to change the data type of a column while reading the csv file
csv_10 = pd.read_csv("C:\\Users\\tejud\\OneDrive\\Documents\\Desktop\\CTVed\\Coding with Harry Potter\\Python\\Pandas\\Biggg Data.csv", dtype={"QUANTITYORDERED":"float"})
print(csv_10)

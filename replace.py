import pandas as pd 

data = pd.read_csv("C:\\Users\\tejud\\OneDrive\\Documents\\Desktop\\CTVed\\Coding with Harry Potter\\Python\\Pandas\\Biggg Data.csv")
# print(data)

# replace() used to replace some val with something
# print(data.replace(to_replace='Julie', value='Teju'))           #for text

# print(data.replace(10121, 31))                          #for number

# with dictionary -regular expression : regex=True used to replace alphabetical data 
# print(data.replace('[A-Za-z]','Python',regex=True))

# print(data.replace('[A-Z]','Tej',regex=True))

# print(data.replace({'DEALSIZE': '[A-Z]'},31,regex=True))

data.replace("medium", method="ffill")      # or bfill


 











import pandas as  pd

# data = pd.read_csv("data/titanic.csv" ,sep='\t', lineterminator='\r')

data = pd.read_csv("data/titanic.csv")

#view preview
# print(data.head())

#remove name attribute from dataset
data.drop(data.columns[[3]],axis=1,inplace=True)

print(data.head())
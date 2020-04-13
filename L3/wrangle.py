import pandas as pd 

data = pd.read_csv("data/titanic.csv")

#preview data
# print(data.head())

#view first column
#print(data.iloc[0])

#view 1st to 7th column
#print(data.iloc[0:8])

#View Fare Column
#print(data.loc[:,["Fare"]])

#View name and fare column
# print(data.loc[:,["Name","Fare"]])
# print(data.loc[2:5,["Name","Fare"]])

#Get the observation based on the string passed
#since it is an equality operation it must match exactly
#print(data.loc[data["Name"] == "Mr. Owen Harris Braund"])

#Group by Sex and Survived, while Pclass is the counter "index"
# print(data.groupby(['Sex','Survived'])['Pclass'].count())

#Get mean of all people in the class

#print(data.groupby('Pclass')['Age'].mean())

#meanAge = data.groupby('Pclass')['Age'].mean().reset_index()
#print(meanAge)


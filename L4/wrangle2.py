import pandas as  pd


#removing duplicates

# raw_data = {'first_name':['Emeka','Emeka','Emeka','Ada','LeBron','Kawhi'],
#             'last_name':['Onyebuchi','Onyebuchi','Onyebuchi','Onyebuchi','James','Leonard'],
#             'age':[42,42,111,35,13,43],
#             'preTestScore':[4,4,4,31,2,3],
#             'postTestScore':[25,25,25,57,62,70]}

# data = pd.DataFrame(raw_data,columns=['first_name','last_name','age','preTestScore','postTestScore'])

# print(data)
# print('*'*20)
# print(data.drop_duplicates())


#Back to wrangling the titanic dataset

data = pd.read_csv("data/titanic.csv")


#find info on all attributes
#print(data.info())


data = data[["Pclass","Sex","Age","Siblings/Spouses Aboard","Parents/Children Aboard","Survived"]]
#print(data.head(15))
#print(data.loc[data["Age"]=="NaN"])

#replace NaN values
#data["Age"].fillna(data["Age"].mean(),inplace=True)

#map alpha to numeric numbers
data['Sex'] = data['Sex'].map({'male':0,'female':1})
#print(data.head(15))
# print(data["Sex"])

data.to_csv('cleansed.csv',sep=",")
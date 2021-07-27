import pandas as pd
#   Question
# li1 = [1,2,3,4,5]
# li2 = [11,22,33,44,55]
# df3 = pd.DataFrame([li1,li2])
#
# print(df3[4][0])    # gives answer how


#   we can use list, tuple or dict to create Series or DataFrame
li1 = [1,2,3,4,5]
s1 = pd.Series(li1)
print(s1)

tup1 = (1,2,3,4,5)
s2 = pd.Series(tup1)
print(s2)

dic1 = {11:10, 12:30, 13:40}
s3 = pd.Series(dic1)
print(s3)

#       we can't use set to create Series or Dataframe as it not have indexiing or keys


li2 = [11,22,33,44,55]
s4 = pd.Series([li1,li2])
print(s4)

df1 = pd.DataFrame(li2)
print(df1)

df2 = pd.DataFrame([li1,li2])
print(df2)

df3 = pd.DataFrame([li1,li2], index=["one","two"])
print(df3)
# print(df3[2][0])

print("check iloc")
print(df3.iloc[0])

print(df3.loc["one"])

dic2 = {"hi":[1,2,3,4,5]}
dic3 = {"python": [11,22,333,44,55]}
dfDic = pd.DataFrame([dic2,dic3], index=["chandra", "language"])
print(dfDic)


dic2 = {"hi":[1,2,3,4,5], "python": [11,22,333,44,55]}
dfDic = pd.DataFrame([dic2])
print(dfDic)

dic2 = {"hi":[1,2,3,4,5], "python": [11,22,333,44,55]}
dfDic = pd.DataFrame(dic2)
print(dfDic)

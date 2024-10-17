import pandas as pd

languages = pd.Series(["Python", "JavaScript", "HTML", "SQL"])
ranking = pd.Series([3,1,2,4])

print(languages)
print(ranking)
#-------------------
# df = pd.DataFrame([("Anne", 30), ("Bill", 27), ("Charlie",55)], columns=["Name", "Age"])
# print(df)
#-------------------
# df = pd.DataFrame({
#     "Languages": languages,
#     "Ranking" : ranking
# })
#-------------------
# df = pd.concat([languages, ranking], axis=1)
# df.columns = ["Languages", "Ranking"]
# print(df)

# df = pd.read_csv("speeds.csv")

# print(df)

df = pd.read_excel("speeds.xlsx")

print(df)
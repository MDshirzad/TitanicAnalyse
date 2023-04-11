import  pandas as pd
from Class import PClass
from Class.People import People,Death,Survived

df = pd.read_csv("Titanic_data.csv")
p = PClass.P_show(dataframe=df)
people=People(df)
deads = Death(df)
Survived = Survived(df)
df_total = df["PassengerId"].count()
print("Total Number of people:",df_total,end='\n')

print("-"*10+"Adults"+"-"*10)
print("Men:",people.men_data(df))
print("Female",people.women_data(df))


print("-"*10+"kids"+"-"*10)

print("Boys:",people.boys_data())
print("Girls",people.girls_data())


print("-"*10+"Deads"+"-"*10)

print("Total:",deads.total_death(df))
print("Men",deads.men_death())
print("Women",deads.women_death())


print("-"*10+"Survived"+"-"*10)

print("Total:",Survived.total_survived(df))
print("Men",Survived.men_survived())
print("Women",Survived.women_survived())


print("-"*10+"PClass Data"+"-"*10)
p.Pclass_1(df)
p.Pclass_2(df)
p.Pclass_3(df)









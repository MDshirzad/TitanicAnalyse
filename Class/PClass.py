import pandas as pd
class P_show:


    def __init__(self,dataframe):
        self.df = dataframe

    @classmethod
    def Pclass_1(self,df):

        PClass_1 = df[df["Pclass"] == 1]
        PClass_1_Survived = PClass_1[PClass_1["Survived"] == 1]

        print("PClass1 Survived:",PClass_1_Survived["PassengerId"].count())
        PClass_1_dead = PClass_1[PClass_1["Survived"] == 0]

    @classmethod
    def Pclass_2(self, df):
        PClass_2 = df[df["Pclass"] == 2]
        PClass_2_Survived = PClass_2[PClass_2["Survived"] == 1]

        print("PClass2 Survived:",PClass_2_Survived["PassengerId"].count())
        PClass_2_dead = PClass_2[PClass_2["Survived"] == 0]

    @classmethod
    def Pclass_3(self, df):
        PClass_3 = df[df["Pclass"] == 3]
        PClass_3_Survived = PClass_3[PClass_3["Survived"] == 1]

        print("PClass3 Survived:",PClass_3_Survived["PassengerId"].count())
        PClass_3_dead = PClass_3[PClass_3["Survived"] == 0]
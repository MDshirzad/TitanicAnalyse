
class People:
    def __init__(self,dataframe):
        self.df=dataframe
        self.Male = dataframe[dataframe["Sex"]=="male"]
        self.Female = dataframe[dataframe["Sex"]=="female"]

    @classmethod


    def men_data(self,df):
        Male = df[df["Sex"] == "male"]
        return Male["PassengerId"].count()


    def women_data(self,df):
        Female = df[df["Sex"] == "female"]
        return Female["PassengerId"].count()


    def boys_data(self):
        Male =self.Male
        boy_kids = Male.where(Male["Age"] <= 11).dropna()
        return boy_kids["PassengerId"].count()

    def girls_data(self):
        Female=self.Female
        girl_kids = Female.where(Female["Age"] <= 11).dropna()
        return girl_kids["PassengerId"].count()

class Death:
    def __init__(self,dataframe):
        self.daf=dataframe
        self.Male = dataframe[dataframe["Sex"]=="male"]
        self.Female = dataframe[dataframe["Sex"]=="female"]


    @classmethod
    def total_death(self,dataframe):
        df=dataframe
        return  df["PassengerId"].where(df["Survived"]==0).count()

    def men_death(self):
        Male = self.Male
        dead_men = Male[Male["Survived"] == 0]
        return  dead_men["PassengerId"].count()

    def women_death(self):
        Female = self.Female
        dead_women = Female[Female["Survived"] == 0]
        return  dead_women["PassengerId"].count()

class Survived:
    def __init__(self,dataframe):
        self.daf=dataframe
        self.Male = dataframe[dataframe["Sex"]=="male"]
        self.Female = dataframe[dataframe["Sex"]=="female"]


    @classmethod
    def total_survived(self,dataframe):
        df=dataframe
        survived = dataframe[dataframe["Survived"]==1]
        return  survived["PassengerId"].count()


    def men_survived(self):
        Male = self.Male
        dead_men = Male[Male["Survived"] == 1]
        return  dead_men["PassengerId"].count()

    def women_survived(self):
        Female = self.Female
        dead_women = Female[Female["Survived"] == 1]
        return  dead_women["PassengerId"].count()



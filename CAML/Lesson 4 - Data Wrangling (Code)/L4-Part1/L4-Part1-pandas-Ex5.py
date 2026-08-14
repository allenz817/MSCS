import pandas as pd

titanic = pd.read_csv('titanic.csv')

titanic['Age'].fillna(value=0, inplace=True)
titanic['Embarked'].fillna(value='Unknown', inplace=True)



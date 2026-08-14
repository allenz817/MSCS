import pandas as pd

titanic = pd.read_csv('titanic.csv')

titanic.loc[titanic['Age'].isnull(), 'Age'] = titanic.loc[titanic['Age'].isnull(), 'Pclass'].map(titanic.groupby('Pclass')['Age'].mean())


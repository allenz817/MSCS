import pandas as pd

titanic = pd.read_csv('titanic.csv')

titanic['FamilySize'] = titanic['Parch'] + titanic['SibSp'] + 1

titanic['FamilySize_Group'] = pd.cut(titanic['FamilySize'], bins=[-1, 1, 2, 3, 4, float('inf')],
                                   labels=['Alone', 'Small', 'Average', 'Large', 'Very Large'])

print(titanic[['Parch', 'SibSp', 'FamilySize', 'FamilySize_Group']].head())

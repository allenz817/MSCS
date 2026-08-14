import pandas as pd

titanic = pd.read_csv('titanic.csv')

# Create age group features
titanic['Age_Group'] = pd.cut(titanic['Age'], bins=[-1, 12, 19, 35, 55, 70, float('inf')],
                             labels=['Child', 'Teenager', 'Young Adult', 'Middle-Aged', 'Older Adult', 'Elderly'])

# Relationship between age groups and survival
print(titanic.groupby('Age_Group')['Survived'].mean())

# Relationship between age groups and passenger class
print(titanic.groupby(['Age_Group', 'Pclass'])['Survived'].mean())

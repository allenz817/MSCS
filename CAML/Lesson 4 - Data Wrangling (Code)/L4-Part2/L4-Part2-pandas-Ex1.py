import pandas as pd

titanic = pd.read_csv('titanic.csv')

titanic = titanic.rename(columns={
    'Pclass': 'Passenger Class',
    'Name': 'Passenger Name',
    'Sex': 'Gender',
    'Age': 'Age',
    'SibSp': 'Siblings/Spouse',
    'Parch': 'Parents/Children',
    'Ticket': 'Ticket Number',
    'Fare': 'Fare Paid',
    'Cabin': 'Cabin Number',
    'Embarked': 'Embarkation Port'
})

print(titanic.head())

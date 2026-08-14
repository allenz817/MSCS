import pandas as pd
from sklearn.impute import KNNImputer

titanic = pd.read_csv('titanic.csv')

imputer = KNNImputer()
titanic['Age'] = imputer.fit_transform(titanic[['Age']])

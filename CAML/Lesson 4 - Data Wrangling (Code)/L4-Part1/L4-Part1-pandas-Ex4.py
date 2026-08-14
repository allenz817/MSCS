import pandas as pd

titanic = pd.read_csv('titanic.csv')

titanic_dropped_cols = titanic.dropna(axis=1, how='any')

print("Original DataFrame shape:", titanic.shape)
print("Modified DataFrame shape:", titanic_dropped_cols.shape)

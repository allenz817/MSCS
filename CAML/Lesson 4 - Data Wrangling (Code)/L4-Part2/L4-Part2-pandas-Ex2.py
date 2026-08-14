import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

titanic = pd.read_csv('titanic.csv')

titanic['Embarked'] = titanic['Embarked'].fillna(titanic['Embarked'].mode()[0])

# Label encoding
label_encoder = LabelEncoder()
titanic['Sex_encoded'] = label_encoder.fit_transform(titanic['Sex'])

# One-hot encoding
embarked_map = {'C': 0, 'Q': 1, 'S': 2}
titanic['Embarked_encoded'] = titanic['Embarked'].map(embarked_map)

one_hot_encoder = OneHotEncoder()
embarked_encoded = one_hot_encoder.fit_transform(titanic[['Embarked_encoded']]).toarray()
embarked_df = pd.DataFrame(embarked_encoded, columns=['Embarked_' + str(int(col)) for col in one_hot_encoder.categories_[0]])
titanic = pd.concat([titanic, embarked_df], axis=1)

print(titanic.head())

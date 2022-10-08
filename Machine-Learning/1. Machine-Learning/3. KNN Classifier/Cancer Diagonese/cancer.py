import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


data = pd.read_csv("KNNAlgorithmDataset.csv")

# column = data.columns
# print(column)

features = data[["radius_mean", "radius_mean", "area_mean", "area_worst", "symmetry_mean"]]
target = data.diagnosis


x = np.array(features).reshape(-1, 5)
y = np.array(target)


x = preprocessing.MinMaxScaler().fit_transform(x)


feature_train, feature_test, target_train, target_test = train_test_split(x, y, test_size=0.25)


model = KNeighborsClassifier(n_neighbors=5)
model.fit(feature_train, target_train)
result = model.predict(feature_test)


print(accuracy_score(target_test, result))






import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import preprocessing


data = pd.read_csv("credit_data.csv")

features = data[["loan", "age", "income"]]
target = data.default

x = np.array(features).reshape(-1, 3)
y = np.array(target)

x = preprocessing.MinMaxScaler().fit_transform(x)

feature_train, feature_test, target_train, target_test = train_test_split(x, y, test_size=0.3)


# self-made cross validation for finding best n-neighbors value
# a = 0
# b = 0
#
# for i in range(1, 100):
#     model = KNeighborsClassifier(n_neighbors=i)
#     fitted = model.fit(feature_train, target_train)
#     predicted = model.predict(feature_test)
#     score = accuracy_score(target_test, predicted)
#
#     if score > a:
#         a = score
#         b = i
#
# print(a)
# print(b)


model = KNeighborsClassifier(n_neighbors=17)
fitted = model.fit(feature_train, target_train)
predicted = model.predict(feature_test)
score = accuracy_score(target_test, predicted)

print(score)

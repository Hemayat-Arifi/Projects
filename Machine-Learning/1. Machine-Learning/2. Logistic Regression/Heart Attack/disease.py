import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix


data = pd.read_csv("heart.csv")

features = data[["age", "sex", "cp", "trestbps", "chol"]]
target = data["target"]

feature_train, feature_test, target_train, target_test = train_test_split(features, target, test_size=0.25)

model = LogisticRegression()

model.fit(feature_train, target_train)

print(model.score(feature_test, target_test))

result = model.predict(feature_test)

print(confusion_matrix(target_test, result))
print(accuracy_score(target_test, result))

print(result)

user = model.predict([[20, 1, 1, 135, 200]])

print(user)

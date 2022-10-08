from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_validate
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris


data = load_iris()

x = data.data
y = data.target

feature_train, feature_test, target_train, target_test = train_test_split(x, y, test_size=0.25)


# model = cross_validate(DecisionTreeClassifier(), x, y, cv=10)
#
# print(model["test_score"])


model = DecisionTreeClassifier(criterion="entropy")
model.fit(feature_train, target_train)
result = model.predict(feature_test)

print(accuracy_score(target_test, result))


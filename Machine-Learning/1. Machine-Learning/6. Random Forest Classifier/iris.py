from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris


data = load_iris()

x = data.data
y = data.target

feature_train, feature_test, target_train, target_test = train_test_split(x, y, test_size=0.3)


model = RandomForestClassifier(n_estimators=1000, criterion="entropy", max_depth=3)
model.fit(feature_train, target_train)
result = model.predict(feature_test)

print(accuracy_score(target_test, result))


from sklearn.datasets import load_breast_cancer
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV


data = load_breast_cancer()

x = data.data
y = data.target

feature_train, feature_test, target_train, target_test = train_test_split(x, y, test_size=0.3)


params = {
    "max_depth": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "criterion": ["gini", "entropy"]
}

model = DecisionTreeClassifier()

model1 = GridSearchCV(model, param_grid=params)

model1.fit(feature_train, target_train)
result = model1.predict(feature_test)

print(accuracy_score(target_test, result))
print(model1.best_params_)



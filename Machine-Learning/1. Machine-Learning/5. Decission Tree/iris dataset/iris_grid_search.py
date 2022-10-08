from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris


data = load_iris()

x = data.data
y = data.target

feature_train, feature_test, target_train, target_test = train_test_split(x, y, test_size=0.25)

params = {
    "max_depth": [1, 2, 3, 4, 5, 6, 7, 8, 9]
}

model = DecisionTreeClassifier()
best_model = GridSearchCV(model, param_grid=params)
best_model.fit(feature_train, target_train)
result = best_model.predict(feature_test)


print(accuracy_score(target_test, result))

print(best_model.best_params_)

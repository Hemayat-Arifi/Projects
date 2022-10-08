from sklearn.datasets import load_iris
from sklearn import svm
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


data = load_iris()

x = data.data
y = data.target

feature_train, feature_test, target_train, target_test = train_test_split(x, y, test_size=0.3)


model = svm.SVC()
fitted_model = model.fit(feature_train, target_train)
result = model.predict(feature_test)

accuracy = accuracy_score(target_test, result)

print(accuracy)




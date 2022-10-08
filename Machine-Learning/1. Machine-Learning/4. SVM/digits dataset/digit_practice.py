from sklearn import metrics, datasets, svm, model_selection
import numpy as np


data = datasets.load_digits()

images = data.images
targets = data.target

x = np.array(images).reshape(len(images), -1)
y = np.array(targets)

feature_train, feature_test, target_train, target_test = model_selection.train_test_split(x, y, test_size=0.25)


model = svm.SVC()
model.fit(feature_train, target_train)
result = model.predict(feature_test)


print(metrics.accuracy_score(target_test, result))


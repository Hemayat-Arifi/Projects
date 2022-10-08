import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


data = pd.read_csv("credit_data.csv")

features = data[["income", "age", "loan"]]
target = data.default


feature_train, feature_test, target_train, target_test = train_test_split(features, target, test_size=0.3)


model = LogisticRegression()
model.fit(feature_train, target_train)

result = model.predict_proba(feature_test)

# print(result)

print(model.score(feature_test, target_test))

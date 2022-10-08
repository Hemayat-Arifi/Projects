import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression


data = pd.read_csv("car_data.csv")

salary = data["AnnualSalary"]
decision = data["Purchased"]

x = np.array(salary).reshape(-1, 1)
y = np.array(decision)


model = LogisticRegression()
model.fit(x, y)

result = model.predict_proba([[3000000]])

print(result)

print(model.score(x, y))

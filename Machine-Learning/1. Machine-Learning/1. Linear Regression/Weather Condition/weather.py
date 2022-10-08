import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.impute import SimpleImputer
import math
import matplotlib.pyplot as plt


data = pd.read_csv("summary_of_weather.csv")


min_temp = data["MIN"]
max_temp = data["MAX"]


x = np.array(min_temp).reshape(-1, 1)
y = np.array(max_temp).reshape(-1, 1)


imp = SimpleImputer(missing_values=np.nan, strategy='mean')
imp.fit(x)


cleaned_x = imp.transform(x)
cleaned_y = imp.transform(y)


model = LinearRegression()
model.fit(cleaned_x, cleaned_y)

score = model.score(cleaned_x, cleaned_y)
# print(score)

#
# plt.scatter(cleaned_x, cleaned_y, color="green")
# plt.plot(cleaned_x, model.predict(cleaned_x), color="black")
# plt.xlabel("Min")
# plt.ylabel("Max")
# plt.title("Tempreture")
# plt.show()
#
user = int(input("enter: \n"))

result = model.predict([[user]])

print(f"predicted max: {result}")



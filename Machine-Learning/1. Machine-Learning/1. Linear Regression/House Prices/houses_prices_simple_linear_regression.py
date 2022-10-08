# TODO: Import our modules

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import math
import matplotlib.pyplot as plt


# TODO: Catch the dataset and analyze it

data = pd.read_csv("house_prices.csv")
price = data.price
size = data.sqft_living


# TODO: Convert dataframes to numpy arrays and reshape it if required

y = np.array(price).reshape(-1, 1)
x = np.array(size).reshape(-1, 1)


# TODO: Build our Model

model = LinearRegression()
model.fit(x, y)


# TODO: Evaluate our Model performance

mse = mean_squared_error(x, y)
mse_resolved = math.sqrt(mse)
score = model.score(x, y)

print(mse)
print(mse_resolved)
print(score)


# TODO: Make Prediction on built model

user = int(input("Please enter size of the house in order to predict the price for you.\n"))
result = model.predict([[user]])

print(f"Your predicted price is {result}")


# TODO: Visualize our model via matplotlib

plt.scatter(x, y, color="red")
plt.plot(x, model.predict(x), color="black")
plt.title("Hemo Linear Regression")
plt.xlabel("Size")
plt.ylabel("price")
plt.show()

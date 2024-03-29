# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19a87O5jNlL8o4ylGtnhdJZg7BodpweIc
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

a = pd.read_csv("daily_min_temperatures.csv", usecols=[1])

Previous_number_of_features = 5

data = a.values

plt.plot(data)
plt.show()

data = data.astype("float32")

scalar = MinMaxScaler((0, 1))
normalized_data = scalar.fit_transform(data)

train, test = train_test_split(normalized_data, test_size=0.3)

print(train.shape)
print(test.shape)

# we define a function to make features with its labels
def reconstruct_data(train_or_test, n):
  x, y = [], []

  for i in range(len(train_or_test) - n - 1):
    a = train_or_test[i:(i + n), 0]
    x.append(a)
    y.append(train_or_test[i + n, 0])

  return np.array(x), np.array(y)

train_x, train_y = reconstruct_data(train, Previous_number_of_features)
test_x, test_y = reconstruct_data(train, Previous_number_of_features)

train_x = np.reshape(train_x, (train_x.shape[0], 1, train_x.shape[1]))
test_x = np.reshape(test_x, (test_x.shape[0], 1, test_x.shape[1]))

# when we have another LSTM in next layer so we set return_sequence=True in its previous LSTM layer as parameter

model = Sequential()
model.add(LSTM(100, return_sequences=True, input_shape=(1, Previous_number_of_features)))
model.add(Dropout(0.5))
model.add(LSTM(50, return_sequences=True))
model.add(Dropout(0.3))
model.add(LSTM(50))
model.add(Dropout(0.3))
model.add(Dense(1))

model.compile(loss="mean_squared_error", optimizer="adam")
model.fit(train_x, train_y, epochs=10, verbose=2, batch_size=16)

result = model.predict(test_x)

test_predict = scalar.inverse_transform(result)
test_label = scalar.inverse_transform([test_y])

print(test_predict)
print(test_label)

plt.plot(test_predict[:10], color="red")
plt.show()

plt.plot(test_label[0][:10], color="green")
plt.show()
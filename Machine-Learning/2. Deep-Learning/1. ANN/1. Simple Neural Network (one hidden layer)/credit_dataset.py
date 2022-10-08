# -*- coding: utf-8 -*-
"""credit_dataset.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AuUUuHAqOgNQWSia-ngKk8DbdyOcN9BU
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizer_v2.adam import Adam
from keras.optimizer_experimental.adadelta import optimizer

data = pd.read_csv("credit_data.csv")

features = data[["loan", "age", "income"]]
labels = data.default
y = np.array(labels).reshape(-1, 1)

encoder = OneHotEncoder()
target = encoder.fit_transform(y).toarray()

feature_train, feature_test, target_train, target_test = train_test_split(features, target, test_size=0.3)

model = Sequential()
model.add(Dense(10, input_dim=3, activation="sigmoid"))
model.add(Dense(2, activation="softmax"))

model.compile(optimizer=Adam(learning_rate=0.0005), loss="categorical_crossentropy", metrics=["accuracy"])
model.fit(feature_train, target_train, verbose=2, epochs=1000)
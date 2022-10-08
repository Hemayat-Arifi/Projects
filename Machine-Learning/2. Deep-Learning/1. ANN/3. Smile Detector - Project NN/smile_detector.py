import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
from PIL import Image
import os


image_list = os.listdir("smiles_dataset/training_set")
test_images = os.listdir("smiles_dataset/test_set")

features = []
labels = []


# Reading Images Pixel intensities and converting them to bytes

for i in image_list:
    a = Image.open("smiles_dataset/training_set/" + i).convert("1")
    b = list(a.getdata())
    features.append(b)
    if i[:5] == "happy":
        labels.append([1, 0])
    else:
        labels.append([0, 1])


x = np.array(features)
y = np.array(labels)

# min-max normalization of features
x = x / 255.0


# Specifying optimizers parameters

opt = Adam(learning_rate=0.005)


# Building The Model

model = Sequential()
model.add(Dense(1024, input_dim=1024, activation="relu"))
model.add(Dense(512, activation="relu"))
model.add(Dense(128, activation="relu"))
model.add(Dense(2, activation="softmax"))

model.compile(optimizer=opt, loss="categorical_crossentropy", metrics=["accuracy"])

model.fit(x, y, batch_size=10, verbose=2, epochs=100)


result = model.evaluate(x, y)


test_list_sad = []
test_sad = Image.open("smiles_dataset/test_set/sad_test.png").convert("1")
test_list_sad.append(list(test_sad.getdata()))
sad = np.array(test_list_sad) / 255.0

test_list_happy = []
test_happy = Image.open("smiles_dataset/test_set/happy_test.png").convert("1")
test_list_happy.append(list(test_happy.getdata()))
happy = np.array(test_list_happy) / 255.0


prediction = model.predict(happy)

new = prediction.round()
if str(new) == "[[0. 1.]]":
    print("Sad")
else:
    print("Happy")


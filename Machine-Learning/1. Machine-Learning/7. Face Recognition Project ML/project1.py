import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.datasets import fetch_olivetti_faces


data = fetch_olivetti_faces()

features = data.data
target = data.target

print(features)


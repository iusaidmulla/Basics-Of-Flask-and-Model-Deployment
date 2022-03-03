import pandas as pd
import numpy as np
import pickle
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier

print("All Libraries loaded")

# read in the iris data
iris = load_iris()
# create X (features) and y (response)
X = iris.data
y = iris.target

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

knn = KNeighborsClassifier(n_neighbors = 4)
knn.fit(X_train,y_train)

print("Model building finished")

#saving the model in .pkl format
pickle.dump(knn, open('iri_knn.pkl', 'wb'))

print("Pickle file dumped")

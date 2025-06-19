import math
from sklearn.datasets import load_iris
import pandas as pd
import matplotlib.pyplot as plt

iris = load_iris()
iris_data = iris.data
iris_data_pd = pd.DataFrame(
    iris_data, columns=iris.feature_names)
petals = pd.DataFrame(iris_data_pd.values[:, 2:4], 
           columns=["petal length (cm)", "petal width (cm)"])
plt.scatter(petals.values[:,0], petals.values[:,1])
plt.show()

from sklearn.cluster import KMeans
plt.figure(figsize=(7, 5))
km = KMeans(n_clusters=2, random_state=20)
km.fit(iris_data_pd.iloc[:, 2:4])
yPred = km.predict(iris_data_pd.iloc[:, 2:4])
plt.scatter(iris_data_pd.iloc[:,2], 
            iris_data_pd.iloc[:, 3], c=yPred)
plt.title("Clustering")
plt.xlabel("petal length")
plt.ylabel("petal width")
plt.show()
km.predict(iris_data_pd.iloc[:, 2:4])
print(iris_data_pd.iloc[98, 2:4])
print(km.cluster_centers_)
<<<<<<< HEAD
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
# plt.scatter(petals.values[:,0], petals.values[:,1])
# plt.show()

from sklearn.cluster import KMeans
plt.figure(figsize=(7, 5))
km = KMeans(n_clusters=2, random_state=20)
km.fit(iris_data_pd.iloc[:, 2:4])
yPred = km.predict(iris_data_pd.iloc[:, 2:4])
# plt.scatter(iris_data_pd.iloc[:,2], 
#             iris_data_pd.iloc[:, 3], c=yPred)
# plt.title("Clustering")
# plt.xlabel("petal length")
# plt.ylabel("petal width")
# plt.show()
km.predict(iris_data_pd.iloc[:, 2:4])

print(iris_data_pd.iloc[98, 2:4])
print(km.cluster_centers_)

def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    squared = dx**2 + dy **2
    result = math.sqrt(squared)
    return result

print("0 cluster dist. :", distance(iris_data_pd.iloc[98,2],    iris_data_pd.iloc[98,3], 
                                    km.cluster_centers_[0][0],  km.cluster_centers_[0][1]))
print("1 cluster dist. :", distance(iris_data_pd.iloc[98,2],    iris_data_pd.iloc[98,3], 
                                    km.cluster_centers_[1][0],  km.cluster_centers_[1][1]))
# n_cluster = [3,4,6,12]
# for i in n_cluster:
#     count = 1
#     km = KMeans(n_clusters=i, random_state=20)

#     km.fit(iris_data_pd.iloc[:, 2:4])
#     yPred = km.predict(iris_data_pd.iloc[:, 2:4])
#     plt.figure(figsize=(7, 5))
#     plt.scatter(iris_data_pd.iloc[:,2], 
#                 iris_data_pd.iloc[:, 3], c=yPred)
#     plt.title("Clustering = " + str(i))
#     plt.xlabel("petal length")
#     plt.ylabel("petal width")
#     count = count + 1
#     plt.show()

km = KMeans(n_clusters=8, random_state=20)
km.fit(iris_data_pd.iloc[:, 2:4])
yPred = km.predict(iris_data_pd.iloc[:, 2:4])
plt.figure(figsize=(7, 5))
# plt.scatter(iris_data_pd.iloc[:,2], 
#             iris_data_pd.iloc[:, 3], c=yPred)
# plt.title("Clustering")
# plt.xlabel("petal length")
# plt.ylabel("petal width")
# plt.show()

import numpy as np
h = 0.02
xMin, xMax = iris_data_pd.iloc[:,2].min() - 1, iris_data_pd.iloc[:,2].max() + 1
yMin, yMax = iris_data_pd.iloc[:,3].min() - 1, iris_data_pd.iloc[:,3].max() + 1
xx, yy = np.meshgrid(np.arange(xMin, xMax, h), np.arange(yMin, yMax, h))
Z = km.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
plt.figure(1)
plt.clf()
# plt.imshow(Z, interpolation="nearest", extent=(xx.min(), xx.max(), yy.min(), yy.max()),
#            origin="lower")
# plt.plot(iris_data_pd.iloc[:,2], 
#             iris_data_pd.iloc[:, 3], "bo", markersize=2 )
# centroids = km.cluster_centers_
# plt.scatter(centroids[:,0], centroids[:,1], marker="^", s=16, linewidths=3, color="r", zorder=10)
# plt.title("Clustering")
# plt.xlim(xMin, xMax)
# plt.ylim(yMin, yMax)
# plt.show()
from sklearn.cluster import AgglomerativeClustering, DBSCAN
linkage = ["complete", "average", "ward"]
for idx, i in enumerate(linkage):
    plt.figure(idx)
    hier = AgglomerativeClustering(n_clusters=3, metric="euclidean", linkage=i)
    hier.fit(iris_data_pd.iloc[:,2:4])
    plt.scatter(iris_data_pd.iloc[:, 2], iris_data_pd.iloc[:, 3], c=hier.labels_)
    plt.title("Clustering"+i)
    plt.xlabel("petal length")
    plt.ylabel("petal width")
plt.show()

db = DBSCAN(eps= 0.5, min_samples=7)
db.fit(iris_data_pd.iloc[:, 2:4] )
yPred = db.fit_predict(iris_data_pd.iloc[:, 2:4] )
plt.scatter(iris_data_pd.iloc[:, 2], iris_data_pd.iloc[:, 3], c=yPred)
plt.title("Density Clustering")
plt.xlabel("petal length")
plt.ylabel("petal width")
=======
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
# plt.scatter(petals.values[:,0], petals.values[:,1])
# plt.show()

from sklearn.cluster import KMeans
plt.figure(figsize=(7, 5))
km = KMeans(n_clusters=2, random_state=20)
km.fit(iris_data_pd.iloc[:, 2:4])
yPred = km.predict(iris_data_pd.iloc[:, 2:4])
# plt.scatter(iris_data_pd.iloc[:,2], 
#             iris_data_pd.iloc[:, 3], c=yPred)
# plt.title("Clustering")
# plt.xlabel("petal length")
# plt.ylabel("petal width")
# plt.show()
km.predict(iris_data_pd.iloc[:, 2:4])

print(iris_data_pd.iloc[98, 2:4])
print(km.cluster_centers_)

def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    squared = dx**2 + dy **2
    result = math.sqrt(squared)
    return result

print("0 cluster dist. :", distance(iris_data_pd.iloc[98,2],    iris_data_pd.iloc[98,3], 
                                    km.cluster_centers_[0][0],  km.cluster_centers_[0][1]))
print("1 cluster dist. :", distance(iris_data_pd.iloc[98,2],    iris_data_pd.iloc[98,3], 
                                    km.cluster_centers_[1][0],  km.cluster_centers_[1][1]))
# n_cluster = [3,4,6,12]
# for i in n_cluster:
#     count = 1
#     km = KMeans(n_clusters=i, random_state=20)

#     km.fit(iris_data_pd.iloc[:, 2:4])
#     yPred = km.predict(iris_data_pd.iloc[:, 2:4])
#     plt.figure(figsize=(7, 5))
#     plt.scatter(iris_data_pd.iloc[:,2], 
#                 iris_data_pd.iloc[:, 3], c=yPred)
#     plt.title("Clustering = " + str(i))
#     plt.xlabel("petal length")
#     plt.ylabel("petal width")
#     count = count + 1
#     plt.show()

km = KMeans(n_clusters=8, random_state=20)
km.fit(iris_data_pd.iloc[:, 2:4])
yPred = km.predict(iris_data_pd.iloc[:, 2:4])
plt.figure(figsize=(7, 5))
# plt.scatter(iris_data_pd.iloc[:,2], 
#             iris_data_pd.iloc[:, 3], c=yPred)
# plt.title("Clustering")
# plt.xlabel("petal length")
# plt.ylabel("petal width")
# plt.show()

import numpy as np
h = 0.02
xMin, xMax = iris_data_pd.iloc[:,2].min() - 1, iris_data_pd.iloc[:,2].max() + 1
yMin, yMax = iris_data_pd.iloc[:,3].min() - 1, iris_data_pd.iloc[:,3].max() + 1
xx, yy = np.meshgrid(np.arange(xMin, xMax, h), np.arange(yMin, yMax, h))
Z = km.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
plt.figure(1)
plt.clf()
# plt.imshow(Z, interpolation="nearest", extent=(xx.min(), xx.max(), yy.min(), yy.max()),
#            origin="lower")
# plt.plot(iris_data_pd.iloc[:,2], 
#             iris_data_pd.iloc[:, 3], "bo", markersize=2 )
# centroids = km.cluster_centers_
# plt.scatter(centroids[:,0], centroids[:,1], marker="^", s=16, linewidths=3, color="r", zorder=10)
# plt.title("Clustering")
# plt.xlim(xMin, xMax)
# plt.ylim(yMin, yMax)
# plt.show()
from sklearn.cluster import AgglomerativeClustering, DBSCAN
linkage = ["complete", "average", "ward"]
for idx, i in enumerate(linkage):
    plt.figure(idx)
    hier = AgglomerativeClustering(n_clusters=3, metric="euclidean", linkage=i)
    hier.fit(iris_data_pd.iloc[:,2:4])
    plt.scatter(iris_data_pd.iloc[:, 2], iris_data_pd.iloc[:, 3], c=hier.labels_)
    plt.title("Clustering"+i)
    plt.xlabel("petal length")
    plt.ylabel("petal width")
plt.show()

db = DBSCAN(eps= 0.5, min_samples=7)
db.fit(iris_data_pd.iloc[:, 2:4] )
yPred = db.fit_predict(iris_data_pd.iloc[:, 2:4] )
plt.scatter(iris_data_pd.iloc[:, 2], iris_data_pd.iloc[:, 3], c=yPred)
plt.title("Density Clustering")
plt.xlabel("petal length")
plt.ylabel("petal width")
>>>>>>> origin
plt.show()
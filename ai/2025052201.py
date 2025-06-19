<<<<<<< HEAD
from sklearn.datasets import load_iris, load_wine, load_diabetes
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import scikitplot as skplt
from sklearn.datasets import load_breast_cancer # pip install scikit-learn
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

data = load_wine()
data = load_diabetes()
# X_train, X_test, y_train, y_test = train_test_split(
#     data.data, data.target, test_size=0.33, random_state=42)

xTrain, xTest, yTrain, yTest = train_test_split(data.data, data.target, random_state=42)
model = LinearRegression()
model.fit(xTrain, yTrain)
score = model.score(xTest, yTest)
print("LinearRegression score :", score)

ridge = Ridge(alpha=1.0)
ridge.fit(xTrain, yTrain)
score = ridge.score(xTest, yTest)
print("-----------Ridge-------------")
print("Ridge score :", score)

ridge = Lasso(alpha=1.0)
ridge.fit(xTrain, yTrain)
score = ridge.score(xTest, yTest)
print("-----------Lasso-------------")
print("Lasso score :", score)

ridge = ElasticNet(alpha=1.0, l1_ratio=0.5)
ridge.fit(xTrain, yTrain)
score = ridge.score(xTest, yTest)
print("-----------ElasticNet-------------")
print("ElasticNet score :", score)

#과제1 : 정규화 선형회귀 모델별 가중치 비교 코딩
#과제2 : bicycle 예제를 Ridge/Lasso/ElasticNet로 바꿔서 실행

dataset = load_iris()
data = pd.DataFrame(dataset.data, columns=dataset.feature_names)
xTrain, xTest, yTrain, yTest = train_test_split(data, dataset.target, 
                                                random_state=42)


mms = MinMaxScaler()
xTrainScaled = mms.fit_transform(xTrain)
xTestScaled = mms.fit_transform(xTest)
print(xTestScaled)

model = KNeighborsClassifier(n_neighbors=5)
model.fit(xTrain, yTrain)   #   [0, 1,2,3,4,6,8,8,34,55,67,78]
pred = model.predict(xTest) #   [7]          |
                            #           Y(3), Y(4), ...Y(8)
                            #    +- virginica(?)
scoreXTrain = accuracy_score(yTest, pred)

model.fit(xTrainScaled, yTrain)
predScaled = model.predict(xTestScaled)
scoreXTrainScaled = accuracy_score(yTest, pred)

print(scoreXTrain, " : " , scoreXTrainScaled)

# Scale 전 후 그래프 변화(?)
print("xTrainScaled.dtype :", xTrainScaled.dtype)
xTrain.plot(kind="box")
plt.title("xTrain")
# plt.show()
xTest.plot(kind="box")
plt.title("xTest")
# plt.show()
xTrainScaledDataFrame = pd.DataFrame(data=xTrainScaled)
xTestScaledDataFrame = pd.DataFrame(data=xTestScaled)
xTrainScaledDataFrame.plot(kind="box")
plt.title("xTrainScaled")
# plt.show()
xTestScaledDataFrame.plot(kind="box")
plt.title("xTestScaled")
=======
from sklearn.datasets import load_iris, load_wine, load_diabetes
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import scikitplot as skplt
from sklearn.datasets import load_breast_cancer # pip install scikit-learn
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

data = load_wine()
data = load_diabetes()
# X_train, X_test, y_train, y_test = train_test_split(
#     data.data, data.target, test_size=0.33, random_state=42)

xTrain, xTest, yTrain, yTest = train_test_split(data.data, data.target, random_state=42)
model = LinearRegression()
model.fit(xTrain, yTrain)
score = model.score(xTest, yTest)
print("LinearRegression score :", score)

ridge = Ridge(alpha=1.0)
ridge.fit(xTrain, yTrain)
score = ridge.score(xTest, yTest)
print("-----------Ridge-------------")
print("Ridge score :", score)

ridge = Lasso(alpha=1.0)
ridge.fit(xTrain, yTrain)
score = ridge.score(xTest, yTest)
print("-----------Lasso-------------")
print("Lasso score :", score)

ridge = ElasticNet(alpha=1.0, l1_ratio=0.5)
ridge.fit(xTrain, yTrain)
score = ridge.score(xTest, yTest)
print("-----------ElasticNet-------------")
print("ElasticNet score :", score)

#과제1 : 정규화 선형회귀 모델별 가중치 비교 코딩
#과제2 : bicycle 예제를 Ridge/Lasso/ElasticNet로 바꿔서 실행

dataset = load_iris()
data = pd.DataFrame(dataset.data, columns=dataset.feature_names)
xTrain, xTest, yTrain, yTest = train_test_split(data, dataset.target, 
                                                random_state=42)


mms = MinMaxScaler()
xTrainScaled = mms.fit_transform(xTrain)
xTestScaled = mms.fit_transform(xTest)
print(xTestScaled)

model = KNeighborsClassifier(n_neighbors=5)
model.fit(xTrain, yTrain)   #   [0, 1,2,3,4,6,8,8,34,55,67,78]
pred = model.predict(xTest) #   [7]          |
                            #           Y(3), Y(4), ...Y(8)
                            #    +- virginica(?)
scoreXTrain = accuracy_score(yTest, pred)

model.fit(xTrainScaled, yTrain)
predScaled = model.predict(xTestScaled)
scoreXTrainScaled = accuracy_score(yTest, pred)

print(scoreXTrain, " : " , scoreXTrainScaled)

# Scale 전 후 그래프 변화(?)
print("xTrainScaled.dtype :", xTrainScaled.dtype)
xTrain.plot(kind="box")
plt.title("xTrain")
# plt.show()
xTest.plot(kind="box")
plt.title("xTest")
# plt.show()
xTrainScaledDataFrame = pd.DataFrame(data=xTrainScaled)
xTestScaledDataFrame = pd.DataFrame(data=xTestScaled)
xTrainScaledDataFrame.plot(kind="box")
plt.title("xTrainScaled")
# plt.show()
xTestScaledDataFrame.plot(kind="box")
plt.title("xTestScaled")
>>>>>>> origin
plt.show()
<<<<<<< HEAD
from sklearn.datasets import load_iris
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

data = load_iris()
# print(data.keys())
# print(data.DESCR)
features = pd.DataFrame(data=data.data,
            columns=data.feature_names)
# print(features.head)

target = pd.DataFrame(data.target, columns=["species"])
iris = pd.concat([features, target], axis=1)
print(iris.head)
iris.rename({"sepal length (cm)":"sepalLength", "sepal width (cm)":"sepalWidth", 
             "petal length (cm)":"petalLength", "petal width (cm)":"petalWidth"}, 
             axis=1, inplace=True)
# iris["species"] = iris.species.map(lambda x:data.target_names[x])
# print(iris)
# print(iris.isna().sum(axis=0))
# print(iris.info())
# print(iris.describe())
# print(iris.corr())
# print(iris.groupby("species").size())

def boxplot_iris(feature_names, dataset) :
  i = 1
  plt.figure(figsize=(11,9))
  for col in feature_names :
    plt.subplot(2,2,i)
    plt.axis("on")
    plt.tick_params(axis='both', left=True, top=False, right=False, 
                    bottom=True, labelleft=False, labeltop=False, 
                    labelright=False, labelbottom=False)
    dataset[col].plot(kind='box', subplots=True, sharex=False, sharey=False)
    plt.title(col)
    i += 1
  # plt.show()

boxplot_iris(iris.columns[:-1], iris)

def histogram_iris(feature_names, dataset) :
  i = 1
  plt.figure(figsize=(11,9))
  for col in feature_names :
    plt.subplot(2,2,i)
    plt.axis("on")
    plt.tick_params(axis='both', left=True, top=False, right=False, 
                    bottom=False, labelleft=False, labeltop=False, 
                    labelright=False, labelbottom=False)
    dataset[col].hist()
    plt.title(col)
    i += 1
  # plt.show()

histogram_iris(iris.columns[:-1], iris)

corr = iris.corr()
cmap = sns.diverging_palette(220, 10, as_cmap=True)
plt.figure(figsize=(11, 9))
sns.heatmap(corr, cmap=cmap, vmax=1.0, vmin=-1.0, square=True, linewidths=.5, cbar_kws={"shrink":0.5})
# plt.show()

sns.pairplot(iris, hue="species")
# plt.show()

from sklearn.model_selection import train_test_split
xTrain, xTest, yTrain, yTest = train_test_split(
    iris.iloc[:, :-1], iris.iloc[:, -1], test_size=0.33, # 0.2 -> 100%(cv=91.67), 0.33 -> 98%(cv=93%), 0.4 -> 96.7%(cv=92%)
    random_state=42, shuffle=True) # 과제 2.  shuffle = False로 해서 위의 세가지 경우를 수행해 볼 것
print(yTest.describe)

from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier(
    criterion='gini', splitter='best',
    max_depth=None, min_samples_split=2,
    min_samples_leaf=1, min_weight_fraction_leaf = 0.0,
    max_features=None, random_state=42, 
    max_leaf_nodes=None, min_impurity_decrease=0.0#,
    # min_impurity_split = None, class_weight=None
    # presort = False
)
print(model)
print(model.fit(xTrain, yTrain))
print(model.score(xTest, yTest))
# 150 샘플 -> 100개 학습, 50개로 검증, 1개 틀림
# 과제>iris 데이터 : (sepal length,  sepal width,  petal length,  petal width)
#  =                     5.0            3.7            7.3           2.1
# -> 품종 맞추기 : 안 맞았을 경우 pair plot을 놓고 여집합 위치에서 데이터를 10개 뽑아서 테스트하고 
#    실제 정확도를 체크해 본다.


from sklearn.model_selection import cross_val_score, KFold, StratifiedKFold
cv = KFold(n_splits = 5, shuffle = True, random_state = 42)
results = cross_val_score(model, xTrain, yTrain, cv = cv)
fin_result = np.mean(results)

for i, result in enumerate(results):
  print("{}번째 교차검증 정확도 : {}".format(i, result))
print("교차검증 최종 정확도 : {}".format(fin_result))


cv1 = StratifiedKFold(n_splits = 10, shuffle = True, random_state = 42)
results = cross_val_score(model, xTrain, yTrain, cv = cv1)
fin_result = np.mean(results)

for i, result in enumerate(results):
  print("{}번째 Stratified 교차검증 정확도 : {}".format(i, result))
print("Stratified 교차검증 최종 정확도 : {}".format(fin_result))

import scikitplot as skplt
skplt.estimators.plot_learning_curve(model, xTrain, yTrain, figsize=(6,6))
# plt.show()

# 과제> 아래의 모델을 사용하여 학습하여 성능을 측정하고 k-Fold로 cv를 수행하여 나온 결과와 비교해 보세요.
# KFold를 사용할 경우
model = DecisionTreeClassifier(
  criterion='entropy', splitter='random', max_depth=8, 
  random_state=142
)

# StratifiedKFold를 사용할 경우
model = DecisionTreeClassifier(
  criterion='entropy', splitter='random', max_depth=6, 
  random_state=78
)

from sklearn.model_selection import GridSearchCV
estimator = DecisionTreeClassifier()
parameters={
    "criterion":['gini', "entropy"], 
    "splitter":['best', "random"],
    "max_depth":[4,6,8,10,12], 
    "min_weight_fraction_leaf" : [0.0,0.1,0.2,0.3],
    "random_state" : [7, 23, 42, 78, 142],
    "min_impurity_decrease" : [0.0,0.05,0.1,0.2]
}
model = GridSearchCV(estimator=estimator, param_grid=parameters,
                     cv = cv1, verbose = 1, n_jobs = -1, 
                     refit = True)
model.fit(xTrain, yTrain)
print("Best Estimator: \n", model.best_estimator_)
print("\nBest Params: \n", model.best_params_)
print("\nBest Score: \n", model.best_score_)

model = DecisionTreeClassifier(criterion='entropy', max_depth=4, random_state=23,
                       splitter='random')
model.fit(xTrain, yTrain)
print("GSCV model score =", model.score(xTest, yTest))

from sklearn.metrics import accuracy_score, confusion_matrix
pred = model.predict(xTest)
acc = accuracy_score(yTest, pred)
print("Accracy :", acc)

confMatrix = confusion_matrix(yTest, pred)
print("Confusion Matrix :\n", confMatrix)

=======
from sklearn.datasets import load_iris
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

data = load_iris()
# print(data.keys())
# print(data.DESCR)
features = pd.DataFrame(data=data.data,
            columns=data.feature_names)
# print(features.head)

target = pd.DataFrame(data.target, columns=["species"])
iris = pd.concat([features, target], axis=1)
print(iris.head)
iris.rename({"sepal length (cm)":"sepalLength", "sepal width (cm)":"sepalWidth", 
             "petal length (cm)":"petalLength", "petal width (cm)":"petalWidth"}, 
             axis=1, inplace=True)
# iris["species"] = iris.species.map(lambda x:data.target_names[x])
# print(iris)
# print(iris.isna().sum(axis=0))
# print(iris.info())
# print(iris.describe())
# print(iris.corr())
# print(iris.groupby("species").size())

def boxplot_iris(feature_names, dataset) :
  i = 1
  plt.figure(figsize=(11,9))
  for col in feature_names :
    plt.subplot(2,2,i)
    plt.axis("on")
    plt.tick_params(axis='both', left=True, top=False, right=False, 
                    bottom=True, labelleft=False, labeltop=False, 
                    labelright=False, labelbottom=False)
    dataset[col].plot(kind='box', subplots=True, sharex=False, sharey=False)
    plt.title(col)
    i += 1
  # plt.show()

boxplot_iris(iris.columns[:-1], iris)

def histogram_iris(feature_names, dataset) :
  i = 1
  plt.figure(figsize=(11,9))
  for col in feature_names :
    plt.subplot(2,2,i)
    plt.axis("on")
    plt.tick_params(axis='both', left=True, top=False, right=False, 
                    bottom=False, labelleft=False, labeltop=False, 
                    labelright=False, labelbottom=False)
    dataset[col].hist()
    plt.title(col)
    i += 1
  # plt.show()

histogram_iris(iris.columns[:-1], iris)

corr = iris.corr()
cmap = sns.diverging_palette(220, 10, as_cmap=True)
plt.figure(figsize=(11, 9))
sns.heatmap(corr, cmap=cmap, vmax=1.0, vmin=-1.0, square=True, linewidths=.5, cbar_kws={"shrink":0.5})
# plt.show()

sns.pairplot(iris, hue="species")
# plt.show()

from sklearn.model_selection import train_test_split
xTrain, xTest, yTrain, yTest = train_test_split(
    iris.iloc[:, :-1], iris.iloc[:, -1], test_size=0.33, # 0.2 -> 100%(cv=91.67), 0.33 -> 98%(cv=93%), 0.4 -> 96.7%(cv=92%)
    random_state=42, shuffle=True) # 과제 2.  shuffle = False로 해서 위의 세가지 경우를 수행해 볼 것
print(yTest.describe)

from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier(
    criterion='gini', splitter='best',
    max_depth=None, min_samples_split=2,
    min_samples_leaf=1, min_weight_fraction_leaf = 0.0,
    max_features=None, random_state=42, 
    max_leaf_nodes=None, min_impurity_decrease=0.0#,
    # min_impurity_split = None, class_weight=None
    # presort = False
)
print(model)
print(model.fit(xTrain, yTrain))
print(model.score(xTest, yTest))
# 150 샘플 -> 100개 학습, 50개로 검증, 1개 틀림
# 과제>iris 데이터 : (sepal length,  sepal width,  petal length,  petal width)
#  =                     5.0            3.7            7.3           2.1
# -> 품종 맞추기 : 안 맞았을 경우 pair plot을 놓고 여집합 위치에서 데이터를 10개 뽑아서 테스트하고 
#    실제 정확도를 체크해 본다.


from sklearn.model_selection import cross_val_score, KFold, StratifiedKFold
cv = KFold(n_splits = 5, shuffle = True, random_state = 42)
results = cross_val_score(model, xTrain, yTrain, cv = cv)
fin_result = np.mean(results)

for i, result in enumerate(results):
  print("{}번째 교차검증 정확도 : {}".format(i, result))
print("교차검증 최종 정확도 : {}".format(fin_result))


cv1 = StratifiedKFold(n_splits = 10, shuffle = True, random_state = 42)
results = cross_val_score(model, xTrain, yTrain, cv = cv1)
fin_result = np.mean(results)

for i, result in enumerate(results):
  print("{}번째 Stratified 교차검증 정확도 : {}".format(i, result))
print("Stratified 교차검증 최종 정확도 : {}".format(fin_result))

import scikitplot as skplt
skplt.estimators.plot_learning_curve(model, xTrain, yTrain, figsize=(6,6))
# plt.show()

# 과제> 아래의 모델을 사용하여 학습하여 성능을 측정하고 k-Fold로 cv를 수행하여 나온 결과와 비교해 보세요.
# KFold를 사용할 경우
model = DecisionTreeClassifier(
  criterion='entropy', splitter='random', max_depth=8, 
  random_state=142
)

# StratifiedKFold를 사용할 경우
model = DecisionTreeClassifier(
  criterion='entropy', splitter='random', max_depth=6, 
  random_state=78
)

from sklearn.model_selection import GridSearchCV
estimator = DecisionTreeClassifier()
parameters={
    "criterion":['gini', "entropy"], 
    "splitter":['best', "random"],
    "max_depth":[4,6,8,10,12], 
    "min_weight_fraction_leaf" : [0.0,0.1,0.2,0.3],
    "random_state" : [7, 23, 42, 78, 142],
    "min_impurity_decrease" : [0.0,0.05,0.1,0.2]
}
model = GridSearchCV(estimator=estimator, param_grid=parameters,
                     cv = cv1, verbose = 1, n_jobs = -1, 
                     refit = True)
model.fit(xTrain, yTrain)
print("Best Estimator: \n", model.best_estimator_)
print("\nBest Params: \n", model.best_params_)
print("\nBest Score: \n", model.best_score_)

model = DecisionTreeClassifier(criterion='entropy', max_depth=4, random_state=23,
                       splitter='random')
model.fit(xTrain, yTrain)
print("GSCV model score =", model.score(xTest, yTest))

from sklearn.metrics import accuracy_score, confusion_matrix
pred = model.predict(xTest)
acc = accuracy_score(yTest, pred)
print("Accracy :", acc)

confMatrix = confusion_matrix(yTest, pred)
print("Confusion Matrix :\n", confMatrix)

>>>>>>> origin

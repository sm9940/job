from sklearn.datasets import load_iris, load_wine
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import scikitplot as skplt
from sklearn.datasets import load_breast_cancer # pip install scikit-learn
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LinearRegression

data = load_iris()
xTrain, xTest, yTrain, yTest = train_test_split(data.data, data.target, test_size=0.33, shuffle=True)

# model = DecisionTreeClassifier(criterion='entropy', max_depth=4, random_state=23,
#                        splitter='random')
model = DecisionTreeClassifier(
    criterion='gini', splitter='best',
    max_depth=None, min_samples_split=2
)
model.fit(xTrain, yTrain)
print("GSCV model score =", model.score(xTest, yTest))

from sklearn.metrics import accuracy_score, confusion_matrix
pred = model.predict(xTest)
acc = accuracy_score(yTest, pred)
print("Accracy :", acc)

confMatrix = confusion_matrix(yTest, pred)
print("Confusion Matrix :\n", confMatrix)

# skplt.metrics.plot_confusion_matrix(yTest, pred, figsize=(8,6))
# plt.show()

from sklearn.metrics import precision_score
precisions = precision_score(yTest, pred, average=None)

for target, score in zip(data.target_names, precisions) :
    print(f"{target}의 정밀도 : {score}")

from sklearn.metrics import recall_score
recalls = recall_score(yTest, pred, average=None)

for target, score in zip(data.target_names, recalls) :
    print(f"{target}의 재현율 : {score}")

print("-------------------------------------------------------")

from sklearn.metrics import f1_score, fbeta_score, classification_report
fbetas = fbeta_score(yTest, pred, beta =0.5, average=None)

for target, score in zip(data.target_names, fbetas) :
    print(f"{target}의 f점수(beta=0.5): {score}")
print("-------------------------------------------------------")

f1s = f1_score(yTest, model.predict(xTest), average=None)

for target, score in zip(data.target_names, f1s) :
    print(f"{target}의 f점수(beta=1): {score}")
print("-------------------------------------------------------")
classReport = classification_report(yTest, pred)
print("Classification Report : \n", classReport)

print(list(yTest))
print("=====================")
print(pred)

import scikitplot as skplt
# nb = GaussianNB()
# nb = nb.fit(xTrain, yTrain)
# y_probas = nb.predict_proba(xTest)
# print(y_probas)
# skplt.metrics.plot_roc(yTest, y_probas)
# plt.show()

### MSE ###
data = load_wine()
X_train, X_test, y_train, y_test = train_test_split(
    data.data, data.target, test_size=0.33, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
score = model.score(X_test, y_test)
print("Score :", score)
coefficient = model.coef_
intercept = model.intercept_
print("Coefficient :\n", coefficient)
print()
print("Intercept :\n", intercept)
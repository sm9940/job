from sklearn.datasets import load_breast_cancer # pip install scikit-learn
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

data = load_breast_cancer()
print(data)
xTrain, xTest, yTrain, yTest = train_test_split(data.data, data.target, random_state=42)
model = DecisionTreeClassifier(criterion="entropy")
print("model :", model)
model.fit(xTrain, yTrain)

yPredict = model.predict(xTest)
print("학습 후 예측 결과 :", yPredict)
for pY, pT in zip(yPredict, yTest) :
    print("[",pY," :", pT,"]")

from sklearn.preprocessing import StandardScaler

print(xTrain)
scaler = StandardScaler()
scaler.fit(xTrain)
xTrainTrans = scaler.transform(xTrain)
print(xTrainTrans)
model.fit(xTrainTrans, yTrain)
print("------------------ transformation ----------------------")
yPredict = model.predict(xTest)
for pY, pT in zip(yPredict, yTest) :
    print("[",pY," :", pT,"]")

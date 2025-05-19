from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

data = load_breast_cancer()
X_train,X_test,y_train,y_test = train_test_split(data.data,data.target,random_state=42)

model = DecisionTreeClassifier(criterion='entropy')
print("model: ",model)
model.fit(X_train,y_train)
y_pred = model.predict(X_test)
print("학습 후 예측 결과 :",y_pred)
for pY,pT in zip(y_pred,y_test) :
    print("[",pY,pT,"]")
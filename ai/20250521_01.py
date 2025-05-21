# 라이브러리 불러오기
from sklearn.datasets import load_iris  # iris 데이터셋 로드
import pandas as pd                     # 데이터프레임 처리
import seaborn as sns                   # 시각화(상관관계, pairplot 등)
import numpy as np                      # 수치 연산
import matplotlib.pyplot as plt         # 시각화

# 1. 데이터 로드 및 확인
data = load_iris()
print(data.keys())       # 데이터셋의 키 확인 (data, target, feature_names, DESCR 등)
print(data.DESCR)        # 데이터셋 설명 출력

# 2. 피처(특징)와 타깃 데이터프레임 생성
features = pd.DataFrame(data=data.data,
                        columns=data.feature_names)
print(features)          # 피처 데이터 일부 출력

target = pd.DataFrame(data.target, columns=["species"])  # 타깃(종) 생성
iris = pd.concat([features, target], axis=1)               # 피처 + 타깃 결합

# 3. 컬럼명 변경 (한글 코드 가독성 향상)
iris.rename({'sepal length (cm)' : 'sepal_length',
             'sepal width (cm)'  : 'sepal_width',
             'petal length (cm)' : 'petal_length',
             'petal width (cm)'  : 'petal_width'},
            axis=1, inplace=True)

print(iris.head())       # 데이터프레임 앞부분 출력
print(iris.isna().sum(axis=0))  # 결측치 확인
print(iris.info())       # 데이터 정보(타입, 개수)
print(iris.describe())   # 기초 통계량 확인
print(iris.groupby('species').size())  # 클래스별 샘플 개수


# 8. 학습용/테스트용 데이터 분리
from sklearn.model_selection import train_test_split
xTrain, xTest, yTrain, yTest = train_test_split(
    iris.iloc[:, :-1], iris.iloc[:, -1],
    test_size=0.33, random_state=42, shuffle=True)
print(yTest.describe())  # 테스트용 타깃 분포 정보

# 9. 결정트리 모델 생성 및 학습
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier(
    criterion='gini', splitter='best', max_depth=None,
    min_samples_split=2, min_samples_leaf=1,
    min_weight_fraction_leaf=0.0, max_features=None,
    min_impurity_decrease=0.0)
print(model)
model.fit(xTrain, yTrain)        # 모델 학습
print(model.score(xTest, yTest)) # 테스트 정확도 출력



# 15. 정확도 및 혼동 행렬
from sklearn.metrics import  confusion_matrix,precision_score,recall_score
pred = model.predict(xTest)
confMatrix = confusion_matrix(yTest, pred)  # 혼동 행렬 생성
print('Confusion Matrix:\n', confMatrix)


precisions= precision_score(yTest,model.predict(xTest),average=None)
recalls= recall_score(yTest,model.predict(xTest),average=None)

for target,score in zip(data.target_names,precisions):
    print(f"{target}의 정밀도: {score}")

for target,score in zip(data.target_names,recalls):
    print(f"{target}의 재현율: {score}")

    from sklearn.metrics import fbeta_score, f1_score

# 다중 분류일 경우 average != "binary"
# beta=1인 F-beta 점수 계산 (beta=1은 F1-score와 동일)
fbetas = fbeta_score(
    yTest,
    model.predict(xTest),
    beta=1,
    average=None
)

for target, score in zip(data.target_names, fbetas):
    print(f"{target}의 f점수(beta=1): {score}")

print("===========================")

# 다중 분류일 경우 average != "binary"
# F1-score 계산
f1s = f1_score(
    yTest,
    model.predict(xTest),
    average=None
)

for target, score in zip(data.target_names, f1s):
    print(f"{target}의 f1점수: {score}")

from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = load_wine()

xTrain, xTest, yTrain, yTest = train_test_split(
    data.data,data.target,random_state=42)

model = LinearRegression()
model.fit(xTrain, yTrain)        # 모델 학습
score=model.score(xTest,yTest)
print('정확도: ',score) # 테스트 정확도 출력

coefficient = model.coef_
intercept = model.intercept_

print("계수 : \n",coefficient)
print()
print("절편 : \n",intercept)
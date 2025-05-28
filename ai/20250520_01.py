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

# 4. 박스플롯 함수 정의 (특징별 값 분포 박스플롯)
def boxplt_iris(feature_names, dataset):
    plt.figure(figsize=(11,9))
    for i, col in enumerate(feature_names, 1):
        plt.subplot(2,2,i)
        plt.tick_params(axis='both', left=True, top=False,
                        right=False, bottom=True,
                        labelleft=False, labeltop=False,
                        labelright=False, labelbottom=False)
        dataset[col].plot(kind='box')  # 박스플롯 그리기
        plt.title(col)
    # plt.show() 생략: 호출 시 화면에 출력

boxplt_iris(iris.columns[:-1], iris)  # 네 개 피처에 대해 박스플롯 표시

# 5. 히스토그램 함수 정의 (특징별 히스토그램)
def histogram_iris(feature_names, dataset):
    plt.figure(figsize=(11,9))
    for i, col in enumerate(feature_names, 1):
        plt.subplot(2,2,i)
        plt.tick_params(axis='both', left=True, top=False,
                        right=False, bottom=True,
                        labelleft=False, labeltop=False,
                        labelright=False, labelbottom=False)
        dataset[col].hist()  # 히스토그램 그리기
        plt.title(col)

histogram_iris(iris.columns[:-1], iris)  # 히스토그램 표시

# 6. 상관관계 히트맵
corr = iris.corr()  # 상관계수 계산
cmap = sns.diverging_palette(220,10, as_cmap=True)
plt.figure(figsize=(11,9))
sns.heatmap(corr, cmap=cmap, vmax=1.0, vmin=-1.0,
            center=0, square=True, linewidths=.5,
            cbar_kws={'shrink':.5})  # 히트맵 그리기

# 7. Pairplot (클래스별 분포 및 관계)
sns.pairplot(iris, hue='species')  # species에 따라 색상 구분
# plt.show() 생략

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

# 10. 교차 검증 (K-Fold)
from sklearn.model_selection import cross_val_score, KFold
cv = KFold(n_splits=10, shuffle=True, random_state=42)
results = cross_val_score(model, xTrain, yTrain, cv=cv)
print(results)                   # 각 폴드 정확도
print(np.mean(results))          # 평균 정확도

# 11. 교차 검증 (StratifiedKFold)
from sklearn.model_selection import StratifiedKFold
cv1 = StratifiedKFold(n_splits=10, shuffle=True, random_state=42)
results = cross_val_score(model, xTrain, yTrain, cv=cv1)
print(results)
print(np.mean(results))

# 12. 학습 곡선 시각화
import scikitplot as skplt
skplt.estimators.plot_learning_curve(model, xTrain, yTrain, figsize=(6,6))
# plt.show()

# 13. 하이퍼파라미터 튜닝 (GridSearchCV)
from sklearn.model_selection import GridSearchCV
estimator = DecisionTreeClassifier()
parameters = {
    'criterion': ['gini','entropy'],
    'splitter': ['best','random'],
    'max_depth': [4,6,8,10,12],
    'min_weight_fraction_leaf': [0.0,0.1,0.2,0.3],
    'random_state': [7,23,42,78,142],
    'min_impurity_decrease': [0.0,0.05,0.1,0.2]
}
model = GridSearchCV(
    estimator=estimator, param_grid=parameters,
    cv=cv1, verbose=1, n_jobs=-1, refit=True)
model.fit(xTrain, yTrain)
print('Best Estimator:', model.best_estimator_)
print('Best Params:', model.best_params_)
print('Best Score:', model.best_score_)

# 14. 최적 모델 평가
model.fit(xTrain, yTrain)
print('GSCV model score =', model.score(xTest, yTest))

# 15. 정확도 및 혼동 행렬
from sklearn.metrics import accuracy_score, confusion_matrix
pred = model.predict(xTest)
acc = accuracy_score(yTest, pred)        # 정확도 계산
confMatrix = confusion_matrix(yTest, pred)  # 혼동 행렬 생성
print('Accuracy:', acc)
print('Confusion Matrix:\n', confMatrix)

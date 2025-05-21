from sklearn.datasets import load_iris
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix  # 혼동 행렬 함수 import

# 1. 데이터 로드 및 전처리
data = load_iris()
iris = pd.DataFrame(data.data, columns=data.feature_names)
iris['species'] = data.target
iris.columns = ['sepal_length','sepal_width','petal_length','petal_width','species']

# 2. 학습/테스트 분리
x = iris.drop(columns=['species'])
y = iris['species']
X_train, X_test, y_train, y_test = train_test_split(
    x, y, test_size=50, train_size=100, random_state=42, shuffle=True
)

# 3. 모델 학습
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# 4. 테스트 정확도 출력
print("전체 테스트 정확도:", model.score(X_test, y_test))

# 5. 여러 새로운 샘플 예측
new_samples = [
    [5.0, 3.7, 7.3, 2.1],  # likely virginica
    [5.1, 3.5, 1.4, 0.2],  # likely setosa
    [7.7, 3.8, 6.7, 2.2],  # virginica
    [4.9, 3.1, 1.5, 0.1]   # setosa
]
df_samples = pd.DataFrame(new_samples, columns=x.columns)
pred = model.predict(df_samples)
for i in pred:
    print("모델 예측 종(species):", data.target_names[i])

# 6. 테스트 세트에 대한 예측과 혼동 행렬 확인
y_pred_test = model.predict(X_test)                     # 테스트 세트에 대한 예측값 생성
cm = confusion_matrix(y_test, y_pred_test)               # 실제값(y_test) vs. 예측값(y_pred_test) 비교
print("\nConfusion Matrix:")                             
print(cm)                                                # 행: 실제 클래스, 열: 예측 클래스 순서

# 7. 시각화를 위해 species 이름 매핑
iris['species_name'] = iris['species'].map(lambda i: data.target_names[i])

# 8. Pairplot 시각화
sns.pairplot(iris, hue='species_name', corner=True)
plt.show()

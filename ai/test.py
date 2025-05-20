from sklearn.datasets import load_iris
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# 1-1. 데이터 준비
data = load_iris()
iris = pd.DataFrame(data.data, columns=data.feature_names)
iris['species'] = data.target

# 1-2. 컬럼명 정리 (선택)
iris.columns = ['sepal_length','sepal_width','petal_length','petal_width','species']

# 1-3. X, y 분리
X = iris.drop(columns=['species'])
y = iris['species']

# 1-4. 100개 학습, 50개 테스트
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=50, train_size=100, random_state=42, shuffle=True
)

# 1-5. 모델 학습
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# 1-6. 기본 테스트 정확도 확인
print("전체 테스트 정확도:", model.score(X_test, y_test))

# 2-1. 주어진 새 샘플
new_sample = [[5.0, 3.7, 7.3, 2.1]]

# 2-2. 예측
pred = model.predict(new_sample)[0]
print("모델 예측 종(species):", data.target_names[pred])

import seaborn as sns
import matplotlib.pyplot as plt

# species를 이름으로 매핑(optional)
iris['species_name'] = iris['species'].map(lambda i: data.target_names[i])

sns.pairplot(iris, hue='species_name', corner=True)
plt.show()

import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import matplotlib.pyplot as plt

# 학습용 데이터
x_train = np.array([0, 1, 4, 5, 7])
y_train = np.array([1, 3, 9, 11, 15])  # y = 2x + 1

# 테스트 데이터
x_test = np.array([2, 6])
y_test = np.array([5, 13])

# 모델 정의
model = Sequential()
model.add(Dense(1, input_shape=(1,)))
model.compile(optimizer='SGD', loss='mse')
model.summary()

# 학습 전 예측
y_predict = model.predict(x_test)
print("학습 전 예측값 ::", y_predict.flatten())
print("정답             ::", y_test)

# 학습
history = model.fit(x_train, y_train, epochs=1000, verbose=0)

# 학습 후 예측
y_predict = model.predict(x_test)
print("학습 후 예측값   ::", y_predict.flatten())

# 손실 그래프 출력
plt.plot(history.history['loss'])
plt.title('Training Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.grid()
plt.show()

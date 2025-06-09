import numpy as np
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense

#학습용 데이터(문제지/정답지)를 준비
x_train = np.array( [0,1,4,5,7] )
y_train = np.array( [1,3,9,11,15] ) # 0 -> 1, 1 -> 3,  y = ax + b, y = ax + 1, y = 2x + 1
print(x_train);     print(y_train)
#모의고사시험지/정답지
x_test = np.array([2,6])
y_test = np.array([5,13])
print(x_test);      print(y_test)
#모델 준비(학습 주체:학생)
model = Sequential()
model.add(Dense(1, input_shape=(1,)))
model.compile('SGD', 'mse')
model.summary()
#학습 전 모의고사 실시(사전 평가)
y_predict = model.predict(x_test)
print("사전 예측값 :: ", y_predict.flatten())
print("정답   :: ", y_test)
#수업준비(수업방식 지정)
#수업실시(반복학습 1000번)
history = model.fit( x_train, y_train, epochs = 100, verbose = 0 )
# 모의고사 실시(학습 후)
y_predict = model.predict(x_test)
print("학습 후 예측값 :: ", y_predict.flatten())
import matplotlib.pyplot as plt
# 그래프그리기(각 단계별 오차 그래프)
plt.plot(history.history['loss']);  plt.title('Loss')
plt.title('Loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train'], loc=0)
plt.show()
import tensorflow.keras as kr
import numpy as np
import matplotlib.pyplot as plt

x_train = np.array([0,1])
y_train = np.array([1,3])
print(x_train)
print(y_train)

x_test = np.array([2,3])
y_test = np.array([5,7])

print(x_test)
print(y_test)

model= kr.layers.Sequential()
model.add(kr.layers.Dense(1,input_shape=(1,)))
print(type(model))
model.summary()
y_predict =model.predict(x_test)
print("예측값 :",y_predict.flatten())
print("정답 : ",y_test)

model.compile("SGD",'mse')
history=model.fit(x_train,y_train,epochs = 1000,verbose = 1)
y_predict = model.predict(x_test)
print(y_predict.flatten())

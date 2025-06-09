# runnig : conda activate tensorflow
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras import optimizers
import numpy as np
import matplotlib.pyplot as plt

x = np.array([1,2,3,4,5])
y = np.array([1,2,3,4,5])

model = Sequential()
model.add(Dense(1, input_dim=1, activation="linear"))
sgd = optimizers.SGD(lr=0.01)
model.compile(optimizer=sgd, loss="mse", metrics=['accuracy'])
model.fit(x,y,batch_size=1, epochs=10, shuffle=False)

plt.plot(x,y,"bo")
plt.plot(x, model.predict(x), "r-")
plt.show()
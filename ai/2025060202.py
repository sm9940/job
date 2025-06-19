<<<<<<< HEAD
# runnig : conda activate tensorflow
from keras.models import Sequential
from keras.layers import Dense
from keras import optimizers
import numpy as np
import matplotlib.pyplot as plt

x = np.array([1,2,3,4,5,6,7,8])
y = np.array([0,0,0,0,1,1,1,1])

model = Sequential() # 선형 알고리즘
model.add(Dense(1, input_dim=1, activation="sigmoid")) # 히든 레이어 알고리즘 : activation = sigmoid - bi-classificatioin목적
rms = optimizers.RMSprop(lr=0.01) 
model.compile(optimizer=rms, loss="binary_crossentropy", metrics=['accuracy']) # LF : MSE 오류평균제곱방식
model.fit(x,y,batch_size=1, epochs=200, shuffle=False)

plt.plot(x,y,"rx")
print(model.predict(x))
=======
# runnig : conda activate tensorflow
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras import optimizers
import numpy as np
import matplotlib.pyplot as plt

x = np.array([1,2,3,4,5,6,7,8])
y = np.array([0,0,0,0,1,1,1,1])

model = Sequential() # 선형 알고리즘
model.add(Dense(1, input_dim=1, activation="sigmoid")) # 히든 레이어 알고리즘 : activation = sigmoid - bi-classificatioin목적
rms = optimizers.RMSprop(lr=0.01) 
model.compile(optimizer=rms, loss="binary_crossentropy", metrics=['accuracy']) # LF : MSE 오류평균제곱방식
model.fit(x,y,batch_size=1, epochs=200, shuffle=False)

plt.plot(x,y,"rx")
print(model.predict(x))
>>>>>>> origin
plt.show()
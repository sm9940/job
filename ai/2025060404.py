# runnig : conda activate tensorflow
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dropout
from keras import optimizers
import numpy as np
import matplotlib.pyplot as plt

#5 모델 생성, mnistKeras.weight을 읽어 세팅, 모델을 컴파일
network = Sequential()
network.add(Flatten(input_shape=(28,28)))
network.add(Dropout(rate=0.2))
network.add(Dense(512, activation='relu'))
network.add(Dropout(rate=0.2))
network.add(Dense(10, activation='softmax'))

import h5py
network.load_weights('mnistKeras.weights.h5')
network.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])
print("model : ", network.summary())

# 03과 04번으로 여기에 
# mnist data 중 0 ~ 9 이미지 10개를 predict()해서 실제 label과 맞는 비교하는 코드를 수행
data_train, data_test = tf.keras.datasets.mnist.load_data()
images_test, labels_test = data_test

for i in range(10) :
    img = images_test[labels_test==i][0].reshape(28,28)
    img = img.reshape((1, 28, 28))
    predicted_result = network.predict(img)
    predicted_labels = np.argmax(predicted_result, axis=1)
    print("image's number is", predicted_labels)
    print("right answer is", labels_test[i])
print("end...!")
# runnig : conda activate tensorflow
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Flatten
from tensorflow.keras import optimizers
import numpy as np
import matplotlib.pyplot as plt

#keras MNIST data loading...
data_train, data_test = tf.keras.datasets.mnist.load_data()
images_train, labels_train = data_train
images_test, labels_test = data_test

# gray image shape(28, 28) -> flatten (28*28)
# images_train = images_train.reshape((60000, 28*28))
# images_train = images_train.astype('float32') /255
# images_test = images_test.reshape((10000, 28*28))
# images_test = images_test.astype('float32') /255

from tensorflow.keras.utils import to_categorical
labels_train = to_categorical(labels_train)
labels_test = to_categorical(labels_test)

#훈련 데이터 x:이미지, y:라벨
print('훈련데이터 라벨 [{}]: \n'.format(labels_train.shape))
print('훈련데이터 이미지[{}] : \n'.format(images_train.shape))
print('테스트데이터 라벨 [{}]: \n'.format(labels_train.shape))
print('테스트데이터 이미지[{}] : \n'.format(images_test.shape))

#5  모델 생성, 레이어 2개, 이미지 사이즈 28*28
network = Sequential()
network.add(Flatten(input_shape=(28,28)))# gray image shape(28, 28) -> flatten (28*28)
# network.add(Dense(700, activation='sigmoid'))
#network.add(Dense(512, activation='relu',input_shape=(28*28))) # flatten (28*28)
network.add(Dense(512, activation='relu'))
network.add(Dense(10, activation='softmax'))
network.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])
print("model : ", network.summary())

network.fit(images_train, labels_train, epochs=500, batch_size=256)
loss_test, acc_test = network.evaluate(images_test, labels_test)
print("acc_test", acc_test)

import h5py
print(h5py.__version__)
network.save_weights('mnistKeras.weight')
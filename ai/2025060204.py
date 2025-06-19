# runnig : conda activate tensorflow
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Flatten
from keras import optimizers
import numpy as np
import matplotlib.pyplot as plt

#5 모델 생성, mnistKeras.weight을 읽어 세팅, 모델을 컴파일
network = Sequential()
network.add(Flatten(input_shape=(28,28)))
network.add(Dense(700, activation='sigmoid'))
network.add(Dense(10, activation='softmax'))

import h5py
network.load_weights('mnistKeras.weight')
network.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])

import cv2
# 이미지 읽기
# 분류하고자 하는 이미지를 읽어옴
images_mission = plt.imread("1.jpg") # 28 * 28 
images_mission = cv2.cvtColor(images_mission, cv2.COLOR_BGR2GRAY)
images_mission = cv2.resize(images_mission, (28,28))
images_mission = images_mission.reshape((1, 28, 28))
images_mission = images_mission.astype('float32') /255

predicted_result = network.predict(images_mission)
predicted_labels = np.argmax(predicted_result, axis=1)
print("image's number is", predicted_labels)

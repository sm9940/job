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
#훈련 데이터 x:이미지, y:라벨
print('훈련데이터 라벨 [{}]: \n'.format(labels_train.shape))
print('훈련데이터 이미지[{}] : \n'.format(images_train.shape))

#plot 이미지
fig, ax = plt.subplots(nrows=2, ncols=5, sharex=True, sharey=True)
ax = ax.ravel()
for i in range(10) :
    img = images_train[labels_train==i][0].reshape(28,28)
    ax[i].imshow(img, cmap='Greys', interpolation='nearest')
ax[0].set_xticks([])
ax[0].set_yticks([])
plt.tight_layout()
plt.show()
#이미지 중 6이란 숫자의 데이터를 25개 꺼내 화면에 그림
fig, ax = plt.subplots(nrows=5, ncols=5, sharex=True, sharey=True)
ax = ax.ravel()
for i in range(25) :
    img = images_train[labels_train==6][i].reshape(28,28)
    ax[i].imshow(img, cmap='Greys', interpolation='nearest')
ax[0].set_xticks([])
ax[0].set_yticks([])
plt.tight_layout()
plt.show()
#훈련데이터 중 하나를 꺼내 그결과 라벨을 출력
digit = images_train[0]
plt.imshow(digit, cmap=plt.cm.binary)
#plt.show()
print("첫번째 이미지의 모양 = ", labels_train[0])

#5  모델 생성, 레이어 2개, 이미지 사이즈 28*28
network = Sequential()
network.add(Flatten(input_shape=(28,28)))
network.add(Dense(700, activation='sigmoid'))
network.add(Dense(10, activation='softmax'))
network.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])
print(network)

from tensorflow.keras.utils import to_categorical
labels_train = to_categorical(labels_train)
labels_test = to_categorical(labels_test)

network.fit(images_train, labels_train, epochs=500, batch_size=256)
loss_test, acc_test = network.evaluate(images_test, labels_test)
print("acc_test", acc_test)

import cv2
# 새로운 이미지 읽기
# 분류하고자 하는 이미지를 읽어옴
images_mission = plt.imread("4.jpg") # 28 * 28 
images_mission = cv2.cvtColor(images_mission, cv2.COLOR_BGR2GRAY)
images_mission = cv2.resize(images_mission, (28,28))
images_mission = images_mission.reshape((1, 28,28))
images_mission = images_mission.astype('float32') /255

# print(images_mission)
predicted_result = network.predict(images_mission)
predicted_labels = np.argmax(predicted_result, axis=1)
print("image's number is", predicted_labels)

import h5py
print(h5py.__version__)
network.save_weights('mnistKeras.weight')
# [과제] network 모델의 구성을 보지 말고 load_weight만으로 weight를 newModel에 맞춰 보세요.
newModel = Sequential([
   Dense(512, activation='relu', input_shape=(28*28,)),
   Dense(10, activation='softmax')
])
newModel.load_weights('mnistKeras.weight')
newModel.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    
# print(images_mission)
predicted_result = newModel.predict(images_mission)
predicted_labels = np.argmax(predicted_result, axis=1)
print("image's number is", predicted_labels)

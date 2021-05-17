import keras
import tensorflow
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D

(a_train, b_train), (a_test, b_test) = mnist.load_data()

a_train = a_train.reshape(a_train.shape[0], 28, 28, 1)
a_test = a_test.reshape(a_test.shape[0], 28, 28, 1)
input_shape = (28,28,1)

a_train = a_train.astype('float32')
a_test = a_test.astype('float32')
a_train /= 255
a_test /= 255

b_train = keras.utils.to_categorical(b_train, 10)
b_test = keras.utils.to_categorical(b_test, 10)

model = Sequential()
model.add(Conv2D(32, kernel_size=(3,3), activation='relu', input_shape=input_shape))
model.add(Conv2D(64, kernel_size=(3,3), activation ='relu'))
model.add(Conv2D(128, kernel_size=(3,3), activation ='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(10, activation='softmax'))

model.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy'])

model.fit(a_train, b_train,batch_size=128,epochs=5,verbose=1)

results = model.evaluate(a_test, b_test, verbose = 0)
print(results)

model.save('test.model')

for x in range(1, 11):
    img = cv.imread(fr'C:\Users\Eric\PycharmProjects\pythonProject2\test.model\{x}.png', cv.IMREAD_GRAYSCALE)
    img = img.astype('float32')
    img = img.reshape(1, 28, 28, 1)
    img /= 255
    prediction = model.predict(img).argmax()
    print(prediction)
    plt.imshow(img[0], cmap=plt.cm.binary)
    plt.show()

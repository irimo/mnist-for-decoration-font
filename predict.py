import keras
import numpy as np
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, InputLayer
from keras.optimizers import RMSprop
import os

model = Sequential()

def before_do():

    (x_train, y_train), (x_test, y_test) = mnist.load_data()

    # MNISTデータを加工する
    x_train  = x_train.reshape(60000, 784)
    x_test   = x_test.reshape(10000, 784)
    x_train  = x_train.astype('float32')
    x_test   = x_test.astype('float32')
    x_train /= 255
    x_test  /= 255
    y_train  = keras.utils.to_categorical(y_train, 10)
    y_test   = keras.utils.to_categorical(y_test, 10)

    # モデルの構築
    model.add(InputLayer(input_shape=(784,)))
    model.add(Dense(10, activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

    # 学習
    epochs = 20
    batch_size = 128
    history = model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, verbose=1, validation_data=(x_test, y_test))

def predict(npy_path, predict_num):

    img =  np.load(npy_path, allow_pickle=True)

    print(img.shape)

    print(type(img))

    img = (np.expand_dims(img,0))

    print(img.shape)

    predictions_single = model.predict(img)

    print(predictions_single)
    print("This number is expect: "+str(predict_num)+" and probably: ")

    predict = np.argmax(predictions_single[0])

    print(predict)

before_do()

for i in range(0,10):
    predict('./output/mini_'+str(i)+'.npy', i)
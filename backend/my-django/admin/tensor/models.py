import tensorflow as tf
import numpy as np


class Perceptron(object):

    def __init__(self):
        pass











class Calculator(object):

    def __init__(self):
        print(f'Tensorflow Version: {tf.__version__}')

    def process(self):
        self.pius(1,6)
        print('*'*100)
        self.mean()

    def pius(self, a, b):
        print(tf.constant(a) + tf.constant(b))

    def mean(self):
        x_array = np.arange(18).reshape(3,2,3)
        # reshape((3 행, 2열 , 3)
        x2 = tf.reshape(x_array, shape=(-1,6)) # shape 으로 다시 변환 -1은 그대로 란 뜻
        # 각 열의 합을 계산
        xsum = tf.reduce_sum(x2, axis=0)
        # 각 열의 평균을 계산
        xmean = tf.reduce_mean(x2, axis=0)

        print(f'입력 크기: {x_array.shape}\n')
        print(f'크기가 변경된 입력 크기: {x2.numpy()}\n')
        print(f'열의 합: {xsum.numpy()}\n')
        print(f'열의 평균: {xmean.numpy()}\n')





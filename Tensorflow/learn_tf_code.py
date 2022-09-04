#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 22:16:28 2022

@author: goncalo

Following the tutorial:
https://www.tensorflow.org/tutorials/quickstart/beginner
"""

import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

physical_devices = tf.config.list_physical_devices()
print("Number of Devices: " + str(len(physical_devices)))

logical_devices = tf.config.list_logical_devices()
print("Number of Devices: " + str(len(logical_devices)))

print ("Tensorflow version: ", tf.__version__)

mnist = tf.keras.datasets.mnist

(x_train,y_train) , (x_test,y_test) = mnist.load_data()

x_train, x_test = x_train / 255.0 , x_test / 255.0

model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape = (28,28)),
    tf.keras.layers.Dense(128, activation = 'relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10)
    ])

predictions = model(x_train[:1]).numpy()
predictions

tf.nn.softmax(predictions).numpy()

loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

-tf.math.log(1/10)

loss_fn(y_train[:1], predictions).numpy()

model.compile(optimizer = 'adam', loss = loss_fn, metrics = ['accuracy'])


# train model
model.fit(x_train, y_train, epochs = 5)

model.evaluate(x_test, y_test, verbose = 2)

probability_model = tf.keras.Sequential([model, tf.keras.layers.Softmax()])
probability_model(x_test[:5])

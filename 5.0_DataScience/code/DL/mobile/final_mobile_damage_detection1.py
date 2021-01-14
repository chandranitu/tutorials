import urllib
import json
import os
import h5py
import numpy as np
import pandas as pd
from IPython.display import Image, display, clear_output
from collections import Counter
from sklearn.metrics import classification_report, confusion_matrix
from keras.optimizers import SGD, RMSprop
from keras.constraints import maxnorm
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.applications.vgg16 import VGG16
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
from keras.regularizers import l2, l1
from keras.models import Sequential, load_model
from keras.layers import Conv2D, MaxPooling2D, ZeroPadding2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.utils.np_utils import to_categorical
from keras import optimizers 
from keras.callbacks import ModelCheckpoint, History

#create H5 files of images

# path to the model weights file

#Linux
#location = '/home/hadoop/hadoop/hadoop_working/DataScience/5.MachineLearning/8.DeepLearning/code/mobile'
#top_model_weights_path = location+'/top_model_weights.h5' # will be saved into when we create our model
# model_path = location + '/initial_data2_model.h5'
#fine_tuned_model_path = location+'/scratch-vs-nonscratch.h5'

#Windows
location = 'D:\project\datascience\mobile'
top_model_weights_path = location+'\top_model_weights.h5' # will be saved into when we create our model
fine_tuned_model_path = location+'\scratch-vs-nonscratch.h5'

# dimensions of our images
img_width, img_height = 100, 100

#train_data_dir = location+'/train'
#validation_data_dir = location+'/test'
train_data_dir = location+'\\train'
validation_data_dir = location+'\\validate'

train_samples = [len(os.listdir(train_data_dir+'/'+i)) for i in sorted(os.listdir(train_data_dir))]
nb_train_samples = sum(train_samples)
validation_samples = [len(os.listdir(validation_data_dir+'/'+i)) for i in sorted(os.listdir(validation_data_dir))]
nb_validation_samples = sum(validation_samples)

nb_validation_samples
fine_tuned_model_path

from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras import backend as K
#**import tkinter as tk
#from tkinter import filedialog
import os.path

#fix random seed for reproducibility
seed = 1000
np.random.seed(seed)

img_width, img_height = 100, 100

epochs = 35
batch_size = 8
lrate = 0.0001
decay = 1e-6

#uses of optimizers(keras)parameter in the SGD for decay and this reduces the learning rate over time.
sgd = SGD(lr=lrate, momentum=0.9, decay=decay, nesterov=False)

#RMSprop. leave the parameters of this optimizer at their default values (except the learning rate, which can be freely tuned).
# This optimizer is usually a good choice for recurrent neural networks. epsilon: float >= 0.
rmsprop = RMSprop(lr=0.0001, rho=0.9, epsilon=1e-8, decay=0.0)

model = Sequential()
model.add(Conv2D(32, (3, 3), input_shape=(100,100,3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Conv2D(64, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Conv2D(128, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(256))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(1))
model.add(Activation('sigmoid'))

model.compile(loss='binary_crossentropy',
              optimizer='sgd',
              metrics=['accuracy'])

#this is the augmentation configuration we will use for training
train_datagen = ImageDataGenerator(
    rescale=1. / 255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True)

#this is the augmentation configuration we will use for testing:
#only rescaling
test_datagen = ImageDataGenerator(rescale=1. / 255)

train_generator = train_datagen.flow_from_directory(
    train_data_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='binary')

validation_generator = test_datagen.flow_from_directory(
    validation_data_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='binary')

checkpoint = ModelCheckpoint(fine_tuned_model_path, monitor='val_acc', 
                                 verbose=1, save_best_only=True, 
                                 save_weights_only=False, mode='auto')
model.fit_generator(
    train_generator,
    steps_per_epoch=nb_train_samples // batch_size,
    epochs=epochs,
    validation_data=validation_generator,
    validation_steps=nb_validation_samples // batch_size,
    verbose=1,
    callbacks=[checkpoint])

#plotting graph of loss function
#dict_keys(['val_acc', 'val_loss', 'loss', 'acc'])
history = model.fit(X, Y, validation_split=0.33, epochs=epochs, batch_size=10, verbose=0)
# list all data in history
print(history.history.keys())
# summarize history for accuracy
plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
# summarize history for loss
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

#with open(location+'\\ft_history.txt', 'wb') as f:
#        json.dump(fit.history, f)

def prepare_img_256(img_path):
 img = load_img(img_path, target_size=(100, 100))
 x = img_to_array(img)
 x = x.reshape((1,) + x.shape)/255
 return x

def get_damage_non_damage(img_256, model):
    print ("Determining scratch...")
    pred = model.predict(img_256)
    if pred[0][0] <=.5:
        return 'No'
    else:
        return 'Yes'

#damage_detection = load_model('scratch-vs-nonscratch.h5')
damage_detection = load_model(fine_tuned_model_path)

#data_path = r'/home/hadoop/hadoop/hadoop_working/DataScience/5.MachineLearning/8.DeepLearning/code/mobile/test'

data_path = r'D:\project\datascience\mobile\test'

for path, subdirs, files in os.walk(data_path):
    for name in files:
        image_path = os.path.join(path, name)
        print(image_path)
        img_256 = prepare_img_256(image_path)
        dnd = get_damage_non_damage(img_256, damage_detection)
        print(dnd)

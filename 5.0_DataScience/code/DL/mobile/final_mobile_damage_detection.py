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

location = '/home/hadoop/hadoop/hadoop_working/DataScience/6.DeepLearning/code/mobile'
top_model_weights_path = location+'/top_model_weights.h5' # will be saved into when we create our model

fine_tuned_model_path = location+'/scratch-vs-nonscratch.h5'

# dimensions of our images
img_width, img_height = 100, 100

#train_data_dir = location+'/train'
train_data_dir = location+'/train'
validation_data_dir = location+'/validate'

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
import os.path

#fix random seed for reproducibility
seed = 2017
np.random.seed(seed)

img_width, img_height = 100, 100

epochs = 20
batch_size = 8
lrate = 0.0001
decay = 1e-6
sgd = SGD(lr=lrate, momentum=0.9, decay=decay, nesterov=False)
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

#Actual testing
damage_detection = load_model('/home/hadoop/hadoop/hadoop_working/DataScience/6.DeepLearning/code/mobile/scratch-vs-nonscratch.h5')
data_path = r'/home/hadoop/hadoop/hadoop_working/DataScience/6.DeepLearning/code/mobile/test'

for path, subdirs, files in os.walk(data_path):
    for name in files:
        image_path = os.path.join(path, name)
        print(image_path)
        img_256 = prepare_img_256(image_path)
        dnd = get_damage_non_damage(img_256, damage_detection)
        print(dnd)

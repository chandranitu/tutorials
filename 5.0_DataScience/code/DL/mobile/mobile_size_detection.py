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
# model_path = location + '/initial_data2_model.h5'
fine_tuned_model_path = location+'/scratch-vs-nonscratch.h5'

# dimensions of our images
img_width, img_height = 100, 100

train_data_dir = location+'/train'
validation_data_dir = location+'/test'

train_samples = [len(os.listdir(train_data_dir+'/'+i)) for i in sorted(os.listdir(train_data_dir))]
nb_train_samples = sum(train_samples)
validation_samples = [len(os.listdir(validation_data_dir+'/'+i)) for i in sorted(os.listdir(validation_data_dir))]
nb_validation_samples = sum(validation_samples)

nb_validation_samples
fine_tuned_model_path

import matplotlib.pyplot as plt

# Determine the (random) indexes of the images want to see 
mobile_signs = [300, 2250, 3650, 4000]

# Fill out the subplots with the random images that you defined 
for i in range(len(mobile_signs)):
    plt.subplot(1, 4, i+1)
    plt.axis('off')
    plt.imshow(validation_samples[mobile_signs[i]])
    plt.subplots_adjust(wspace=0.5)
    plt.show()

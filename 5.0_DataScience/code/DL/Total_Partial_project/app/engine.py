
# coding: utf-8

# In[29]:

import os
import json
import urllib

import h5py
import numpy as np
import pickle as pk

from keras.applications.imagenet_utils import preprocess_input, decode_predictions
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
from keras.models import Sequential, load_model
from keras.utils.data_utils import get_file


# In[30]:

def prepare_img_256(img_path):
	img = load_img(img_path, target_size=(100, 100))
	x = img_to_array(img)
	x = x.reshape((1,) + x.shape)/255
	return x


# In[31]:

def car_damage_gate(img_256, model):
	print ("Validating that damage exists...")
	pred = model.predict(img_256)
	if pred[0][0] <=.5:
		return True
	else:
		return False


# In[32]:

def location_assessment(img_256, model):
	print ("Determining location of damage...")
	pred = model.predict(img_256)
	#print(pred)
	if pred[0][0] <=.5:
		return 'Front'
	else:
		return 'Rear'


# In[33]:

#d = {0: 'Front', 1: 'Rear'}


# In[34]:

def front_injury_assessment(img_256, model):
    print ("Determining severity of damage...")
    pred = model.predict(img_256)
    if pred[0][0] <=.5:
        return 'Collar bone fracture' # print "Validation complete - proceed to location and severity determination"
    else:
        return 'Concussion and Face laceration'


# In[35]:

def rear_injury_assessment(img_256, model):
    print ("Determining severity of damage...")
    pred = model.predict(img_256)
    if pred[0][0] <=.5:
        return 'Rib Fracture' # print "Validation complete - proceed to location and severity determination"
    else:
        return 'Neck Strain'


# In[36]:

injury_front_model = load_model('ft_model_damage_front_injury.h5')
injury_rear_model = load_model('ft_model_injury_rear.h5')
location_model = load_model('ft_model_damage1_location.h5')


# In[37]:

# load models
def engine(img_path,location_model):
	img_256 = prepare_img_256(img_path,location_model)
	#injury_front_model = load_model('ft_model_damage_front_injury.h5')
	#injury_rear_model = load_model('ft_model_injury_rear.h5')
	#location_model = load_model('ft_model_damage1_location.h5')
	#print('location printing')
	#print(location_model)
	x = location_assessment(img_256, location_model)
	print(x)
	if x == 'Front':
		y = front_injury_assessment(img_256, injury_front_model)
	else:
		y = rear_injury_assessment(img_256, injury_rear_model)
	#print()
	result = {'gate1': 'Car validation check: ', 
	'gate1_result': 1, 
	'gate1_message': {0: None, 1: None},
	'gate2': 'Damage presence check: ',
	'gate2_result': 1,
	'gate2_message': {0: None, 1: None},
	'location': x,
	'Injury': y,
	'final': 'Assessment completed!'}
	return result


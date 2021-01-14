import numpy as np
import h5py

# load the saved .h5 file
with h5py.File("/home/hadoop/hadoop/hadoop_working/DataScience/5.MachineLearning/8.DeepLearning/code/tensorflow/demo_data.h5", "r") as f:
	
	# display the list of keys in this file
	keys = list(f.keys())
	print("{0} keys in this file: {1}".format(len(keys), keys))
	# prints 2 keys in this file: ['dataset1', 'dataset2']
	
	# load the numpy array
	data = f.get("dataset1")
	a1   = np.array(data)
	print("Shape of dataset1: {0}".format(a1.shape)) 
	# prints Shape of dataset1: (500, 500)

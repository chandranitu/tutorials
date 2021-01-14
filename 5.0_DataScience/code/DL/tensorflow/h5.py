import numpy as np
import h5py

# create two random numpy arrays
a1 = np.random.random(size = (500, 500))
a2 = np.random.random(size = (1000, 1000))

# save it as a HDF5 file
with h5py.File("/home/hadoop/hadoop/hadoop_working/DataScience/5.MachineLearning/8.DeepLearning/code/tensorflow/demo_data.h5", "w") as f:
	f.create_dataset("dataset1", data=a1)
	f.create_dataset("dataset2", data=a2)


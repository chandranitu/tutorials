from scipy.cluster.vq import kmeans,vq,whiten

#data generation
from numpy import vstack,array 
from numpy.random import rand

# data generation with three features
data = vstack((rand(100,3) + array([.5,.5,.5]),rand(100,3)))
print data


# whitening of data
data = whiten(data)

# K-Means with K = 3 (2 clusters)
cent = kmeans(data,3)
print(cent)

# assign each sample to a cluster
cls,_ = vq(data,cent)
print cls

#Color tagging

#Searching objects by color is a common practice while browsing e-commerce web sites and relying only on the description and the title of the object may not be enough to provide top-notch relevancy. We propose this tool to automatically associate color tags to an image by trying to guess the main object of the picture and extracting its dominant color(s).

#The design of the library can be viewed as a pipeline composed of several sequential processing. Each of these processings accepts several options in order to tune its behavior to better fit your catalog. Those processings are (in order):

#    Resizing and cropping
##    Background detection
#    Skin detection
##    Clustering of remaining pixels
#    Selection of the best clusters
 #   Giving color names to clusters


import cv2
import numpy as np

from /hadoop/hadoop_working/spark_scala_python/ML/code/colorextractor/color_extractor.py import ImageToColor

npz = np.load('hdfs:/ml/color_names.npz')
#iris = sc.textFile('hdfs:/ml/iris.csv')
img_to_color = ImageToColor(npz['samples'], npz['labels'])

img = cv2.imread('image.jpg')
print(img_to_color.get(img))


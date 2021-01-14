#!/usr/bin/python
from os import listdir
from PIL import Image as PImage

def loadImages(path):
    # return array of images
    imagesList = listdir(path)
    loadedImages = []
    for image in imagesList:
        img = PImage.open(path + image)
        loadedImages.append(img)
    return loadedImages

path = "D:\\project\\datascience\\mobile\\train\\scratch\\"

# your images in an array
imgs = loadImages(path)

for img in imgs:
    #  show every image
    img.show()
	
	
#----------
import glob
import imageio

for image_path in glob.glob("D:\project\datascience\mobile\train\scratch\*.png"):
    im = imageio.imread(image_path)
    print (im.shape)
    print (im.dtype)
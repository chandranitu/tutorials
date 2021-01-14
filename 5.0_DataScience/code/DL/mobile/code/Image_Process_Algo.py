# import the necessary packages

from skimage import exposure
import numpy as np
import argparse
import cv2 
import sys
import imutils
from skimage import measure
from imutils import contours


# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-q", "--query", required = True, help = "Path to the query image")
args = vars(ap.parse_args())

# load the query image, compute the ratio of the old height
# to the new height, clone it, and resize it
image = cv2.imread(args["query"])

# load the query image, compute the ratio of the old height to the new height, clone it, and resize it
#image = cv2.imread('D:\First.jpeg')
#Passed Test Cases
#image = cv2.imread('D:\project\datascience\mobile\External.png')
#image = cv2.imread(cv2.samples.findFile('D:\project\datascience\mobile\External.png'))
#try:
#    image.shape
#    print("checked for shape".format(image.shape))
#except AttributeError:
#    print("shape not found")
    #code to move to next frame

ratio = image.shape[0] / 300.0
orig = image.copy()
#image = cv2.resize(image, (0,0), fx=0.3, fy=0.3)
image = imutils.resize(image, height = 300)

# convert the image to grayscale, blur it, and find edges
# in the image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.bilateralFilter(gray, 11, 17, 17)
edged = cv2.Canny(gray, 30, 200)

# find contours in the edged image, keep only the largest
# ones, and initialize our screen contour
(_, cnts, h) = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:10]
screenCnt = None
#print ("contours found: {}", cnts)
out1 = imutils.resize(image, height = 300)
cv2.imshow("Screen Detection", out1)
cv2.waitKey(0)


# loop over our contours
for c in cnts:
	# approximate the contour
	peri = cv2.arcLength(c, True)
	#print("peri value is {0}",peri)
	approx = cv2.approxPolyDP(c, 0.02 * peri, True)
	#print("approx value is {0} and length is {1}", approx, len(approx))
	# if our approximated contour has four points, then
	# we can assume that we have found our screen
	if len(approx) == 4:
		screenCnt = approx
		break

#print("Contour information is {0}",screenCnt)

if screenCnt is None or len(screenCnt) == 0:
	print("Algo 2 need to works")
	a2_warp = cv2.cvtColor(orig, cv2.COLOR_BGR2GRAY)
	a2_warp = exposure.rescale_intensity(a2_warp, out_range = (0, 255))
	
	screen_gray = cv2.bilateralFilter(a2_warp, 11, 17, 17)
	screen_edged = cv2.Canny(screen_gray, 30, 200)

	kernel = np.ones((5,5), np.uint8)

	out2 = imutils.resize(screen_edged, height = 300)
	cv2.imshow("Crack Detection", out2)
	cv2.waitKey(0)
	img_dilation = cv2.dilate(screen_edged, kernel, iterations=1)
	out3 = imutils.resize(img_dilation, height = 300)
	cv2.imshow("After dialation Crack Detection", out3)
	cv2.waitKey(0)
	img_erosion = cv2.erode(img_dilation, kernel, iterations=1)
	out4 = imutils.resize(img_erosion, height = 300)
	cv2.imshow("After erosion Crack Detection", out4)
	cv2.waitKey(0)

	thresh = cv2.threshold(img_dilation, 200, 255, cv2.THRESH_BINARY)[1]

	# perform a connected component analysis on the thresholded
	# image, then initialize a mask to store only the "large"
	# components
	labels = measure.label(thresh, neighbors=8, background=0)
	mask = np.zeros(thresh.shape, dtype="uint8")
	#print("labels {0}",labels)
	
	# save the cropped image to file
	cv2.imwrite("cropped.png", thresh)
	out5 = imutils.resize(thresh, height = 500)
	cv2.imshow("Done", out5)
	cv2.waitKey(0)
	# loop over the unique components
	for label in np.unique(labels):
		# if this is the background label, ignore it
		if label == 0:
			continue

		# otherwise, construct the label mask and count the
		# number of pixels 
		labelMask = np.zeros(thresh.shape, dtype="uint8")
		labelMask[labels == label] = 255
		numPixels = cv2.countNonZero(labelMask)
		#print("numPixels {0}",numPixels)
		# if the number of pixels in the component is sufficiently
		# large, then add it to our mask of "large blobs"
		if numPixels > 300:
			mask = cv2.add(mask, labelMask)
			
	# find the contours in the mask, then sort them from left to
	# right
	#print("Mask {0}",mask)
	cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)
	cnts = cnts[0] if imutils.is_cv2() else cnts[1]
	#print ("cnt are {0}",cnts)
	
	if len(cnts) == 0:
		print("No crack found in screen..")
	else:
		print("find cracks at below coordinates..")
		cnts = contours.sort_contours(cnts)[0]
		print(cnts)
		# loop over the contours
		for (i, c) in enumerate(cnts):
			# draw the bright spot on the image
			(x, y, w, h) = cv2.boundingRect(c)
			((cX, cY), radius) = cv2.minEnclosingCircle(c)
			cv2.circle(orig, (int(cX), int(cY)), int(radius),
				(0, 0, 255), 2)
		cv2.putText(orig, "#{}".format(i + 1), (x, y - 15),
				cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)
		
		image_a2 = imutils.resize(orig, height = 500)
		cv2.imshow("Screen Detection", image_a2)
		cv2.waitKey(0)		
	
else:
	cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 1)
	out7 = imutils.resize(image, height = 500)
	cv2.imshow("Screen Detection", out7)
	cv2.waitKey(0)

	# now that we have our screen contour, we need to determine
	# the top-left, top-right, bottom-right, and bottom-left
	# points so that we can later warp the image -- we'll start
	# by reshaping our contour to be our finals and initializing
	# our output rectangle in top-left, top-right, bottom-right,
	# and bottom-left order
	pts = screenCnt.reshape(4, 2)
	rect = np.zeros((4, 2), dtype = "float32")

	# the top-left point has the smallest sum whereas the
	# bottom-right has the largest sum
	s = pts.sum(axis = 1)
	rect[0] = pts[np.argmin(s)]
	rect[2] = pts[np.argmax(s)]

	# compute the difference between the points -- the top-right
	# will have the minimum difference and the bottom-left will
	# have the maximum difference
	diff = np.diff(pts, axis = 1)
	rect[1] = pts[np.argmin(diff)]
	rect[3] = pts[np.argmax(diff)]

	# multiply the rectangle by the original ratio
	rect *= ratio
	print (" Actual screen detected at {0}",rect)
	# now that we have our rectangle of points, let's compute
	# the width of our new image
	(tl, tr, br, bl) = rect
	widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
	widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))

	# ...and now for the height of our new image
	heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
	heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))

	# take the maximum of the width and height values to reach
	# our final dimensions
	maxWidth = max(int(widthA), int(widthB))
	maxHeight = max(int(heightA), int(heightB))

	# construct our destination points which will be used to
	# map the screen to a top-down, "birds eye" view
	dst = np.array([
		[0, 0],
		[maxWidth - 1, 0],
		[maxWidth - 1, maxHeight - 1],
		[0, maxHeight - 1]], dtype = "float32")
	#print ("dst is {0}",dst)
	# calculate the perspective transform matrix and warp
	# the perspective to grab the screen
	M = cv2.getPerspectiveTransform(rect, dst)
	#print ("M is {0}",M)
	warp = cv2.warpPerspective(orig, M, (maxWidth, maxHeight))
	final_warp = warp.copy()
	#warp = cv2.resize(warp, (0,0), fx=0.3, fy=0.3)
	out8 = imutils.resize(warp, height = 500)
	cv2.imshow("Actual Mobile Screen", out8)
	cv2.waitKey(0)


	warp = cv2.cvtColor(warp, cv2.COLOR_BGR2GRAY)
	warp = exposure.rescale_intensity(warp, out_range = (0, 255))
	(h, w) = warp.shape
	(dX, dY) = (int(w * 0.99), int(h*0.99))
	crop = warp[h-dY:dY, w - dX:w]
	 
	# save the cropped image to file
	cv2.imwrite("cropped.png", crop)
	out9 = imutils.resize(crop, height = 500)
	cv2.imshow("Resize", out9)
	cv2.waitKey(0)


	# Find the edges in extracted screen
	#screen_gray = cv2.cvtColor(warp, cv2.COLOR_BGR2GRAY)
	screen_gray = cv2.bilateralFilter(crop, 11, 17, 17)
	screen_edged = cv2.Canny(screen_gray, 30, 200)

	kernel = np.ones((5,5), np.uint8)
	out10 = imutils.resize(screen_edged, height = 500)
	cv2.imshow("Crack Detection", out10)
	cv2.waitKey(0)
	img_dilation = cv2.dilate(screen_edged, kernel, iterations=1)
	out11 = imutils.resize(img_dilation, height = 500)
	cv2.imshow("After dialation Crack Detection", out11)
	cv2.waitKey(0)
	# img_erosion = cv2.erode(img_dilation, kernel, iterations=1)
	# out12 = imutils.resize(img_erosion, height = 500)
	# cv2.imshow("After erosion Crack Detection", out12)
	# cv2.waitKey(0)

	thresh = cv2.threshold(img_dilation, 200, 255, cv2.THRESH_BINARY)[1]

	# perform a connected component analysis on the thresholded
	# image, then initialize a mask to store only the "large"
	# components
	labels = measure.label(thresh, neighbors=8, background=0)
	mask = np.zeros(thresh.shape, dtype="uint8")
	#print("labels {0}",labels)
	# loop over the unique components
	for label in np.unique(labels):
		# if this is the background label, ignore it
		if label == 0:
			continue

		# otherwise, construct the label mask and count the
		# number of pixels 
		labelMask = np.zeros(thresh.shape, dtype="uint8")
		labelMask[labels == label] = 255
		numPixels = cv2.countNonZero(labelMask)
		#print("numPixels {0}",numPixels)
		# if the number of pixels in the component is sufficiently
		# large, then add it to our mask of "large blobs"
		if numPixels > 300:
			mask = cv2.add(mask, labelMask)
			
	# find the contours in the mask, then sort them from left to
	# right
	#print("Mask {0}",mask)
	cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)
	cnts = cnts[0] if imutils.is_cv2() else cnts[1]
	#print ("cnt are {0}",cnts)

	if len(cnts) == 0:
		print("No crack(s) found..")
		
		# show the output image
		temp_org = cv2.cvtColor(orig, cv2.COLOR_BGR2GRAY)
		h1 , w1 = temp_org.shape
		temp_forg = cv2.cvtColor(final_warp, cv2.COLOR_BGR2GRAY)
		h2 , w2 = temp_forg.shape
		(dX1, dY1) = (int((h1 - h2) * 0.54), int((w1 - w2) * 0.55))
		#print ("values are {0},{1},{2},{3},{4},{5} are ",dX1,dY1,h2,w2 , h1,w1)
		orig[dX1:dX1+h2,dY1:dY1+w2] = final_warp
		#temp = cv2.resize(orig, (0,0), fx=0.3, fy=0.3)
		temp = imutils.resize(orig, height = 500)
		cv2.imshow("Image", temp)
		cv2.waitKey(0)
	else:
		print("cracks found at below coordinates..")
		cnts = contours.sort_contours(cnts)[0]
		print(cnts)
		# loop over the contours
		for (i, c) in enumerate(cnts):
			# draw the bright spot on the image
			(x, y, w, h) = cv2.boundingRect(c)
			((cX, cY), radius) = cv2.minEnclosingCircle(c)
			cv2.circle(final_warp, (int(cX), int(cY)), int(radius),
				(0, 0, 255), 2)
		cv2.putText(final_warp, "#{}".format(i + 1), (x, y - 15),
				cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)

		# show the output image
		temp_org = cv2.cvtColor(orig, cv2.COLOR_BGR2GRAY)
		h1 , w1 = temp_org.shape
		temp_forg = cv2.cvtColor(final_warp, cv2.COLOR_BGR2GRAY)
		h2 , w2 = temp_forg.shape
		(dX1, dY1) = (int((h1 - h2) * 0.52), int((w1 - w2) * 0.52))
		#print ("values are {0},{1},{2},{3},{4},{5} are ",dX1,dY1,h2,w2 , h1,w1)
		#orig[dX1:dX1+h2,dY1:dY1+w2] = final_warp
		orig[int(tl[1]):int(tl[1]+h2),int(tl[0]):int(tl[0]+w2)] = final_warp
		#temp = cv2.resize(orig, (0,0), fx=0.5, fy=0.5)
		res = imutils.resize(orig, height = 500)
		cv2.imshow("Image", res)
		cv2.waitKey(0)
		
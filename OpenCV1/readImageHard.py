# import the necessary packages
import numpy as np
import cv2
import math
import numpy as np

def order_points(pts):
# 	# initialzie a list of coordinates that will be ordered
# 	# such that the first entry in the list is the top-left,
# 	# the second entry is the top-right, the third is the
# 	# bottom-right, and the fourth is the bottom-left
	rect = np.zeros((4, 2), dtype = "float32")
# 	# the top-left point will have the smallest sum, whereas
	# the bottom-right point will have the largest sum
	s = pts.sum(axis = 1)
	rect[0] = pts[np.argmin(s)]
	rect[2] = pts[np.argmax(s)]
	# now, compute the difference between the points, the
	# top-right point will have the smallest difference,
	# whereas the bottom-left will have the largest difference
	diff = np.diff(pts, axis = 1)
	rect[1] = pts[np.argmin(diff)]
	rect[3] = pts[np.argmax(diff)]
	# return the ordered coordinates
	return rect




def rotateImage(image, angle):
	image_center = tuple(np.array(image.shape[1::-1]) / 2)
	rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
	result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
	return result

def four_point_transform(image, pts):
	# obtain a consistent order of the points and unpack them
	# individually
	rect = order_points(pts)
	(tl, tr, br, bl) = rect
	# compute the width of the new image, which will be the
	# maximum distance between bottom-right and bottom-left
	# x-coordiates or the top-right and top-left x-coordinates
	widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
	widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
	maxWidth = max(int(widthA), int(widthB))
	# compute the height of the new image, which will be the
	# maximum distance between the top-right and bottom-right
	# y-coordinates or the top-left and bottom-left y-coordinates
	heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
	heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
	maxHeight = max(int(heightA), int(heightB))
	# now that we have the dimensions of the new image, construct
	# the set of destination points to obtain a "birds eye view",
	# (i.e. top-down view) of the image, again specifying points
	# in the top-left, top-right, bottom-right, and bottom-left
	# order
	dst = np.array([
		[0, 0],
		[maxWidth - 1, 0],
		[maxWidth - 1, maxHeight - 1],
		[0, maxHeight - 1]], dtype = "float32")
	# compute the perspective transform matrix and then apply it
	M = cv2.getPerspectiveTransform(rect, dst)
	warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))
	# return the warped image
	return warped

#
image = cv2.imread("testHard.jpg")
imagesize = image.shape
image = cv2.GaussianBlur(image,(5,5),0)
image = cv2.GaussianBlur(image,(5,5),0)
# image2 = image


# image = cv2.GaussianBlur(image,(5,5),0)


# print(imagesize)



ptslist = [(721,47), (360, 45),(650, 290), (200, 290)]
# (650,30), (300, 30),(650, 330), (300, 330) perfect square around circle
# (680,50), (330, 70),(620, 280), (270, 280) very close
#  [(730,15), (370, 15),(580, 330), (220, 330)] most final
# (720,45), (360, 45),(650, 290), (200, 290) Elisa can fuck with hough circles
# (730,45), (350, 40),(665, 295), (210, 290) Elias thinks it looks better
#720,45

startpt = (735,50) #(725, 50)
endpt = (360, 50) #(375, 50)
startpt2 = (650, 290) #(575, 300), (590,300)
endpt2 = (200, 290) #(225,300)

color = (0, 255, 0)

# imageLine = cv2.line(image, startpt, endpt, color, 9)
# imageLine = cv2.line(imageLine,startpt2, endpt2, color, 9)
# imageLine = cv2.line(imageLine,startpt, startpt2, color, 9)
# imageLine = cv2.line(imageLine, endpt, endpt2, color, 9)
#
# leftLine = math.sqrt((225 - 375)**2 + (300 - 45)**2)
# rightLine = math.sqrt((575 - 725)**2 + (300 - 45)**2)

# print("Left Line : ", leftLine)
# print("Right Line: ", rightLine)


pts = np.array(ptslist, dtype = "float32")
# apply the four point tranform to obtain a "birds eye view" of
# the image



warped = four_point_transform(image, pts)
# image2 = rotateImage(warped, 60)

width = warped.shape[1] + 9
# 9
height = 449  #395 420
#449 BEST YET
dim = (width, height)



resized = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
resized = cv2.resize(resized, dim, interpolation = cv2.INTER_AREA)

circles = cv2.HoughCircles(resized, cv2.HOUGH_GRADIENT, 1.2, 100)
radi = []
xlist = []
ylist = []
# cv2.imshow("Resized", resized)
# show the original and warped images
if circles is not None:
    circles = np.round(circles[0, :]).astype("int")
    for (x, y, r) in circles:

        radi.append(r)
        xlist.append(x)
        ylist.append(y)
        # print(r)
#
    print("the max radius is " , max(radi))

    maxradi = max(radi)


    for (x, y, r) in circles:
        if r == maxradi:
            cv2.circle(resized, (x, y), r, (0, 255, 0), 4)
            cv2.rectangle(resized, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)



# params = cv2.SimpleBlobDetector_Params()
#
# params.filterByArea = True
# params.minArea = 3000
#
# params.filterByCircularity = False
# # params.minCircularity = 0.05
#
# params.filterByConvexity = False
# # params.minConvexity = 0.0025
#
# params.filterByInertia = False
# # params.minInertiaRatio = 0.05
#
# detector = cv2.SimpleBlobDetector_create(params)

# keypoints = detector.detect(resized)

# blank = np.zeros((1, 1))
# blobs = cv2.drawKeypoints(resized, keypoints, blank, (0, 0, 255),
#                           cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
#
# number_of_blobs = len(keypoints)
# text = "Number of Circular Blobs: " + str(len(keypoints))
# cv2.putText(blobs, text, (20, 550),
#             cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 100, 255), 2)
#
# cv2.imshow("Blobs", blobs)
# s




cv2.imshow("Original", image)

cv2.imshow("Warped", resized)
# cv2.imshow("Rotated", image2)
cv2.waitKey(0)

# cv2.imshow("humpday", image)
# cv2.waitKey(0)
import cv2
import numpy as np
import imutils

img = cv2.imread('pic2.jpg')
ratio = img.shape[0] /500
orig = img.copy()
img = imutils.resize(img, height = 500)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (5,5),0)

low = 75
high = 200
#was 50 and 100
edges = cv2.Canny(gray,low,high)


rho = 1 #distance resolution in pixels of the Hough grid
threshold = 20 #min number of votes
theta = np.pi/180 #angular resolution in radians of the Hough grid
min_line_length = 100 #min number of pixels making up a line(100)
max_line_gap = 30 #max gap in pixels between connectable line segments (20)
line_image = np.copy(img) * 0
lines = cv2.HoughLinesP(edges, rho, theta, threshold, np.array([]), min_line_length, max_line_gap)

thirdline = []
largestLine = []

for line in lines:
    for x1,y1,x2,y2 in line:
        largestLine.append(y2-y1)
        # cv2.line(line_image, (x1,y1), (x2,y2), (255,20,147),1)
        # lines_edges = cv2.addWeighted(img,0.8, line_image, 1, 0)

        # thirdline.append(x1)
        # thirdline.append(y1)
        # thirdline.append(x2)
        # thirdline.append(y2)

repeat = largestLine.copy()
# print(repeat)
largestLineFinal = max(largestLine)
largestLine.remove(largestLineFinal)
largestLineFinal2 = max(largestLine)

print(largestLineFinal2)
print(largestLineFinal)

only1 = 0
only2 = 0

for line in lines:
    for x1,y1,x2,y2 in line:
        a = y2 -y1
        if(only2<1):
            if a == largestLineFinal:
                # print('here')
                cv2.line(line_image, (x1,y1), (x2,y2), (255,20,147),1)
                lines_edges = cv2.addWeighted(img,0.8, line_image, 1, 0)

                thirdline.append(x1)
                thirdline.append(y1)
                thirdline.append(x2)
                thirdline.append(y2)
                only2 = only2 + 1

        if(only1<1):
            if a == largestLineFinal2:
                # print('here')
                cv2.line(line_image, (x1,y1), (x2,y2), (255,20,147),1)
                lines_edges = cv2.addWeighted(img,0.8, line_image, 1, 0)

                thirdline.append(x1)
                thirdline.append(y1)
                thirdline.append(x2)
                thirdline.append(y2)
                only1 = only1 + 1





pointAx = int((thirdline[0] + thirdline[4])/2)
pointAy = int((thirdline[5]+thirdline[1])/2)

pointBx = int((thirdline[2] + thirdline[6])/2)
pointBy = int((thirdline[7]+thirdline[3])/2)
# print(pointAx,pointAy,pointBx,pointBy)
if abs(pointBx) + abs(pointBy)>abs(pointAx) + abs(pointAy):
    cv2.arrowedLine(lines_edges, (pointBx, pointBy), (pointAx, pointAy), (0,0,255), 2)
elif abs(pointAy) + abs(pointAx)> abs(pointBx) + abs(pointBy):
    cv2.arrowedLine(lines_edges, (pointBx, pointBy), (pointAx, pointAy), (0, 0, 255), 2)

midpointx = int((pointAx + pointBx)/2)
midpointy = int((pointAy+pointBy)/2)

cv2.circle(lines_edges, (midpointx,midpointy), 2, (0,255,0), 5)

cv2.imwrite('picFinal.jpg',lines_edges)
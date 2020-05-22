import cv2
import numpy as np
import imutils

img = cv2.imread('image.jpg')
ratio = img.shape[0] /500
orig = img.copy()
img = imutils.resize(img, height = 500)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (9,9),0)

low = 55
high = 115
edges = cv2.Canny(gray,low,high)

h=500
start = 0

sh = 500
eh = 500
end = 374
middle = 187

cake = 0
cake2 = 4
x3 = 5
x4 = 1
x5 = 2
x6 = 6
x7 = 7
x8 = 3

ypoop1 = 500
ypoop2 = 500
pointAx = 187
pointAy = 500
pointBx = 0
saved = []

manp = 0
mank = 1
manp2 = 2
pank = 3
while h>500-40:
    thirdline = []

    # outlining triangles because honestly what the fuck is up
    cv2.line(img, (pointAx - 187, ypoop1), (pointAx + 187, ypoop2), (0, 255, 0), 2)
    cv2.line(img, (pointAx - 187, ypoop1), (pointAx, pointAy - 160), (0, 255, 0), 2)
    cv2.line(img, (pointAx + 187, ypoop2), (pointAx, pointAy - 160), (0, 255, 0), 2)

    # t = np.array([[(start, h), (end, h), (middle, h-40)]])
    print( "ax " + str(pointAx))
    print( "ay " + str(pointBx))
    t = np.array([[(pointAx-187,ypoop1), (pointAx + 187, ypoop2), (pointAx, pointAy-160)]])
    # cv2.fillPoly(img, t, 255)
    # period = np.array([[()]])
    mask = np.zeros_like(edges)
    cv2.fillPoly(mask, t, 255)
    mask_image = cv2.bitwise_and(edges, mask)


    # (pointAx - 187, ypoop1), (pointAx + 187, ypoop2), (pointAx, pointAy - 40)

    rho = 1  # distance resolution in pixels of the Hough grid
    threshold = 20  # min number of votes
    theta = np.pi / 180  # angular resolution in radians of the Hough grid
    min_line_length = 10  # min number of pixels making up a line(100)
    max_line_gap = 40  # max gap in pixels between connectable line segments (30)
    line_image = np.copy(img) * 0
    lines = cv2.HoughLinesP(mask_image, rho, theta, threshold, np.array([]), min_line_length, max_line_gap)
    left = []
    # for x in range(0,len(lines)):
    #     for x1,y1,x2,y2 in lines[x]:
    #         leftest = (x1+x2)/2
    #         left.append(leftest)
    #         #rightest will be max in the list and leftest will be min in the list
    # mostleft = min(left)
    # # print("left "+ str(mostleft))
    # mostright = max(left)
    # print("r " + str(mostright))



    if lines is None:
        pass
    else:
        for x in range(0, len(lines)):
            for x1, y1, x2, y2 in lines[x]:
                # print("fina " + str((x1+x2)/2))
                # if (x1+x2)/2 == mostleft:

                    thirdline.append(x1)
                    thirdline.append(y1)
                    thirdline.append(x2)
                    thirdline.append(y2)
                    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
                    # cv2.circle(img, (x2,y2), 5,255)
                    # saved.append(x2)
                    # saved.append(y2)
                # if (x1+x2)/2 == mostright:
                #     thirdline.append(x1)
                #     thirdline.append(y1)
                #     thirdline.append(x2)
                #     thirdline.append(y2)
                #     cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
    # print( "at one")
    # print(thirdline)

    # cake = 0
    # cake2 = 4
    #
    # if saved[manp] - saved[manp2]> 20:
    #     kaype = (saved[manp] + saved[manp])/2
    #     pankie = (saved[pank] + saved[mank])/2
    #     kaype = int(kaype)
    #     pankie = int(pankie)
    #
    #     cv2.circle(img, (kaype, pankie), 5, 10)

    # manp = manp+1
    # manp2 = manp2 + 1
    # mank = mank+1
    # pank = pank + 1
    pointAx = int((thirdline[cake] + thirdline[cake2]) / 2)
    pointAy = int((thirdline[x3] + thirdline[x4]) / 2)

    pointBx = int((thirdline[x5] + thirdline[x6]) / 2)
    pointBy = int((thirdline[x7] + thirdline[x8]) / 2)


    print("point a " + str(pointAx))
    if pointAx-thirdline[cake] <50:
        pass
    if pointAx-thirdline[cake2] <50:
        pass
    if pointAx - thirdline[x5]<50:
        pass
    if pointAx - thirdline[x6] < 50:
        pass
    if pointBx-thirdline[x5] <50:
        pass
    if pointBx - thirdline[cake] < 50:
        pass
    if pointBx - thirdline[cake2] < 50:
        pass
    if pointBx-thirdline[x6] <50:
        pass
    else:
        slope = (pointBy-pointAy)/(pointBx-pointAx)
        normal = -1/slope
        normal = int(normal)
        ypoop1=500 -  (normal*(pointBx + 187 - pointBx) + pointBy)
        ypoop2 =500 - (normal*(pointBx - 187 - pointBx) + pointBy)
        print("y1 " + str(ypoop1))
        print("y2 " + str(ypoop2))
        cv2.arrowedLine(img,  (pointAx, pointAy), (pointBx, pointBy), (0, 0, 255), 2)
        cv2.line(img, (pointAx, pointAy), (pointBx, pointBy), (0, 255, 0), 2)




        # if pointAx > pointBx:
        #     # end point is to the left of the starting point
        #     cv2.arrowedLine(img, (pointAx, pointAy), (pointBx, pointBy), (0, 0, 255), 2)
        # else:
        #     # end point is to the right of the starting point
        #     cv2.arrowedLine(img, (pointAx, pointAy), (pointBx, pointBy), (255, 0, 0), 2)


    cake = cake + 8

    cake2 = cake2 + 8
    x3 = x3 + 8
    x4 = x4 + 8
    x5 = x5 + 8
    x6 = x6 + 8
    x7 = x7 + 8
    x8 = x8 + 8




        # pts = np.array([[(start, pointAy), (end, pointAy), (pointAx, pointAy-10)]])
        #
        # cv2.fillPoly(img, pts, 255)
        # sh = sh + 10
        #
        # eh = eh -10
        # middle = middle + 5



    # print(len(lines))



    h = h - 160

cv2.imwrite('picFinal.jpg', img)
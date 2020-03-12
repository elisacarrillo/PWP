import numpy as np
import argparse
import cv2

image = cv2.imread("testEasy.jpg")
# imagesize = image.shape
# cv2.resize(image, imagesize)

image = cv2.GaussianBlur(image,(5,5),0)
output = image.copy()
print("Image Done")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
radi = []
xlist = []
ylist = []


# detect circles in the image
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2, 100)
#550
# ensure at least some circles were found
if circles is not None:
    circles = np.round(circles[0, :]).astype("int")
    for (x, y, r) in circles:

        radi.append(r)
        xlist.append(x)
        ylist.append(y)
        # print(r)

    # print("the max radius is " , max(radi))

    maxradi = max(radi)
    # for f in radi:
    #     if (f == maxradi):
    #         lmao = f
    #         cv2.circle(output, (x, y), r, (0, 255, 0), 4)
    #         cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)


    for (x, y, r) in circles:
        if r == maxradi:
            cv2.circle(output, (x, y), r, (0, 255, 0), 4)
            cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)






        # show the output image
    # cv2.imshow("original", image)
    cv2.imshow("output", np.hstack([image, output]))
    # cv2.write("final.jpg",output)
    cv2.waitKey(0)
    print("Completed")
    # cv2.destroyAllWindows()
    # cv2.destroyAllWindows()



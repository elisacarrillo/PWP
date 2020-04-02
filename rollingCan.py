import numpy as np
import cv2

vid = cv2.VideoCapture('can.avi')
while vid.isOpened():
    ret, frame = vid.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.blur(gray, (5,5))
    gray = cv2.blur(gray, (5,5))
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2, 100)
    radi = []
    xlist = []
    ylist = []

    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        for (x, y, r) in circles:
            radi.append(r)
            xlist.append(x)
            ylist.append(y)

        max_radi = max(radi)

        for (x, y, r) in circles:
            if r == max_radi:
                cv2.circle(gray, (x, y), r, (0, 255, 0), 4)
                cv2.rectangle(gray, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)

    cv2.imshow('frame', gray)
    # cv2.waitKey(0)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
vid.release()
cv2.destroyAllWindows()

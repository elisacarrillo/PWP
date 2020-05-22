import numpy as np
import cv2

vid = cv2.VideoCapture('3674.mp4')
while vid.isOpened():
    ret, frame = vid.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)

    low = 20
    high = 100
    # was 50 and 100
    edges = cv2.Canny(gray, low, high)

    t = np.array([[(500, 900), (1300, 900), (1000, 450)]])
    # cv2.fillPoly(frame, t, 255)
    # period = np.array([[()]])
    mask = np.zeros_like(edges)
    cv2.fillPoly(mask, t, 255)
    mask_image = cv2.bitwise_and(edges, mask)

    rho = 1  # distance resolution in pixels of the Hough grid
    threshold = 20  # min number of votes
    theta = np.pi / 180  # angular resolution in radians of the Hough grid
    min_line_length = 10  # min number of pixels making up a line(100)
    max_line_gap = 40  # max gap in pixels between connectable line segments (30)
    line_image = np.copy(gray) * 0
    lines = cv2.HoughLinesP(mask_image, rho, theta, threshold, np.array([]), min_line_length, max_line_gap)

    a_line = 0
    cv2.circle(frame, (100, 100), 20, (0, 0, 255), 45)
    tilt = []
    if lines is None:
        cv2.circle(frame, (100, 100), 20, (255, 0, 0), 45)
    else:
        for x in range(0, len(lines)):
            for x1, y1, x2, y2 in lines[x]:
                if y2-y1 > a_line:
                    a_line = y2 - y1

                else:
                    pass
                # a_line.append(y1)
                # a_line.append(x2)
                # a_line.append(y2)


        print("a" + str(a_line))
        for x in range(0, len(lines)):
            for x1, y1,x2,y2 in lines[x]:
                if y2 - y1 == a_line:
                    difference = x2 - x1
                    difference = abs(difference)
                    cv2.line(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
                    print("d" + str(difference))
                    if difference > 50:#was 50
                        cv2.circle(frame, (100,100), 20, (255,0,0), 45)

                    elif y2-y1<30:
                        cv2.circle(frame, (100, 100), 20, (255, 0, 0), 45)

                        #only read largest lines
                    else:
                        cv2.circle(frame, (100, 100), 20, (0, 0, 255), 45)

    # mx = max(a_line)
    # a_line.remove(mx)




    # cv2.fillPoly(gray, t, 244)
    cv2.imshow('frame', frame)
    # cv2.waitKey(0)
    if cv2.waitKey(17) & 0xFF == ord('q'):
        break
vid.release()
cv2.destroyAllWindows()
import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)

while (1):
    _, frame = cap.read()
    hsv_frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    low_red = np.array([161,155,84])
    high_red = np.array([179,255,255])
    red_mask = cv.inRange(hsv_frame, low_red, high_red)
    red = cv.bitwise_and(frame, frame, mask=red_mask)

    cv.imshow("Frame", frame)
    cv.imshow("Red", red)
    cv.imshow("Mask", red_mask)
    cv.waitKey(1)
import cv2, numpy, os, time

cap = cv2.VideoCapture(0)

time.sleep(0.5)

ret, frame = cap.read()

cv2.imshow("IMAGE", frame)

key = cv2.waitKey(0)

if key != ord('q'):
    pass

cap.release()


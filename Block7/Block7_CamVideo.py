import cv2, numpy, os

image = cv2.imread(os.path.expanduser("~/Downloads/IMG_2533.jpeg"))

cap = cv2.VideoCapture(0)

key = cv2.waitKey(1)

while key != 27:
    key = cv2.waitKey(1)
    ret, frame = cap.read()
    cv2.imshow("IMAGE", cv2.flip(frame, 1))

# key = cv2.waitKey(0)
# if key != ord('q'):
#     pass

cap.release()

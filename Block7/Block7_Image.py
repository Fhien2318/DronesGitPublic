import cv2, numpy, os

image = cv2.imread(os.path.expanduser("~/Downloads/IMG_2533.jpeg"))

cv2.imshow("IMAGE", image)


while cv2.waitKey(0) != ord('q'):
    pass



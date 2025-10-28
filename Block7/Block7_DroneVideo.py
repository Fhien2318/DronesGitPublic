import cv2, numpy, os
from pioneer_sdk import Pioneer, Camera

mini = Pioneer()
camera = Camera()

key = -1

while key != 27:
    key = cv2.waitKey(1)
    frame = camera.get_cv_frame()
    if frame is not None:
        cv2.imshow("IMAGE", frame)

# key = cv2.waitKey(0)
# if key != ord('q'):
#     pass


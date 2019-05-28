import cv2

from cv2 import *

namedWindow("webcam")
vc = VideoCapture(0);

while True:
    next, frame = vc.read()
    imshow("webcam", frame)
    if waitKey(50) >= 0:
        break;

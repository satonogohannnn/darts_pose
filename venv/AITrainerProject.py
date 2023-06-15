import cv2
import numpy as np
import time
import PoseModule as pm

cap = cv2.VideoCapture("AITrainer/sato_2.mp4")
detector = pm.poseDetector()

while True:
    success, img = cap.read()
    img = cv2.resize(img, (1080, 1920))
    # img = cv2.imread("AITrainer/test1.jpg")
    img, results = detector.findPose(img)
    # lmList = detector.findPosition(img, False)
    # print(lmList)

    cv2.imshow("Image", img)
    cv2.waitKey(1)

import cv2
import time
from skimage import io
import numpy as np
def face_recog(userImg, verifyImg):
    # try:
    responseSend = {}
    responseSend["isFaceVerified"]=False
    def reverse(tuples):
        new_tup = tuples[::-1]
        return new_tup

    # Askikng for input
    #orign = input("mmm: ")
    #check = input("mmm: ")

    # Store the image into variable
    userImg= io.imread(userImg)
    verifyImg= io.imread(verifyImg)
    original = cv2.imread(np.array(userImg))
    duplicate = cv2.imread(np.array(verifyImg))

    # Store the image shape into variable
    ori_shape = original.shape[:2]
    dup_shape = duplicate.shape[:2]

    rot_shape = reverse(dup_shape)
        # pause()
    if ori_shape == dup_shape:
        # Extract the difference of color element between two image
        difference = cv2.subtract(original, duplicate)
        b, g, r = cv2.split(difference)

        # TEST 2: Based on color of image
        if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
            responseSend["isFaceVerified"]=True
        # cv2.imshow('Difference', difference)
        #cv2.imshow("Duplicate",  duplicate)
    # except:
    #     print("error")
    return responseSend
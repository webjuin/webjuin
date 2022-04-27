# https://g0pher.tistory.com/104

import glob, os
import cv2
import numpy as np

categ = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

for dir in categ:
    img_dir = './' + dir + '/'
    for ff in os.listdir(img_dir):
        file = img_dir + ff
        img = cv2.imread(file)
        
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = np.float32(gray)
        dst = cv2.cornerHarris(gray, 2, 3, 0.04)
        pp = cv2.dilate(dst, None)
        print(pp)
        
        img[dst>0.01*dst.max()]=[0,0,255]
        
        cv2.imshow('dst', img)
        cv2.waitKey(1000)
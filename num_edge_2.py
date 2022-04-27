# https://koreapy.tistory.com/1186

import glob, os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

def norm_digit(img):
    # 무게 중심 좌표 추출
    m = cv2.moments(img)
    cx = m['m10'] / m['m00']
    cy = m['m01'] / m['m00']
    h, w = img.shape[:2]
    
    # affine 행렬 생성
    aff = np.array([[1, 0, w/2 - cx], [0, 1, h/2 - cy]], dtype=np.float32)
    
    # warpAffine을 이용해 기하학 변환
    dst = cv2.warpAffine(img, aff, (0, 0))
    return dst

#print(cre[0][0:1])

categ = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
res = []
X = []; Y = []
for dir in categ:
    img_dir = './' + dir + '/'
    #X = []; Y = []
    for ff in os.listdir(img_dir):
        file = img_dir + ff
        img = cv2.imread(file)
        img = img[20:200, 20:200, :]
        
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        a, b = gray.shape
        bb = np.zeros((a, b))
        
        corners = cv2.goodFeaturesToTrack(gray, 80, 0.01, 25)
        corners = np.int32(corners)
        
        
        for corner in corners:
            x, y = corner[0]
            cv2.circle(bb, (x, y), 5, 255, 1, cv2.LINE_AA)
        m = cv2.moments(bb)
        cx = m['m10'] / m['m00']
        cy = m['m01'] / m['m00']
        print(cx, cy)
        X.append(cx)
        Y.append(cy)
        
        #plt.plot(cx, cy, 'r.')
        #plt.pause(0.1)
        #cv2.imshow('dst', img)
        #cv2.imshow('bb', bb)
        #cv2.waitKey(3000)
        #plt.clf()
    
plt.plot(X, Y, '#FFFF00.')
plt.show()

    
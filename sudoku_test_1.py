# https://g0pher.tistory.com/104

import pandas as pd
import cv2
from datetime import datetime
#import NUM_INPUT_ML_1

img = cv2.imread('test_5.jpg')
img = img[266:948, 10:688, :]   
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
a, b = img_gray.shape
print(a, b)

for i in range(9):
        for j in range(9):
                A = img[i*76:i*76+76, j*75:j*75+75]
                A = cv2.resize(A, dsize=(224, 224))
                ret, thr = cv2.threshold(A, 127, 255, cv2.THRESH_BINARY)
                B = thr[20:200, 20:200]
                #print(sum(sum(sum(thr[20:200, 20:200] < 1))))
                now = datetime.now()
                print(now.strftime('%y%m%d%H%M%S'))
                cv2.imshow('A', A)
                cv2.imshow('B', B)
                cv2.imshow('thr', thr)
                cv2.imshow('img', img)
                if sum(sum(sum(thr[20:200, 20:200] < 1))) > 1000:
                        file_name = 'num_'+str(now.strftime('%y%m%d%H%M%S'))+'.jpg'
                        cv2.imwrite(file_name, A)
                        #res = NUM_INPUT_ML_1.image_num(A)
                        #print(res)
                cv2.waitKey(1000)

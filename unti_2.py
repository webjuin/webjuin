# https://g0pher.tistory.com/104

import pandas as pd
import cv2
import matplotlib.pyplot as plt
import glob, os
import numpy as np
import pandas as pd

def var_pos(binary):
    r, c = binary.shape
    II = []; JJ=[]
    for i in range(r):
        for j in range(c):
            if binary[i, j] > 0:
                II.append(i)
                JJ.append(j)
            else:
                II.append(0)
                JJ.append(0)

    var_x = int(np.var(II))
    var_y = int(np.var(JJ))

    return var_x, var_y

img = cv2.imread('capture1.png')
#img = cv2.resize(img, dsize=(224, 224))
#cv2.imshow('img', img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#cv2.imshow('gray', gray)

ret, bin = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)
yy, xx = bin.shape
print(yy, xx)
ss_x = [];ss_y = []

for x in range(xx):
    ss_x.append(sum(bin[:, x]))   

for y in range(yy):
    ss_y.append(sum(bin[y,:]))

#
#res = bin[274:860 , 226:810]
#cv2.imshow('res', res)
#cv2.waitKey()

#plt.subplot(121)
plt.plot(ss_x)
#plt.subplot(122)
plt.plot(ss_y)
plt.show()




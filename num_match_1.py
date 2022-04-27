# https://g0pher.tistory.com/104

import pandas as pd
import cv2
import matplotlib.pyplot as plt
import glob
import numpy as np
import math
import time
import seaborn as sb


categ = ['1','2','3','4','5','6','7','8','9']
test_list = ['test_1.jpg', 'test_2.jpg', 'test_3.jpg', 'test_4.jpg', 'test_5.jpg']

for test in test_list:
    test_img = cv2.imread(test)

for folder in categ:
    path = './' + folder + '/*.jpg'
    cre_list = glob.glob(path)
    for cre in cre_list:
        cre_img = cv2.imread(cre)
        src = cre_img[30:200, 30:200].copy()
        
        src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
        ret, thr = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)

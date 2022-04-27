# https://g0pher.tistory.com/104

import pandas as pd
import cv2
import matplotlib.pyplot as plt
import glob
import numpy as np
import math
import time, os

def filter(thr):
    w, h = thr.shape
    filter_step = []
    for i in range(1, w-1):
        for j in range(1, h-1):
            cou_zero = sum(sum(thr[i-1:i+2,j-1:j+2] < 127))
            if cou_zero > 0:
                filter_step.append(cou_zero)
    
    num_cou = []
    for i in range(10):
        num_cou.append(filter_step.count(i))

    return num_cou


categ = ['1','2','3','4','5','6','7','8','9']
df = pd.DataFrame()
num_cre_table = []

for folder in categ:
    path = './' + folder + '/*.jpg'
    file_list = glob.glob(path)
    
    res = []
    
    for file in file_list:
        img = cv2.imread(file)
        src = img[30:200, 30:200].copy()
        
        src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
        ret, thr = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
        
        num_cou = filter(thr)

        y = []

        for i in range(1, len(num_cou)-1):
            #y.append(num_cou[i]/num_cou[len(num_cou)-1])
            y.append(num_cou[i])

        res.append(y)
    #print(folder, len(y))
    #rr = np.array(res)
    #print(res, type(res))
    
    for j in range(8):
        rr = []
        for i in range(len(res)):
            rr.append(res[i][j:j+1])
        #print(folder, j, np.min(np.array(rr)), np.max(np.array(rr)))
        num_cre_table.append([folder, j, np.min(np.array(rr)), np.max(np.array(rr))])
    
    os.system('cls')
    for out in num_cre_table:
        print(out)
    #time.sleep(10)
    print('-------------------------------')
# https://g0pher.tistory.com/104

import pandas as pd
import cv2
import matplotlib.pyplot as plt
import glob
import numpy as np
import math
import time

def filter(thr):
    w, h = thr.shape
    filter_step = []
    #i_generator = (i for i in range(1, w-1))
    #j_generator = (j for j in range(1, h-1))
    for i in range(1, w-1):
    #for i in i_generator:
       for j in range(1, h-1):
    #    for j in j_generator:
            cou_zero = sum(sum(thr[i-1:i+2,j-1:j+2] < 127))
            if cou_zero > 0:
                filter_step.append(cou_zero)
    
    num_cou = []
    for i in range(10):
        num_cou.append(filter_step.count(i))

    return num_cou


categ = ['1','2','3','4','5','6','7','8','9']
ss_p = []

df = pd.DataFrame(columns=['num','1','2','3','4','5','6','7','8'])
colors = ['#8A360F','#00FFFF','#E3CF57','#0000FF','#9C661F','#FF4040','#8B2323','#7FFF00','#6495ED','#B23AEE']
cc = 0
for folder in categ:
    path = './' + folder + '/*.jpg'
    file_list = glob.glob(path)
    cc_a = [];cc_b=[];cc_c=[];cc_d=[];cc_e=[]
    ss_c = []
    for file in file_list:
        img = cv2.imread(file)
        src = img[30:200, 30:200].copy()
        
        src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
        ret, thr = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
        
        num_cou = filter(thr)

        y = []
        y.append(folder)
        for i in range(1, len(num_cou)-1):
            y.append(num_cou[i]/num_cou[len(num_cou)-1])

        #plt.plot(x, y, color = colors[cc])
        #plt.pause(0.1)
        cv2.imshow('training', thr)
        cv2.waitKey(100)
        print(y)

        df.loc[cc] = y
        cc += 1
        #print(cc)
#time.sleep(10)
#print(df.head)

cre_table = []
for j in range(1, 10):
    for filt in range(1, 9):
        res = []
        for i in range(cc):
            if df['num'].values[i] == str(j):
                #print(df.values[i][filt:filt+1])
                res = np.append(res, df.values[i][filt:filt+1])
        #print(' num : ', str(j), ' filter : ', str(filt), ' 최소 : ',np.min(res), ' 최대 : ',np.max(res))
        #print(str(j),str(filt),np.min(res),np.max(res))
        #cre_table.append([str(j),str(filt),np.min(res),np.max(res)])
        cre_table = np.append(cre_table, [str(j),str(filt),np.min(res),np.max(res)])
        #print(df.head)
print(cre_table)
print(cre_table.size)

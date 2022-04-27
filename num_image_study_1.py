# https://g0pher.tistory.com/104

import pandas as pd
import cv2
import matplotlib.pyplot as plt
import glob
import numpy as np
import math
import time

def cre_thr(thr):
    cou_a = 0;cou_b=0;cou_c=0;cou_d=0;cou_e=0
    w, h = thr.shape
    for i in range(1, w-1, 3):
        for j in range(1, h-1, 3): 
            a = np.std([thr[j-1, i], thr[j, i], thr[j+1, i]]) #중간 세로
            b = np.std([thr[j, i-1], thr[j, i], thr[j, i+1]]) #중간 가로
            c = np.std([thr[j-1, i-1], thr[j, i], thr[j+1, i+1]]) #좌측 대각
            d = np.std([thr[j-1, i+1], thr[j, i], thr[j+1, i-1]]) #우측 대각
            #print(a, b, c, d)
            
            if a > 0:
                cou_a += 1
            if b > 0:
                cou_b += 1
            if c > 0:
                cou_c += 1
            if d > 0:
                cou_d += 1

    return cou_a, cou_b, cou_c, cou_d

def num_cre_table(cate):
    cou = 0;cre_table = []
    print('training on ... ...')
    for folder in cate:
        path = './' + folder + '/*.jpg'
        file_list = glob.glob(path)
        cc_a = [];cc_b=[];cc_c=[];cc_d=[];cc_e=[]
        for file in file_list:
            img = cv2.imread(file)
            src = img[30:200, 30:200].copy()
            src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
            ret, thr = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
            cou_a, cou_b, cou_c, cou_d = cre_thr(thr)
            cc_a.append(cou_a);cc_b.append(cou_b);cc_c.append(cou_c);cc_d.append(cou_d)
            #cv2.imshow('src_gray', src_gray)
            cv2.imshow('training', thr)
            cv2.waitKey(1)

        cre_table.append([np.min(cc_a), np.max(cc_a),
                    np.min(cc_b), np.max(cc_b),
                    np.min(cc_c), np.max(cc_c),
                    np.min(cc_d), np.max(cc_d)])
    return cre_table


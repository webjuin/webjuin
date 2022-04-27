# https://g0pher.tistory.com/104

import pandas as pd
import cv2
import matplotlib.pyplot as plt
import glob, os
import numpy as np
import math
import time
import mouse
import pyautogui


def test_filter(thr):
    w, h = thr.shape
    filter_step = []
    fil = [[1,0,0],[0,1,0],[0,0,1]]
    for i in range(1, w-1):
        for j in range(1, h-1):
            cou_zero = sum(sum(thr[i-1:i+2,j-1:j+2]*fil < 127))
            if cou_zero > 0:
                filter_step.append(cou_zero)
    
    num_cou = []
    for i in range(10):
        num_cou.append(filter_step.count(i))
    
    print(num_cou)
        
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

#print(res_cre[0][0], res_cre[0][1])
def res_cre():
    res = []
    categ = ['1','2','3','4','5','6','7','8','9']
    df = pd.DataFrame()
    ff = 1
    for folder in categ:
        path = './' + folder + '/*.jpg'
        file_list = glob.glob(path)
        
        kk1 = [];kk2=[];kk3=[];kk4=[];kk5=[];kk6=[];kk7=[]
        
        for file in file_list:
            img = cv2.imread(file)
            src = img[30:200, 30:200].copy()
            
            src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
            ret, thr = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
            
            num_cou = np.array(filter(thr))
            test_filter(thr)
            
            k1 = num_cou[1:2]/sum(num_cou[1:9])
            k2 = num_cou[2:3]/sum(num_cou[1:9])
            k3 = num_cou[3:4]/sum(num_cou[1:9])
            k4 = num_cou[4:5]/sum(num_cou[1:9])
            k5 = num_cou[5:6]/sum(num_cou[1:9])
            k6 = num_cou[6:7]/sum(num_cou[1:9])
            k7 = num_cou[7:8]/sum(num_cou[1:9])

            cv2.imshow('thr', thr)
            cv2.waitKey(100)
            kk1.append(k1);kk2.append(k2);kk3.append(k3);kk4.append(k4);kk5.append(k5);kk6.append(k6);kk7.append(k7)
            
        res.append([ff, np.min(kk1), np.max(kk1),
                    np.min(kk2), np.max(kk2),
                    np.min(kk3), np.max(kk3),
                    np.min(kk4), np.max(kk4),
                    np.min(kk5), np.max(kk5),
                    np.min(kk6), np.max(kk6),
                    np.min(kk7), np.max(kk7)])
        ff += 1
    return res

if __name__ == '__main__':
    table = res_cre()
    print(table)
    categ = ['1','2','3','4','5','6','7','8','9']
    df = pd.DataFrame()
    ff = 1
    for folder in categ:
        path = './' + folder + '/*.jpg'
        file_list = glob.glob(path)
        kk1 = [];kk3 = []; kk5 = [];kk7=[]
        for file in file_list:
            img = cv2.imread(file)
            src = img[30:200, 30:200].copy()
            
            src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
            ret, thr = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
            
            num_cou = np.array(filter(thr))
            
            k1 = num_cou[1:2]/sum(num_cou[1:9])
            k2 = num_cou[2:3]/sum(num_cou[1:9])
            k3 = num_cou[3:4]/sum(num_cou[1:9])
            k4 = num_cou[4:5]/sum(num_cou[1:9])
            k5 = num_cou[5:6]/sum(num_cou[1:9])
            k6 = num_cou[6:7]/sum(num_cou[1:9])
            k7 = num_cou[7:8]/sum(num_cou[1:9])

            ff = 0
            for i in range(0, 8):
                if table[i][1] <= k1 <= table[i][2]:
                    if table[i][3] <= k2 <= table[i][4]:
                        if table[i][5] <= k3 <= table[i][6]:
                            if table[i][7] <= k4 <= table[i][8]:
                                if table[i][9] <= k5 <= table[i][10]:
                                    if table[i][11] <= k6 <= table[i][12]:
                                        if table[i][13] <= k7 <= table[i][14]:
                                            ff = table[i][0]
                            #print(ff)
            os.system('cls')
            if ff:
                print(ff)
            
            #print(ff, k1, k3, k5, k7)
            
            #for i in range(1, 9):
            #    plt.subplot(2,4,i)
            #    plt.plot(num_cou[i:i+1]/sum(num_cou[1:9]), 'bo')
            #    plt.title('filter '+str(i))
            #plt.pause(1)
            cv2.imshow('thr', thr)
            cv2.waitKey(1000)
        ff += 1
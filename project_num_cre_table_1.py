import pandas as pd
import cv2
import matplotlib.pyplot as plt
import glob
import numpy as np
import os
import time

def mean_pos(binary):
    r, c = binary.shape
    II = []; JJ=[]
    for i in range(r):
        for j in range(c):
            if binary[i, j] > 0:
                II.append(i)
                JJ.append(j)

    mean_x = int(np.mean(II))
    mean_y = int(np.mean(JJ))

    return mean_x, mean_y

def var_pos(binary):
    r, c = binary.shape
    II = []; JJ=[]
    for i in range(r):
        for j in range(c):
            if binary[i, j] > 0:
                II.append(i)
                JJ.append(j)

    var_x = int(np.var(II))
    var_y = int(np.var(JJ))

    return var_x, var_y


categ = ['1','2','3','4','5','6','7','8','9']
index = ['num', 'min_X_A', 'max_X_A', 'min_Y_A', 'max_Y_A', 'min_X_B', 'max_X_B', 'min_Y_B', 'max_Y_B']
df = pd.DataFrame(columns=index)
print('making cretical table ... ...')

for folder in categ:
    #path = 'C:/Users/webju/OneDrive/python/SUDOKU_NUM/' + folder + '/*.jpg'
    path = 'C:/Users/Administrator/OneDrive/python/SUDOKU_NUM/' + folder + '/*.jpg'
    file_list = glob.glob(path)
    X_A = [];Y_A = []
    X_B = [];Y_B = []
    
    for file in file_list:
        img = cv2.imread(file)
        src = img[20:200, 20:200].copy()
        #src = img.copy()
        src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
        ret, thr = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
        dst = cv2.Canny(thr, 127, 255)
        mean_x, mean_y = mean_pos(dst)
                
        A = dst[:mean_x,:];B = dst[mean_x:,:]

        var_x_A, var_y_A = var_pos(A)
        var_x_B, var_y_B = var_pos(B)

        X_A.append(var_x_A);Y_A.append(var_y_A)
        X_B.append(var_x_B);Y_B.append(var_y_B)

        #cv2.imshow('dst', dst)
        #cv2.waitKey(1)
    
    data = [(folder, min(X_A), max(X_A), min(Y_A), max(Y_A), min(X_B), max(X_B),
            min(Y_B), max(Y_B))]
    data = pd.DataFrame(data, columns=index)
    df = pd.concat([df, data])

print(df)
df.to_pickle('cretical_table.pkl')
        

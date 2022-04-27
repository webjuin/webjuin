# https://sudoku.com/evil/
# 메인 프로그램

import pandas as pd
import mouse
import pyautogui as pag
from PIL import ImageGrab
import cv2
import matplotlib.pyplot as plt
import time
import keyboard
import numpy as np
from datetime import datetime
import project_num_cre_table_1


def cre_table(dst, var_x_A, var_y_A, var_x_B, var_y_B):
    table = pd.read_pickle('cretical_table.pkl')
    k = 40 # window margin
    L1_min = table['min_X_A'] <= var_x_A+k
    L1_max = table['max_X_A'] >= var_x_A-k

    L2_min = table['min_Y_A'] <= var_y_A+k
    L2_max = table['max_Y_A'] >= var_y_A-k

    L3_min = table['min_X_B'] <= var_x_B+k
    L3_max = table['max_X_B'] >= var_x_B-k

    L4_min = table['min_Y_B'] <= var_y_B+k
    L4_max = table['max_Y_B'] >= var_y_B-k


    LL = L1_min & L1_max & L2_min & L2_max & L3_min & L3_max & L4_min & L4_max
    
    
    re = np.array(table['num'][LL]).tolist()
    
    #print(re)

    try:
        num_re = re[0]
        #print(num_re)
        return num_re
    except:
        now = datetime.now()
        file_name = 'D:/' + now.strftime('%Y-%m-%d-%H-%M-%S') + '.jpg'
        cv2.imwrite(file_name, dst)
        project_num_cre_table_1
        pass



def empty_filter(thr):
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

#class auto_sudoku():
def read_image_num():
    print('ready to read ... ... ')
    p_cou = 0
    X = [];Y = []
    while True:
        #if mouse.is_pressed('right'):
        if keyboard.read_key() == 'p':
            y, x = pag.position()
            X.append(x)
            Y.append(y)
            time.sleep(0.3)
            p_cou += 1
        if p_cou == 2:
            im1 = pag.screenshot()
            path = r'./capture1.png'
            pag.screenshot(path)
            break
    img = cv2.imread('capture1.png', cv2.IMREAD_COLOR)
    #x1 = 276;x2 = 860;y1 = 228;y2 = 812
    # 562 542
    x1 = X[0];x2 = X[1]
    y1 = Y[0];y2 = Y[1]
    
    x1 = 562 - 288;y1 = 542 - 246
    x2 = 562 + 242;y2 = 542 + 286
    
    #print(x1, y1)
    #print(x2, y2)
    
    step = int((x2-x1)/9)
    img = img[x1:x2, y1:y2, :]

    cv2.imshow('img', img)

    w, h, _= img.shape
    r = w/9;c = h/9
    y = [];res = []

    x_b = 0;y_b = 0
    cou = 0
    puzzle_table = []
    for i in range(1, 10):
        a = int((i-1)*c)
        for j in range(1, 10):
            b = int((j-1)*r)
            grid = img[a:a+step, b:b+step, :]
            grid = cv2.resize(grid, dsize=(220, 220), interpolation=cv2.INTER_AREA)
            grid = grid[20:200, 20:200, :]
            grid_gray = cv2.cvtColor(grid, cv2.COLOR_BGR2GRAY)
            ret, thr = cv2.threshold(grid_gray, 127, 255, cv2.THRESH_BINARY)        
            num_cou = empty_filter(thr)
            if len(num_cou) > 1 and num_cou[1] > 4:
                y = []
                for i in range(1, len(num_cou)-1):
                    y.append(num_cou[i])
                res.append(y)
                dst = cv2.Canny(thr, 127, 255)
                mean_x, mean_y = mean_pos(dst)
                
                A = dst[:mean_x,:];B = dst[mean_x:,:]

                var_x_A, var_y_A = var_pos(A)
                var_x_B, var_y_B = var_pos(B)

                #print(var_x_A, var_y_A, var_x_B, var_y_B)
                num_image = cre_table(dst, var_x_A, var_y_A, var_x_B, var_y_B)

                puzzle_table.append(str(num_image))
                cv2.imshow('dst', dst)
                cv2.waitKey(1)
            else:
                #pag.moveTo(165+b, 338+a)
                #pag.click()
                #sudoku_click_1to9_1.main(cou)
                #print(0)
                puzzle_table.append(str(0))
                time.sleep(0.001)
                cou += 1

    puzzle_table = np.array(puzzle_table).reshape((9, 9))

    return puzzle_table

if __name__ == "__main__":
    puzzle_table = read_image_num()
    print(puzzle_table)

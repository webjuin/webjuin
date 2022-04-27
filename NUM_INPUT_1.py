# https://g0pher.tistory.com/104

import pandas as pd
import cv2
import matplotlib.pyplot as plt
import glob
import numpy as np
import math
import time
import mouse
import pyautogui


grid = (['0', '0', '0', '0', '2', '0', '0', '0', '6'],
        ['5', '0', '0', '0', '3', '0', '0', '0', '0'],
        ['0', '0', '9', '5', '0', '6', '1', '0', '0'],
        ['0', '0', '0', '0', '5', '0', '0', '0', '0'],
        ['9', '0', '0', '4', '0', '7', '0', '0', '3'],
        ['0', '0', '1', '0', '0', '0', '0', '8', '0'],
        ['4', '0', '0', '6', '0', '9', '0', '0', '7'],
        ['0', '0', '0', '0', '0', '2', '0', '0', '0'],
        ['0', '7', '0', '0', '0', '0', '3', '0', '0'])

def memo_3x3(r, c):
        if grid[r][c] == '0':
                rr = r//3;cc = c//3
                #print(r, c, rr, cc)
                gg = []
                for r_i in range(rr*3, rr*3+3):
                        for c_i in range(cc*3, cc*3+3):
                                gg.append(grid[r_i][c_i])
                                
                while '0' in gg:
                        gg.remove('0')
        return gg              
        
def memo_num(grid):
        res = []
        nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        for r in range(0, 9):
                for c in range(0, 9):
                        cc = []
                        if grid[r][c] == '0':
                                for i in range(0, 9):
                                        cc.append(grid[r][i])
                                for j in range(0, 9):
                                        cc.append(grid[j][c])
                                
                                while '0' in cc:
                                        cc.remove('0')

                                nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
                                for i in cc:
                                        while i in nums:
                                                nums.remove(i)
                                gg = memo_3x3(r, c)
                                for i in gg:
                                        while i in nums:
                                                nums.remove(i)
                                res.append(nums)
        return res      

#if __name__ == '__main__':
def memo_type(cou):        
        ss = memo_num(grid)
        pp = ss[cou]
        #print(pp, len(pp))
        pyautogui.typewrite(pp)

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


def cap_and_num():
    categ = ['1','2','3','4','5','6','7','8','9']
    df = pd.DataFrame()

    for folder in categ:
        path = './' + folder + '/*.jpg'
        file_list = glob.glob(path)
        
        for file in file_list:
            img = cv2.imread(file)
            src = img[30:200, 30:200].copy()
            
            src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
            ret, thr = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
            
            num_cou = filter(thr)

            y = []
            for i in range(1, len(num_cou)-1):
                y.append(num_cou[i]/num_cou[len(num_cou)-1])

            print(folder, len(y))
            print(y)
            print('-------------------------------')

if __name__ == '__main__':
    while True:
        if mouse.is_pressed('right'):
            im1 = pyautogui.screenshot()
            path = r'./capture1.png'
            pyautogui.screenshot(path)
            break
        
    img = cv2.imread('capture1.png', cv2.IMREAD_COLOR)

    #x1 = 276;x2 = 860;y1 = 228;y2 = 812
    x1 = 302;x2 = 964;y1 = 130;y2 = 794

    step = int((x2-x1)/9)
    img = img[x1:x2, y1:y2, :]

    cv2.imshow('img', img)
    w, h, _= img.shape
    r = w/9; c = h/9
    y = []
    res = []
    x_b = 0;y_b = 0
    cou = 0

    for i in range(1, 10):
        a = int((i-1)*c)
        for j in range(1, 10):
            b = int((j-1)*r)
            grid = img[a:a+step, b:b+step, :]
            grid_gray = cv2.cvtColor(grid, cv2.COLOR_BGR2GRAY)
            ret, thr = cv2.threshold(grid_gray, 127, 255, cv2.THRESH_BINARY)        
            num_cou = filter(thr)

            if len(num_cou) > 1 and num_cou[1] > 4:
                y = []
                for i in range(1, len(num_cou)-1):
                    y.append(num_cou[i])
                res.append(y)
                cv2.imshow('thr', thr)
                cv2.waitKey(1000)
            else:
                pyautogui.moveTo(165+b, 338+a)
                pyautogui.click()
                memo_type(cou)
                time.sleep(0.001)
                cou += 1
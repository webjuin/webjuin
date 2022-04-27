# https://sudoku.com/ko/evil/
# 메인 프로그램

import pandas as pd
import mouse
import pyautogui as pag
from PIL import ImageGrab
import cv2
import num_cre_table_1
import matplotlib.pyplot as plt
import time
import sudoku_click_1to9_1

while True:
    if mouse.is_pressed('right'):
        im1 = pag.screenshot()
        path = r'./capture1.png'
        pag.screenshot(path)
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
        num_cou = num_cre_table_1.filter(thr)
        if len(num_cou) > 1 and num_cou[1] > 4:
            y = []
            for i in range(1, len(num_cou)-1):
                y.append(num_cou[i])
            res.append(y)
            cv2.imshow('thr', thr)
            cv2.waitKey(1000)
        else:
            #pag.moveTo(165+b, 338+a)
            #pag.click()
            #sudoku_click_1to9_1.main(cou)
            time.sleep(0.001)
            cou += 1w
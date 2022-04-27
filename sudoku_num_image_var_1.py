# https://sudoku.com/evil/
# 메인 프로그램

from datetime import datetime
import pandas as pd
import mouse
import pyautogui as pag
import cv2
import num_cre_table_1
import matplotlib.pyplot as plt
import time
import keyboard
import numpy as np


def num_image_var():
    print('ready to capture ... ... ')
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

    x1 = X[0];x2 = X[1]
    y1 = Y[0];y2 = Y[1]
    

    step = int((x2-x1)/9)
    img = img[x1:x2, y1:y2, :]

    cv2.imshow('img', img)

    w, h, _= img.shape
    r = w/9;c = h/9
    y = [];res = []

    x_b = 0;y_b = 0
    cou = 0

    for i in range(1, 10):
        a = int((i-1)*c)
        for j in range(1, 10):
            b = int((j-1)*r)
            grid = img[a:a+step, b:b+step, :]
            grid = cv2.resize(grid, dsize=(220, 220), interpolation=cv2.INTER_AREA)
            grid = grid[20:200, 20:200, :]
            grid_gray = cv2.cvtColor(grid, cv2.COLOR_BGR2GRAY)
            ret, thr = cv2.threshold(grid_gray, 127, 255, cv2.THRESH_BINARY)        
            num_cou = num_cre_table_1.filter(thr)
            if len(num_cou) > 1 and num_cou[1] > 4:
                y = []
                for i in range(1, len(num_cou)-1):
                    y.append(num_cou[i])
                res.append(y)
                dst = cv2.Canny(grid_gray, 50, 250)
                now = datetime.now()
                file_name = 'D:/python_work/SUDOKU/' + now.strftime('%Y-%m-%d-%H-%M-%S') + '.jpg'
                cv2.imwrite(file_name, dst)
                print(file_name)
                cv2.imshow('dst', dst)
                cv2.waitKey(1000)
            else:

                time.sleep(0.001)
                cou += 1

if __name__ == "__main__":
    num_image_var()
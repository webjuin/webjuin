# https://sudoku.com/evil/
# 메인 프로그램

from datetime import datetime
import pandas as pd
import mouse
import pyautogui as pag
import cv2
import matplotlib.pyplot as plt
import time
import keyboard
import numpy as np


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

def capture_num():
    print('ready to capture ... ... ')
    p_cou = 0
    X = [];Y = []
    while True:
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
            num_cou = empty_filter(thr)
            if len(num_cou) > 1 and num_cou[1] > 4:
                y = []
                for i in range(1, len(num_cou)-1):
                    y.append(num_cou[i])
                res.append(y)
                #dst = cv2.Canny(grid_gray, 127, 255)
                dst = cv2.Canny(thr, 127, 255)
                now = datetime.now()
                file_name = 'D:/' + now.strftime('%Y-%m-%d-%H-%M-%S') + '.jpg'
                cv2.imwrite(file_name, dst)
                print(file_name)
                cv2.imshow('dst', dst)
                cv2.imshow('thr', thr)
                cv2.waitKey(10)
            else:

                time.sleep(0.001)
                cou += 1

if __name__ == "__main__":
    capture_num()
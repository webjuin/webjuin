# https://sudoku.com/ko/evil/

import pandas as pd
import keyboard
import pyautogui as pag
from PIL import ImageGrab
import cv2
import numpy as np
import time
import mouse

grid = (['0', '0', '0', '0', '2', '0', '0', '0', '6'],
        ['5', '0', '0', '0', '3', '0', '0', '0', '0'],
        ['0', '0', '9', '5', '0', '6', '1', '0', '0'],
        ['0', '0', '0', '0', '5', '0', '0', '0', '0'],
        ['9', '0', '0', '4', '0', '7', '0', '0', '3'],
        ['0', '0', '1', '0', '0', '0', '0', '8', '0'],
        ['4', '0', '0', '6', '0', '9', '0', '0', '7'],
        ['0', '0', '0', '0', '0', '2', '0', '0', '0'],
        ['0', '7', '0', '0', '0', '0', '3', '0', '0'])

def dd_gg(r, c):
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
        
def dd_num(grid):
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
                                gg = dd_gg(r, c)
                                for i in gg:
                                        while i in nums:
                                                nums.remove(i)
                                res.append(nums)
        return res      

#if __name__ == '__main__':
def main(cou):        
        ss = dd_num(grid)
        pp = ss[cou]
        #print(pp, len(pp))
        pag.typewrite(pp)
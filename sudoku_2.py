# https://m.blog.naver.com/ydot/221650775739

import pandas as pd


backtracks = 0

def printSudoku(grid):
    numrow = 0
    for row in grid:
        if numrow % 3 == 0 and numrow != 0:
            print(' ')
        print(row[0:3],' ',row[3:6],' ',row[6:9])
        numrow += 1
        

def isValid(grid, i, j, e):
    rowOk = all([e != grid[i][x] for x in range(9)])
    if rowOk:
        columnOk = all([e != grid[x][j] for x in range(9)])
        if columnOk:
            secTopX, secTopY = 3*(i//3), 3*(j//3)
            for x in range(secTopX, secTopY+3):
                for y in range(secTopX, secTopY+3):
                    if grid[x][y] == e:
                        return False
            return True
    return False

def findNextCellToFill(grid):
    for x in range(0, 9):
        for y in range(0, 9):
            if grid[x][y] == 0:
                return x, y
    return -1, -1

def solveSudoku(grid, i=0, j=0):
    global backtracks
    i, j = findNextCellToFill(grid)
    if i == -1:
        return True
    for e in range(1, 10):
        if isValid(grid, i, j, e):
            grid[i][j] = e
            
            if solveSudoku(grid, i, j):
                return True
            
            backtracks += 1
    grid[i][j] = 0
    return False


input =[[8,0,0,0,0,0,0,1,2],
        [0,0,0,0,6,0,0,0,0],
        [0,0,0,0,3,5,0,0,0],
        [0,1,7,0,0,0,0,6,0],
        [4,0,0,7,8,0,0,9,0],
        [0,0,0,0,0,9,0,4,0],
        [0,0,6,0,4,0,0,0,0],
        [0,0,0,0,2,0,0,0,9],
        [0,0,3,1,0,0,5,0,0]]

solveSudoku(input)
printSudoku(input)
    
    
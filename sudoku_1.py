# https://g0pher.tistory.com/104

import pandas as pd

game = [[8,0,0,0,0,0,0,1,2],
        [0,0,0,0,6,0,0,0,0],
        [0,0,0,0,3,5,0,0,0],
        [0,1,7,0,0,0,0,6,0],
        [4,0,0,7,8,0,0,9,0],
        [0,0,0,0,0,9,0,4,0],
        [0,0,6,0,4,0,0,0,0],
        [0,0,0,0,2,0,0,0,9],
        [0,0,3,1,0,0,5,0,0]]

tmp = [[] for i in range(81)]

def startTree(count):
    if count%50 == 0:
        print('|',end='')
    if count == 81:
        return 7
    y0 = count//9
    x0 = count%9
    findPossibility(x0, y0)

    tt = 1
    while True:
        if tt == 7:
            return 7
        elif tt == 0:
            if tmp[count-1]!=[0]:
                game[(count-1)//9][(count-1)%9]=0
                return 1
            else:
                return 0

        if tmp[count]==[]:
            tt=0
            continue
        elif tmp[count] !=[0]:
            game[y0][x0]=tmp[count][0]
            del tmp[count][0]
        tt = startTree(count+1)
        if tmp[count] == [0] and tt!=7:
            tt=0

def findBase(locate):#기본 사각형 위치 초기화
    if locate<=2:
        return 0
    elif locate>2 and locate<=5:
        return 3
    else:
        return 6

def findPossibility(x1,y1):#해당좌표 가능성 검사
    yTmp=findBase(y1)
    xTmp=findBase(x1)
    tmp[y1*9+x1] = []

    if game[y1][x1] != 0:
        tmp[y1*9+x1] = [0]
        return

    for target in range(1,10):
        for find in range(9):
            if target == game[find][x1]:#세로검사
                find=10
            if find==0 or find==1 or find==2:#네모칸 검사
                if target in game[yTmp+find][xTmp:xTmp+2]:
                    find=10
            if find==10:
                break
        if target in game[y1] or find==10:#가로검사
            continue
        else:
            tmp[y1*9+x1].append(target)


for i in game:
    print(i)
print('')
print('Going ', end=' ')

startTree(0)
print('|')
print('')

for i in game:
    print(i)
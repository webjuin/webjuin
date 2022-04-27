# https://g0pher.tistory.com/104

import cv2
import numpy as np

x = [58, 110, 2, 110, 110, 110, 170, 224, 170, 224, 224, 224, 224, 224, 224, 280, 280, 280,
     280, 280,   2,   2, 334, 334, 334, 334, 334, 334, 385, 392, 392, 392, 392, 448,
     448, 448, 448, 448, 448, 497, 58, 58, 58, 58, 2, 94]
y = [62, 8, 8, 492, 114, 276,   8,   8, 443, 492,  62, 276, 332, 224, 332, 225, 276,  62,
       8, 438, 224, 385,  62, 224, 492, 276, 438, 62, 492, 114, 170, 276, 276, 170,
       224, 332, 62, 62, 332, 224, 62, 224, 438, 276, 62, 438, 170]
#(168, 8), (171, 443), (2, 7), (217, 493), (219, 62),\8
#        (221, 8), (224, 277), (225, 332), (227, 225), (277, 331), (279, 225), (280, 276), (280, 61),\
#        (283, 7), (285, 436), (3, 228), (3, 385), (332, 59), (336, 224), (336, 492), (337, 278),\
#        (339, 439), (339, 60), (385, 492), (392, 114), (394, 171), (395, 280), (399, 282), (445, 171),\
#        (446, 220), (447, 333), (450, 58), (450, 58), (452, 334), (497, 221), (53, 61), (58, 228),\
#        (58, 442), (59, 279), (59, 62), (64, 442), (94, 171)]

dir_del = None
clicked_points = []
clone = None

def MouseLeftClick(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        clicked_points.append((y, x))

		# 원본 파일을 가져 와서 clicked_points에 있는 점들을 그린다.
        #dstgray = clone.copy()
        for point in clicked_points:
            cv2.circle(dstgray, (point[1], point[0]), 2, (0, 255), thickness = -1)
            print(point)
        cv2.imshow('dstgray', dstgray)



cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_AUTOFOCUS, 1)
data = []
while cap.isOpened():
    ret, img = cap.read()
    img = cv2.fastNlMeansDenoisingColored(img, None, 5, 5, 7, 21)
    rows, cols, ch = img.shape

    a = [[188,162],[488,142],[190,458],[516,448]]
    b = [[0, 0],[1000, 0],[0,1000],[1000,1000]] # 왼쪽위점, 오른쪽위점, 왼쪽아래점, 오른쪽아래점 

    pts1 = np.float32(a)
    pts2 = np.float32(b)
    img = cv2.circle(img, (a[0][0], a[0][1]), 3, (0,0,255),-1) 
    img = cv2.circle(img, (a[1][0], a[1][1]), 3, (0,0,255),-1) 
    img = cv2.circle(img, (a[2][0], a[2][1]), 3, (0,0,255),-1) 
    img = cv2.circle(img, (a[3][0], a[3][1]), 3, (0,0,255),-1) #cv2.circle(img, c, 5, (55, 255, 55), -1) 
    M = cv2.getPerspectiveTransform(pts1, pts2) 
    dst = cv2.warpPerspective(img, M, (1000, 1000)) # 변환후 크기 (x좌표, y좌표) 
    dst = cv2.resize(dst, dsize=(500, 500))

    dstgray = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)

    #cv2.imshow('img', img)
    #cv2.imshow('dst', dst)
    #cv2.namedWindow('dstgray')
    #cv2.setMouseCallback('dstgray', MouseLeftClick)
    for i in range(0, len(x)):
        dstgray[x[i]:x[i]+3, y[i]:y[i]+3] = 0
    cv2.imshow('dstgray', dstgray)

    cv2.waitKey(10)


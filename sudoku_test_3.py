# https://g0pher.tistory.com/104

import pandas as pd
import cv2
import matplotlib.pyplot as plt
import sudoku_num_image_cre_table_1

cate = ['1','2','3','4','5','6','7','8','9']
cre_table = sudoku_num_image_cre_table_1.out_table()
print(cre_table)

file_list = ['test_1.jpg', 'test_2.jpg', 'test_3.jpg', 'test_4.jpg', 'test_5.jpg']

res_1 = [];res_2 = []
for file in file_list:
    img = cv2.imread(file)
    img = img[266:948, 10:688, :]   
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    a, b = img_gray.shape

    for i in range(len(cate)):
        for j in range(len(cate)):
            A = img_gray[i*76:i*76+76, j*75:j*75+75]
            A = cv2.resize(A, dsize=(224, 224))
            A = A[30:200, 30:200].copy()
            ret, thr = cv2.threshold(A, 127, 255, cv2.THRESH_BINARY)
            num_cou = sudoku_num_image_cre_table_1.filter(thr)
            y = []
            if num_cou[1] > 1:
                for i in range(1, len(num_cou)-1):
                    y.append(num_cou[i])
                    #y.append(num_cou[i]/num_cou[len(num_cou)-1])
                
                print(len(cre_table), cre_table[64][2], cre_table[64][3])
                num_check = 0
                for i in range(0, 72):
                    r = int(i // 8);c = int(i / 8)
                    print(r, c)
                    if cre_table[c+r*8][2] <= y[r] <= cre_table[c+r*8][3]:
                        num_check = 1
                        out_num = cre_table[c+r*8][0]
                    else:
                        num_check = 0
                        break
                
                #print(cre_table[1][0])
                if num_check:
                    print(out_num)
            
                cv2.imshow('thr', thr)
                cv2.waitKey(3000)
            #else:
            #    cv2.imshow('Nothing', thr)
            #    cv2.waitKey(3000)
                
            cv2.destroyAllWindows()


                    
                    
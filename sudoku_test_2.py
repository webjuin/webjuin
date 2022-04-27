# https://g0pher.tistory.com/104

import pandas as pd
import cv2
import matplotlib.pyplot as plt
file_list = ['test_5.jpg'] #, 'test_2.jpg', 'test_3.jpg', 'test_4.jpg', 'test_5.jpg']
cre_1 = [[4710, 5370, 2100, 2472],
         [7870, 8350, 3170, 3387],
         [8170, 8590, 2950, 2973],
         [8540, 8660, 2310, 2706],
         [8720, 9240, 2750, 3549],
         [8920, 8940, 2470, 2480],
         [5770, 6160, 3070, 3390],
         [10310, 10740, 3300, 4180],
         [9090, 9290, 3050, 4000]]

print(cre_1[0][0])

res_1 = [];res_2 = []
for file in file_list:
    img = cv2.imread(file)
    img = img[266:948, 10:688, :]   
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    a, b = img_gray.shape
    print(a, b)
    for i in range(9):
            for j in range(9):
                    A = img[i*76:i*76+76, j*75:j*75+75]
                    A = cv2.resize(A, dsize=(224, 224))
                    ret, thr = cv2.threshold(A, 127, 255, cv2.THRESH_BINARY)
                    B = A.copy()
                    B[30:190, 50:180] = 0
                    ss_1 = sum(sum(sum(thr[30:190, 50:180] < 1)))
                    ss_2 = sum(sum(sum(thr[30:90, 50:180] < 1)))
                    
                    if ss_1 > 0:
                        res_1.append(ss_1)
                        for i in range(0, 9):
                            if (cre_1[i][0] <= ss_1 <= cre_1[i][1]) and (cre_1[i][2] <= ss_2 <= cre_1[i][3]):
                                print(str(i+1))
                                cv2.imshow(str(i+1), A)
                                cv2.imshow(str(i+1), B)
                                cv2.imshow(str(i+1), thr)
                                #cv2.imshow('1', img)
                                cv2.waitKey(5000)
                                cv2.destroyAllWindows()
                                
plt.plot(res_1,'b.')
plt.show()

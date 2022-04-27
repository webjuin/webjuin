# https://m.blog.naver.com/arin12349/221890866722

from PIL import Image
from PIL import ImageGrab
from pytesseract import *
import re
import cv2
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_AUTOFOCUS, 1)

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(img, lang='eng')
    print(text)

    cv2.imshow('img', img)
    cv2.waitKey(10)


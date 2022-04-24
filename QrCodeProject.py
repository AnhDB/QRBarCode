import cv2
import numpy as np
from pyzbar.pyzbar import decode

"""
Kiểm tra QRCode có hợp lệ không?
Nếu data có trong file data.txt --> hợp lệ. --> màu xanh
Nếu không có trong file --> ko hợp lệ --> màu đỏ
"""
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

with open('data.txt') as file:
    list = file.read().splitlines()

while True:
    success, img = cap.read()
    for barcode in decode(img):
        myData = barcode.data.decode('utf-8')
        print(myData)
        if myData in list:
            myOutput = 'Authorized'
            myColor = (0,255,0)
        else:
            myOutput = 'Un - Authorized'
            myColor = (0, 0, 255)
        pts = np.array([barcode.polygon], np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(img, [pts], True, myColor, 3)
        pts2 = barcode.rect
        cv2.putText(img, myOutput, (pts2[0],pts2[1]), cv2.FONT_HERSHEY_SIMPLEX, 1,  myColor, 2)

    cv2.imshow('Result', img)
    cv2.waitKey(1)


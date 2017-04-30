import time
import cv2

def take_picture():
    cam = cv2.VideoCapture(0)
    time.sleep(0.1)
    ret, img = cam.read()
    cv2.imwrite('recent.png', img)
    del(cam)
    return img
take_picture()

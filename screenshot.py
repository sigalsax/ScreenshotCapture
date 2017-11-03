'''
Records and captures 5 screenshots every second
'''
import pyscreenshot as ImageGrab
import time
import cv2 as cv
import numpy as np
import datetime

def takeScreenShot():
	for x in range(1,6):
		print('grabbing ', x , ' screenshot')
		img = ImageGrab.grab(bbox=(100,1,1715,925)) #x, y, w, h
		# array format to be used for imwrite
		img_np = np.array(img)
		# saves img
		cv.imwrite("screenshot"+str(x)+".JPG",img_np)
		time.sleep(1)

if __name__ == "__main__":
	takeScreenShot()

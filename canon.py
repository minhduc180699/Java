import cv2
import matplotlib.pyplot as plt
from scipy import ndimage
import numpy as np
img = cv2.imread('canon1.jpg')
#imgcrop = img[740:850,950:1430]
##imgcrop = ndimage.rotate(imgcrop,180)
##imgcrop2 = cv2.cvtColor(imgcrop,CV_RGB2GRAY);
image = cv2.cvtColor(img, cv2.COLOR_RGB2RGBA)
imgthumbnail = cv2.resize(image,(600,400))
cv2.imshow("ảnh",imgthumbnail)
k = cv2.waitKey(0)
if k ==ord('s'):
    cv2.imwrite("anhbgr.jpg",imgthumbnail)
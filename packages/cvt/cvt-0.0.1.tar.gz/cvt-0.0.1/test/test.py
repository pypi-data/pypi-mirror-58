import torch
import numpy as np 
import matplotlib.pyplot as plt
import cv2 as cv
img = cv.imread('test/assets/image.png')
mask = cv.imread('test/assets/mask.png')

data = {'image':img, 'mask':mask}

import cvt
tfms = cvt.from_file('example/json_cfg2.json')
data = tfms(data)
plt.imshow(data['image'])
plt.show()
plt.imshow(data['mask'])
plt.show()
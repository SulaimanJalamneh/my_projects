

import cv2
import numpy as np
from matplotlib import pyplot as plt
import datetime 

img=cv2.imread("img2.jpg")
print(img.shape)


cv2.waitKey(0)
cv2.destroyAllWindows()

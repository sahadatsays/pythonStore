import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('watch.jpg',cv2.IMREAD_GRAYSCALE)

#SHOW IMAGE
# cv2.imshow('image', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

plt.imshow(image, cmap='gray', interpolation='bicubic')
plt.show()
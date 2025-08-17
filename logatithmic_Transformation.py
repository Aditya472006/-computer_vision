import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE) 
c = 1
log_img = c * np.log(1 + img)

plt.subplot(1,2,1), plt.imshow(img, cmap='gray'), plt.title("Original")
plt.subplot(1,2,2), plt.imshow(log_img, cmap='gray'), plt.title("Log Transformation")
plt.show()


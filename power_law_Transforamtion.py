import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE) / 255.0
gamma = 2.5
gamma_img = np.power(img, gamma)

plt.subplot(1,2,1), plt.imshow(img, cmap='gray'), plt.title("Original")
plt.subplot(1,2,2), plt.imshow(gamma_img, cmap='gray'), plt.title(f"Gamma (γ={gamma})")
plt.show()

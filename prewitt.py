import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('whatsapp.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
img_gaussian = cv2.GaussianBlur(gray,(3,3),0)


kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
img_prewittx = cv2.filter2D(img_gaussian, -1, kernelx)

plt.subplot(1,2,1),plt.imshow(image)
plt.title('Original')
plt.subplot(1,2,2), plt.imshow(img_prewittx)
plt.title('Prewitt X')
plt.show()


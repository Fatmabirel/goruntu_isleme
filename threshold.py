import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('notes.jpg')


image_bw = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
_, threshold = cv2.threshold(image_bw,130,255,cv2.THRESH_BINARY)


plt.subplot(1,2,1),plt.imshow(image)
plt.title('Original')
plt.subplot(1,2,2), plt.imshow(threshold, cmap='gray')
plt.title('Threshold')
plt.show()



import cv2
import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt

roberts_cross_v = np.array([[1, 0],
                            [0, -1]])

roberts_cross_h = np.array([[0, 1],
                            [-1, 0]])

image = cv2.imread("deneme.jpg", 0).astype('float64')
image /= 255.0
vertical = ndimage.convolve(image, roberts_cross_v)
horizontal = ndimage.convolve(image, roberts_cross_h)

edged_img = np.sqrt(np.square(horizontal) + np.square(vertical))
edged_img *= 255

plt.subplot(1,2,1),plt.imshow(image)
plt.title('Orginal')
plt.subplot(1,2,2), plt.imshow(edged_img)
plt.title('Robert Cross')
plt.show()

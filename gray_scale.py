import cv2
import matplotlib.pyplot as plt


image = cv2.imread('whatsapp.png', 1)

gray_scale = cv2.imread('whatsapp.png', 0)

plt.subplot(1,2,1),plt.imshow(image)
plt.title('Orginal')
plt.subplot(1,2,2), plt.imshow(gray_scale, cmap='gray')
plt.title('Gamma')
plt.show()


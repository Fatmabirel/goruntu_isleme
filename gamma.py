import cv2
import numpy as np
import matplotlib.pyplot as plt


def gammaCorrection(src, gamma):
    invGamma = 1 / gamma

    table = [((i / 255) ** invGamma) * 255 for i in range(256)]
    table = np.array(table, np.uint8)

    return cv2.LUT(src, table)


img = cv2.imread('deneme.jpg')
gammaImg = gammaCorrection(img, 3)

plt.subplot(1,2,1),plt.imshow(img)
plt.title('Orginal')
plt.subplot(1,2,2), plt.imshow(gammaImg)
plt.title('Gamma')
plt.show()
import random
import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('dag.jpg', cv2.IMREAD_GRAYSCALE)
histogram, bin_edges = np.histogram(img, bins=256, range=(0, 1))
def add_noise(img):
    row, col = img.shape
    number_of_pixels = random.randint(300, 10000)
    for i in range(number_of_pixels):
        y_coord = random.randint(0, row - 1)
        x_coord = random.randint(0, col - 1)
        img[y_coord][x_coord] = 255
    number_of_pixels = random.randint(300, 10000)
    for i in range(number_of_pixels):
        y_coord = random.randint(0, row - 1)
        x_coord = random.randint(0, col - 1)
        img[y_coord][x_coord] = 0
    return img

image = add_noise(img)
plt.subplot(1,2,1),plt.imshow(img)
plt.title('Original')
plt.show()
plt.subplot(1,2,1),plt.imshow(image)
plt.title('Salt and Pepper')
plt.show()
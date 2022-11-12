import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read an image
image = cv2.imread('deneme.jpg')

# Apply log transformation method
c = 255 / (np.log(1 + 255))
log_image = c * (np.log(image + 1))

# Specify the data type so that
# float value will be converted to int
log_image = np.array(log_image, dtype=np.uint8)

# Display both images
plt.subplot(1,2,1),plt.imshow(image)
plt.title('Orginal')
plt.subplot(1,2,2),plt.imshow(log_image)
plt.title('Log')
plt.show()

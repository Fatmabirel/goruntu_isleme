import cv2
import matplotlib.pyplot as plt

image = cv2.imread('dag.jpg')
image= cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
colored_negative = abs(255-image)

plt.subplot(1,2,1),plt.imshow(image)
plt.title('Orginal')
plt.subplot(1,2,2), plt.imshow(colored_negative)
plt.title('Negative')
plt.show()

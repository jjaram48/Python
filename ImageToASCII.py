import cv2
import numpy as np

# Read the image
image = cv2.imread("Image1.jpg")

# Access pixel values
# For pixel at (x, y)
# x = 21  # Replace with your desired x coordinate
# y = 21   # Replace with your desired y coordinate

# pixel_value = image[y, x]
grayscale_image = np.mean(image, axis=2)

print(grayscale_image)

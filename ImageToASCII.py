import cv2
import numpy as np

# Read the image
image = cv2.imread("Image1.jpg")

# Load the array of ASCII
# densityArray = ['@', '#', '%', '8', '&', 'B', 'M', 'W', 'X', 'Z', 'o', 'a', 'h', 'k', 'b', 'd', 'p', 'q', 'w', 'm', '*', '+', '=', '~', '-', ':', '.', ',', ' ']
densityArray = np.array(list("@#%8&BMWXZohkbdpqwm*+=~-:.' \""))
# Discard last element " in the densistyArray
densityArray = densityArray[:-1]

# Access pixel values
# For pixel at (x, y)
# x = 21  # Replace with your desired x coordinate
# y = 21   # Replace with your desired y coordinate

# pixel_value = image[y, x]
grayscale_image = np.mean(image, axis=2)

# print(grayscale_image)
print(densityArray[28])


import cv2
import numpy as np
# import pprint

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
# grayscaleImage = np.mean(image, axis=2)

# Read the grayscale image
grayscaleImage = cv2.imread("Image1.jpg", cv2.IMREAD_GRAYSCALE)

# Normalize the grayscale image to the range [0, 28] (corresponding to the index in density_array)
scaledImage = np.interp(grayscaleImage, (0, 255), (0, len(densityArray) - 1))

# Convert the scaled grayscale values to integers (indices for density_array)
ascii_indices = scaledImage.astype(int)

# Map each grayscale value to its corresponding ASCII character
ascii_image = densityArray[ascii_indices]

# Join the ASCII characters row-wise to create the final ASCII art
ascii_art = "\n".join("".join(row) for row in ascii_image)

# print(grayscale_image)
# pprint(grayscaleImage)
# pprint.pprint(grayscaleImage, width=80)
with open("ascii_art.txt", "w") as f:
    f.write(ascii_art)

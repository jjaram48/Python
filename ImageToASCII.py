import cv2

# Read the image
image = cv2.imread("Image1.jpg")

# Access pixel values
# For pixel at (x, y)
x = 21  # Replace with your desired x coordinate
y = 21   # Replace with your desired y coordinate

pixel_value = image[y, x]

print(pixel_value)

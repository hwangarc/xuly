import cv2
import numpy as np
import os

# Prompt user to enter number to be added to the image
num = int(input("+ mấy :"))

# Load all images from the folder
images = []
for image_path in os.listdir("images"):
    image = cv2.imread(os.path.join("images", image_path))
    if image is not None:
        images.append(cv2.copyMakeBorder(cv2.resize(image, (446, 446)), 2, 2, 2, 2, cv2.BORDER_CONSTANT, None, value=[255, 255, 255]))

# Add border, text, Gaussian blur, and brightness reduction to the last image
font = cv2.FONT_HERSHEY_SIMPLEX
img5 = images[-1].copy()
cv2.putText(img5, '+'+str(num), (int((img5.shape[1] - cv2.getTextSize('+'+str(num), font, 2, 5)[0][0]) / 2), int((img5.shape[0] + cv2.getTextSize('+'+str(num), font, 2, 5)[0][1]) / 2)), font, 2, (255, 255, 255), 5, cv2.LINE_AA)
img5 = cv2.GaussianBlur(img5, (5, 5), 0)
img5 = cv2.addWeighted(img5, 1.0, img5, 0, -20)

# Create a black canvas and paste images on the canvas
canvas = np.zeros((900, 900, 3), dtype=np.uint8)
canvas[:450, :450] = cv2.resize(images[0], (450, 450))
canvas[:450, 450:] = cv2.resize(images[1], (450, 450))
canvas[450:900, :300] = cv2.resize(images[2], (300, 450))
canvas[450:900, 300:600] = cv2.resize(images[3], (300, 450))
canvas[450:900, 600:] = cv2.resize(img5, (300, 450))

# Show the result
cv2.imwrite('output.jpg', canvas)
cv2.imshow('Result', canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()

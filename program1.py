import cv2
import numpy as np
import os

def load_images():
    images = []
    for image_path in os.listdir("images"):
        image = cv2.imread(os.path.join("images", image_path))
        if image is not None:
            images.append(cv2.copyMakeBorder(cv2.resize(image, (446, 446)), 2, 2, 2, 2, cv2.BORDER_CONSTANT, None, value=[255, 255, 255]))
    return images

def process_last_image(images):
    font = cv2.FONT_HERSHEY_SIMPLEX
    num = input("+ m: ")
    img_last = images[-1].copy()
    cv2.putText(img_last, '+'+str(num), (int((img_last.shape[1] - cv2.getTextSize('+'+str(num), font, 2, 5)[0][0]) / 2), int((img_last.shape[0] + cv2.getTextSize('+'+str(num), font, 2, 5)[0][1]) / 2)), font, 2, (255, 255, 255), 5, cv2.LINE_AA)
    img_last = cv2.GaussianBlur(img_last, (5, 5), 0)
    img_last = cv2.addWeighted(img_last, 1.0, img_last, 0, -20)
    return img_last

def create_canvas(images, img_last):
    canvas = np.zeros((900, 900, 3), dtype=np.uint8)
    canvas[:450, :450] = cv2.resize(images[0], (450, 450))
    canvas[:450, 450:] = cv2.resize(images[1], (450, 450))
    canvas[450:, :450] = cv2.resize(images[2], (450, 450))
    canvas[450:, 450:] = cv2.resize(img_last, (450, 450))
    return canvas

if __name__ == "__main__":
    images = load_images()
    img_last = process_last_image(images)
    canvas = create_canvas(images, img_last)
    cv2.imwrite('output.jpg', canvas)
    cv2.imshow('Result', canvas)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

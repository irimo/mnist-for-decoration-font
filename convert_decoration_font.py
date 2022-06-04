import numpy as np
import os, glob
import cv2

X = []
Y = []
decoration_font_path = "./mini/0.jpg"
image = cv2.imread(decoration_font_path)

height = image.shape[0]
width = image.shape[1]

arr2 = image[:, :, 0]
arr3 = [0] * (height * width)
i = 0
for y in range(height):
    for x in range(width):
        arr2[y, x] = float(image[y, x, 0] / 255)
        arr3[i] = arr2[y, x]
data = np.array(arr3)
np.save("./output/mini_0.npy", data) 
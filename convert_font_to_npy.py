import numpy as np
import os, glob
import cv2

def output_npy(before_path, after_path):
    X = []
    Y = []
    # decoration_font_path = str(before_path)
    image = cv2.imread(before_path)
    side = 28
    image_re = cv2.resize(src=image, dsize=(side, side))
    height = side
    width = side

    arr2 = image_re[:, :, 0]
    arr3 = [0] * (height * width)

    for y in range(height):
        for x in range(width):
            arr2[y, x] =  float((255-image_re[y, x, 0]) / 255)
            
    arr3 = np.reshape(arr2, (784))
    data = np.array(arr3)
    print(np.shape(data))

    np.save(after_path, data) 

for i in range(0, 9):
    output_npy("./mini/"+str(i)+".jpg", "./output/mini_"+str(i)+".npy")
import cv2
import imageio
import numpy as np
from matplotlib import pyplot as plt
from image_slicer import slice, join
from color_calculator import avg_rgb, rgb_to_lab, calc_delta

img_url = './images/brain/image_0001.jpg'

# display image height, width, amount of color channels
image = imageio.imread(img_url)
print(
    f"image height: {image.shape[0]}px\n"
    f"image width: {image.shape[1]}px\n"
    f"amount of color channels: {image.shape[2]}\n"
)

# display image onscreen
# image_cv2 = cv2.imread(img_url)
# cv2.imshow('Brain', image_cv2)
# cv2.waitKey(0)

# calculate average RGB
RGB = avg_rgb(img_url)
print(RGB)

# display average of red, green, blue channels
print(
    f"Average RGB\n"
    f"R: {RGB[0]}\n"
    f"G: {RGB[1]}\n"
    f"B: {RGB[2]}\n"
)

# show image of average RGB
plt.imshow(RGB), plt.axis('off')
plt.show()

# convert RGB to CIE-L*ab
avg_R = RGB[0]
avg_G = RGB[1]
avg_B = RGB[2]
LAB = rgb_to_lab(avg_R, avg_G, avg_B)

LAB_1 = rgb_to_lab(48, 38, 41)
LAB_2 = rgb_to_lab(121, 130, 106)
LAB_3 = rgb_to_lab(48, 59, 122)

# display average LAB results
print(
    f"Average LAB\n"
    f"L: {LAB[0]}\n"
    f"A: {LAB[1]}\n"
    f"B: {LAB[2]}\n"
)

# slice image 3 x 3
# slice(IMG_URL, 9)

# print(calc_delta(LAB_1, LAB_2))
# print(calc_delta(LAB_1, LAB_3))
# print(calc_delta(LAB_2, LAB_3))
















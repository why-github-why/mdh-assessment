import cv2
import numpy as np
import imageio
from matplotlib import pyplot as plt
from image_slicer import slice, join
from PIL import Image
from color_calculator import avg_rgb, rgb_to_lab, calc_delta

# import os
#
# print(os.getcwd())
# curr_work_dir = os.open('./images/brain/tiles/', os.O_RDONLY)
# os.fchdir(curr_work_dir)
# print(os.getcwd())
# files = os.listdir(os.getcwd())
# image_list = [filename for filename in files if filename[-4:] in ['.png', '.PNG']]
#
# w, h = Image.open(image_list[0]).size
# N = len(image_list)
#
# print(w, h, N)

# convert jpg to png
# img_jpg = Image.open('./images/brain/tiles/brain.jpg')
# img_jpg.save('./images/brain/tiles/brain.png')

img = './images/brain/tiles/brain.png'
# slice image into tiles (20 x 20)
num_tiles = 400
tiles = slice(img, num_tiles)

for tile in tiles:
    print(type(tile), tile)

# for tile in tiles:
#     img = imageio.imread(tile.filename)
#     hist, bins = np.histogram(img.flatten(), 256, [0, 256])
#     cdf = hist.cumsum()
#     cdf_normalized = cdf * hist.max() / cdf.max()
#     plt.plot(cdf_normalized, color='g')
#     plt.hist(img.flatten(), 256, [0, 256], color='g')
#     plt.xlim([0, 256])
#     plt.legend(('cdf', 'histogram'), loc='upper left')
#     cdf_m = np.ma.masked_equal(cdf, 0)
#     cdf_o = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min())
#     cdf = np.ma.filled(cdf_o, 0).astype('uint8')
#     img3 = cdf[img]
#     cv2.imwrite(tile.filename, img3)
#     tile.image = Image.open(tile.filename)

# join tiles
image = join(tiles)
image.save('./images/brain/tiles/brain-joined.png')




import cv2
import numpy as np
from math import sqrt


def avg_rgb(img_url):
    """ Calculate average RGB """
    # load image as BGR
    image_bgr = cv2.imread(img_url, cv2.IMREAD_COLOR)

    # calculate the mean (average) of each channel
    bgr_channels = cv2.mean(image_bgr)

    # convert BGR to RGB by swapping blue and red channels
    rgb = np.array([(bgr_channels[2], bgr_channels[1], bgr_channels[0])])

    # convert nested list to list
    average_rgb = [rgb[0][0], rgb[0][1], rgb[0][2]]

    return average_rgb


# calculations based on info provided by http://www.easyrgb.com/en/math.php
def rgb_to_lab(red, green, blue):
    """ Convert RGB to XYZ to LAB """
    rgb = [red, green, blue]
    var_rgb = []
    lab = []

    # convert RGB to XYZ
    for channel in rgb:
        calc_1 = (channel / 255)

        if calc_1 > 0.04045:
            calc_2 = ((calc_1 + 0.055) / 1.055) ** 2.4
        else:
            calc_2 = calc_1 / 12.92

        calc_3 = calc_2 * 100
        var_rgb.append(calc_3)

    r = var_rgb[0]
    g = var_rgb[1]
    b = var_rgb[2]

    x = r * 0.4124 + g * 0.3576 + b * 0.1805
    y = r * 0.2126 + g * 0.7152 + b * 0.0722
    z = r * 0.0193 + g * 0.1192 + b * 0.9505

    # XYZ (Tristimulus)(D65/2° standard illuminant)
    calc_x = x / 95.047
    calc_y = y / 100.000
    calc_z = z / 108.883

    # convert XYZ to LAB (CIE-L*ab)
    if calc_x > 0.008856:
        new_x = calc_x ** (1 / 3)
    else:
        new_x = (7.787 * calc_x) + (16 / 116)
    if calc_y > 0.008856:
        new_y = calc_y ** (1 / 3)
    else:
        new_y = (7.787 * calc_y) + (16 / 116)
    if calc_z > 0.008856:
        new_z = calc_z ** (1 / 3)
    else:
        new_z = (7.787 * calc_z) + (16 / 116)

    cie_l = (116 * new_x) - 16
    cie_a = 500 * (new_x - new_y)
    cie_b = 200 * (new_y - new_z)

    # return LAB results as list
    lab.append(cie_l)
    lab.append(cie_a)
    lab.append(cie_b)

    return lab


# calculations based on info provided by http://www.easyrgb.com/en/math.php
def calc_delta(lab_1, lab_2):
    """ Calculate color difference of LAB (CIE-L*ab) using the Delta E* CIE formula """
    calc_l = (lab_1[0] - lab_2[0]) ** 2
    calc_a = (lab_1[1] - lab_2[1]) ** 2
    calc_b = (lab_1[2] - lab_2[2]) ** 2

    delta = sqrt(calc_l + calc_a + calc_b)

    return delta























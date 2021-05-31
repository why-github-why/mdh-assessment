# MDH Assessment

Please complete the following assessment in any stack/technology you feel comfortable with.\
Build a console app that takes a large input image, and a folder with tile images as input.\
(You can download this image dataset that should work well: http://www.vision.caltech.edu/Image_Datasets/Caltech101/)
 
1. Calculate avg RGB for each tile image. (Avg R, Avg G, Avg B)\
    Calculating the average RGB value for each of the files in the bigger dataset you will use as your tiles for the bigger image.
2. Divide our input image in 20x20 parts. (You can change this however you like)\
    The one image will be separated into 400 separate parts / images.
3. Calculate the avg RGB for each of the 400 parts in our larger input image.
4. Calculate the distance between every tile (AVG RGB) and every part of our image (AVG RGB):\
    We don't want to use Euclidian distance to calculate our distances between colours since this does not take human colour perception into account.
    Instead let's use "Delta E* CIE" and then use these transformations to go from RGB-> CIE-L*ab to do the calculation.
    http://www.easyrgb.com/en/math.php
5. Choose the tile images with the smallest distance, resize them and replace that image part with the tile.
6. Save output image. (It should look like the original image, made up of a bunch of smaller tiles)

## Language
### Python

## Libraries
Please refer to *requirements.txt*

## Progress
- [x] Calculate average RGB
- [x] Divide image in 20 x 20 tiles
- [x] Calculate average RGB for each tile
- [x] Calculate distance between each tile (average RGB)
- [ ] Reconstruct image based on smallest distance
- [ ] Save output image

## Code
#### Calculate average RGB
Source: [color_calculator.py](https://github.com/why-github-why/mdh-assessment/blob/main/color_calculator.py) \
*Provide image URL (in string format):*
```
def avg_rgb(img_url):
    ...
```

#### Convert RGB to XYZ to LAB
Source: [color_calculator.py](https://github.com/why-github-why/mdh-assessment/blob/main/color_calculator.py) \
Calculations based on: http://www.easyrgb.com/en/math.php \
*Provide R, G, B values (as float values):*
```
def rgb_to_lab(red, green, blue):
    """ Convert RGB to XYZ to LAB """
    ...
```
#### Calculate distance between two LAB values
Source: [color_calculator.py](https://github.com/why-github-why/mdh-assessment/blob/main/color_calculator.py) \
Calculations also based on: http://www.easyrgb.com/en/math.php \
*Provide two different LAB results (as lists):*
```
def calc_delta(lab_1, lab_2):
    """ Calculate color difference of LAB (CIE-L*ab) using the Delta E* CIE formula """
    ...
```
#### Slice image into 20 x 20 tiles
Source: [reconstruct_image.py](https://github.com/why-github-why/mdh-assessment/blob/main/reconstruct_image.py) \
*Provide image URL and number of tiles (20 x 20 = 400):*
```
img = './images/brain/tiles/brain.png'
num_tiles = 400
tiles = slice(img, num_tiles)
```


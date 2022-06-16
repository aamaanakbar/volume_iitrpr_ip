import cv2
import numpy as np
import matplotlib

from PIL import Image
img = input("/home/cse-lab-207/Downloads/volume/b_20_gray_binary_otsu.png")
img = Image.open(img)
for y in range(img.height):
  for x in range(img.width):
    pixel = img.getpixel((x, y))
    if pixel >= 200:
         print(pixel,"pixels are bright.")
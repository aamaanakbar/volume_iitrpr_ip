# importing libraries
import cv2
import numpy as np
import matplotlib
# reading the image data from desired directory
img = cv2.imread("/home/cse-lab-207/Downloads/volume/b_20_gray_binary_otsu.png")
#cv2.imshow('Image',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

# importing the module
#import cv2
  
# loading the image
#img = cv2.imread("geeksforgeeks.png")
  
# fetching the dimensions
wid = img.shape[1]
hgt = img.shape[0]
  
# displaying the dimensions
print(str(wid) + "x" + str(hgt))
# counting the number of pixels

y=img.shape[1]*img.shape[0]
t=3*y
print(t)

z=number_of_white_pix = np.sum(img == 255)
#number_of_black_pix = np.sum(img == 200)
  
print('Number of white pixels:', number_of_white_pix)
#print('Number of black pixels:', number_of_black_pix)

print('forground pixel is =',t-z)
#print(t-z)
print(img.shape)
#print(type(img.shape))

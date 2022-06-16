
# import opencv
import cv2
 
 
# Load the input image
image = cv2.imread('/home/cse-lab-207/Downloads/1654162133316.jpg')
#cv2.imshow('Original', image)
#cv2.waitKey(0)
 

#new code for resize.....

print('Original Dimensions : ',image.shape)

# Use the cvtColor() function to grayscale the image
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
#cv2.imshow('Grayscale', gray_image)
#here con 
 
scale_percent = 20 # percent of original size
width = int(gray_image.shape[1] * scale_percent / 100)
height = int(gray_image.shape[0] * scale_percent / 100)
dim = (width, height)
  
# resize image
resized = cv2.resize(gray_image, dim, interpolation = cv2.INTER_AREA)
 
print('Resized Dimensions : ',resized.shape)
 
cv2.imshow("Resized image", resized)


#before it resize code .....
cv2.waitKey(0) 
 

 
# Window shown waits for any key pressing event
cv2.destroyAllWindows()
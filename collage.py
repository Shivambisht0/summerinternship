import cv2

c1=cv2.imread('CROP1.jpg')

c2=cv2.imread('CROP2.jpg')
#Making the images compatible for concatenation.
c1=c1[10:160,10:160]
c2=c2[10:160,10:160]
#Showing the part of image1 to concatenate
cv2.imshow("Pic1",c1)
cv2.waitKey()
cv2.destroyAllWindows()
 
#Showing the part of image2 to concatenate
cv2.imshow("Pic1",c2)
cv2.waitKey()
cv2.destroyAllWindows()
 
#Import numpy to use concatenate()
import numpy
#Concatenating along the axis=0
collage=numpy.concatenate((c1,c2))
#Collage of the two images.
cv2.imshow("Collage",collage)
cv2.waitKey()
cv2.destroyAllWindows()

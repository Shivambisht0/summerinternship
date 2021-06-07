#For image processing
import cv2
#To create a numpy array
import numpy
#Creating a 3-D numpy array, to make colourful picture 
photo = numpy.zeros([400,400,3])

#creating a white canvas for the image.
photo[:,:]=[255,255,255]

photo
#For inserting orange colour
photo[89:121,104:289]=[0,69,255]
#For inserting green colour
photo[153:185,104:289]=[0,255,0]
#For the blue borders
photo[183:185,104:289]=[255,0,0]
photo[87:185,102:104]=[255,0,0]
photo[87:185,289:291]=[255,0,0]
photo[87:89,104:289]=[255,0,0]


#To show the created photo and then holding it and then closing it.
cv2.imshow("hi",photo)
cv2.waitKey()
cv2.DestroyAllWindows()

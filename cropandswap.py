import cv2
#Reading the first image
pic1=cv2.imread('crop1.jpg')

#Reading the second image
pic2=cv2.imread('crop2.jpg')
#Showing the first image
cv2.imshow("FirstImage",pic1)
cv2.waitKey()
cv2.destroyAllWindows()
 
#Cropped part of the first image which you want to swap
cropped1=pic1[70:130,65:150]
#Showing the cropped part
cv2.imshow("Cropped1",cropped1)
cv2.waitKey()
cv2.destroyAllWindows()
 
#Showing the second image
cv2.imshow("SecondImage",pic2)
cv2.waitKey()
cv2.destroyAllWindows()
 
#Cropping the second image
cropped2=pic2[70:130,65:150]
# Showing the cropped part
cv2.imshow("Cropped2",cropped2)
cv2.waitKey()
cv2.destroyAllWindows()
 
#Again storing fresh image in variable pic1,pic2
pic1=cv2.imread('crop1.jpg')
pic2=cv2.imread('crop2.jpg')


pic1copy=pic1

pic1copy[70:130,65:150]=cropped2
#Showing the final image1
cv2.imshow("AfterCrop1",pic1)
cv2.waitKey()
cv2.destroyAllWindows()
 
pic2[70:130,65:150]=cropped1
#Showing the final image2
cv2.imshow("AfterCrop2",pic2)
cv2.waitKey()
cv2.destroyAllWindows()

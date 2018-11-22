import numpy as np
import cv2

image = cv2.imread("/Users/nikhil.rai/Documents/courses/Ex_Files_OpenCV_Python_Dev/Exercise Files/Ch02/02_06 Begin/thresh.jpg")

cv2.imshow("Original",image)

blur = cv2.GaussianBlur(image,(5,55),0)
cv2.imshow("Blur",blur)

'''
Erosion: Gets the black spots and converts it into black spots based on iterations

Dilation: Gets the black spots and starts converting to white spots based on iterations

How it works: A section is created that iterates through the image to perform the action. In our example we are going to hav 5,5 section doing the iteration
'''
kernel = np.ones((5,5),'uint8')

dilated = cv2.dilate(image,kernel,iterations=1)
eroded = cv2.erode(image,kernel,iterations=1)
dilated1 = cv2.dilate(image,kernel,iterations=3)
cv2.imshow("Dilated",dilated)
cv2.imshow("Dilated1",dilated1)#tried 3 iterations
cv2.imshow("Eroded",eroded)


cv2.waitKey(0)
cv2.destroyAllWindows()

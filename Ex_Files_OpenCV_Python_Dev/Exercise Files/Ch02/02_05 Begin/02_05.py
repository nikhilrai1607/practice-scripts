import numpy as np
import cv2

img = cv2.imread("/Users/nikhil.rai/Documents/courses/Ex_Files_OpenCV_Python_Dev/Exercise Files/Ch02/02_05 Begin/butterfly.jpg", 1)

#Convert all colors to gray
gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
cv2.imwrite("/Users/nikhil.rai/Documents/courses/Ex_Files_OpenCV_Python_Dev/Exercise Files/Ch02/02_05 Begin/gray.jpg",gray)

'''
Efficient and faster way of separating the b,g,r compared to cv2.split
'''
b = img[:,:,0]
g = img[:,:,1]
r = img[:,:,2]

'''
Create transparency for a particular color
'''

rgba = cv2.merge((b,g,r,g))
rgba1 = cv2.merge((b,g,r,r))
rgba2 = cv2.merge((b,g,r,b))

xx = np.concatenate((rgba,rgba1,rgba2),axis=1)

#.PNG is being used as jpeg cannot display transparency factor
cv2.imwrite("/Users/nikhil.rai/Documents/courses/Ex_Files_OpenCV_Python_Dev/Exercise Files/Ch02/02_05 Begin/rgba.png",xx)

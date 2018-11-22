import numpy as np
import cv2

'''
imread reads the image
1 will load the image in full color. if nothing is passed, this is default
moveWindow will set the image window to a specific point on screen if 0,0, it is the top left corner of the screen
'''
img = cv2.imread("/Users/nikhil.rai/Documents/courses/Ex_Files_OpenCV_Python_Dev/Exercise Files/Ch02/02_04 Begin/butterfly.jpg", 1)
cv2.imshow("Image",img)
cv2.moveWindow("Image",0,0)

print(img.shape)
height,width,channels = img.shape

'''
cv2.split will split each matrix into 3 parts (in our case)
'''
b,g,r = cv2.split(img)
#this creates a new image array of width 3 times of original
rgb_split = np.empty([height,width*3,3],'uint8')

rgb_split[:,0:width] = cv2.merge([b,b,b])
rgb_split[:,width:width*2] = cv2.merge([g,g,g])
rgb_split[:,width*2:width*3] = cv2.merge([r,r,r])

cv2.imshow("Channels",rgb_split)
cv2.moveWindow("Channels",0,height)

'''
To get the (HSV) Hue, Saturation and Value indexes rather than bgr or to convert it
'''
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
h,s,v = cv2.split(hsv)
hsv_split = np.concatenate((h,s,v),axis=1)
cv2.imshow("Split HSV",hsv_split)

cv2.waitKey(0)
cv2.destroyAllWindows()

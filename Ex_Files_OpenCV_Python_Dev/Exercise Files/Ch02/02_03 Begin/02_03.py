import numpy as np
import cv2
'''
#create a numpy array of zeros
#[150,200,1]  =>  [height,width,channels]
#uint8 = max value of each entry will range between 0 to 2**8(256-1)
'''
black = np.zeros([150,200,1],'uint8')
cv2.imshow("Black",black)
#print(black[0,0,:])

'''
We can also define an array of ones with np.ones
Note this will create an array of 1s however that doesn't mean it is white
'''
ones = np.ones([150,200,3],'uint8')
cv2.imshow('Ones',ones)

'''
To create a white image we will have to set all to max
'''
white = np.ones([150,200,3],'uint8')
white *= (2**8-1)
cv2.imshow('white',white)
#print(white.shape)
#print(white[0].shape)

'''
We can deep copy an np array with array.copy
'''

blue = ones.copy()
blue[:,:] = (255,0,0)
cv2.imshow('Blue',blue)

#add wait to the window for keystroke
cv2.waitKey(0)
#on Keystroke destroy all windows
cv2.destroyAllWindows()

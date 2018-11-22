import numpy as np
import cv2

# Global variables
canvas = np.ones([500,500,3],'uint8')*255
'''
Set the global parameters for the circle
'''
color = (0,255,0)
radius = 2

#handle the mouse click
pressed = False

# click callback
def click(event, x, y, flags, param):
	global canvas, pressed
	if event == cv2.EVENT_LBUTTONDOWN:
		#print("LButton Down")
		pressed = True
		cv2.circle(canvas,(x,y),radius,color,-1)
	elif event == cv2.EVENT_MOUSEMOVE and pressed == True:
		#print("Mouse Move")
		cv2.circle(canvas,(x,y),radius,color,-1)
	elif event == cv2.EVENT_LBUTTONUP:
		#print("LButton Up")
		pressed = False

# window initialization and callback assignment
cv2.namedWindow("canvas")
cv2.setMouseCallback("canvas", click)

# Forever draw loop
while True:

	cv2.imshow("canvas",canvas)

	# key capture every 1ms
	ch = cv2.waitKey(1)
	if ch & 0xFF == ord('q'):
		break
	elif ch & 0xFF == ord('b'):
		color = (255,0,0)
	elif ch & 0xFF == ord('r'):
		color = (0,0,255)
	elif ch & 0xFF == ord('g'):
		color = (0,255,0)



cv2.destroyAllWindows()

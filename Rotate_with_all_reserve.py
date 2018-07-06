import math
import cv2
import numpy as np

def rotate(img,x1,x2,x3,x4,y1,y2,y3,y4,flag=0):
	if flag == 0:
		theta = math.atan((y2-y1)/(x2-x1+0.0000001))
		angle = theta/3.14*180
	else:
		angle = flag
		theta = angle/180*3.14
	
	h,w,c = img.shape		
	nw = (abs(h*np.sin(theta)) + abs(w*np.cos(theta)))*1
	nh = (abs(h*np.cos(theta)) + abs(w*np.sin(theta)))*1	
		
	x_c = nw/2
	y_c = nh/2
	
	rotateMat = cv2.getRotationMatrix2D((int(x_c), int(y_c)), angle, 1)	
	pos_0 = (nw-w)/2
	pos_1 = (nh-h)/2
	pos_2 = 0
	res = np.dot(rotateMat,np.array([[pos_0],[pos_1],[pos_2]]))
	rotateMat[0,2] += res[0]
	rotateMat[1,2] += res[1]	
	imgRotation = cv2.warpAffine(img, rotateMat, (int(nw), int(nh)), borderValue=(0, 0, 0))	
	
	x11 = int(rotateMat[0,0]*x1 + rotateMat[0,1]*y1 + rotateMat[0,2])
	x21 = int(rotateMat[0,0]*x2 + rotateMat[0,1]*y2 + rotateMat[0,2])
	x31 = int(rotateMat[0,0]*x3 + rotateMat[0,1]*y3 + rotateMat[0,2])
	x41 = int(rotateMat[0,0]*x4 + rotateMat[0,1]*y4 + rotateMat[0,2])

	y11 = int(rotateMat[1,0]*x1 + rotateMat[1,1]*y1 + rotateMat[1,2])
	y21 = int(rotateMat[1,0]*x2 + rotateMat[1,1]*y2 + rotateMat[1,2])
	y31 = int(rotateMat[1,0]*x3 + rotateMat[1,1]*y3 + rotateMat[1,2])
	y41 = int(rotateMat[1,0]*x4 + rotateMat[1,1]*y4 + rotateMat[1,2])	
	
	return imgRotation,x11,x21,x31,x41,y11,y21,y31,y41
	

img = cv2.imread('ori.jpg')
x1,y1,x2,y2,x3,y3,x4,y4 = 100,200,500,200,500,700,100,700
RotateAngle = 30 # 0: rotate with the rectangle angle
imgRotation,x1,x2,x3,x4,y1,y2,y3,y4 = rotate(img,x1,x2,x3,x4,y1,y2,y3,y4,RotateAngle)

cv2.line(imgRotation, (x1,y1),(x2,y2),(0,0,255),4)
cv2.line(imgRotation, (x2,y2),(x3,y3),(0,0,255),4)
cv2.line(imgRotation, (x3,y3),(x4,y4),(0,0,255),4)
cv2.line(imgRotation, (x4,y4),(x1,y1),(0,0,255),4)

cv2.imwrite('Rotated.jpg', imgRotation)
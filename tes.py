import cv2
import numpy as np


camera=cv2.VideoCapture(0)

ret,frame=camera.read()


while(camera.isOpened()):
	
	
	gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

	Brightness= np.ones(gray.shape,dtype="uint8")*60
	brigthnessForGray=cv2.add(gray,Brightness)
	
	Darkness= np.ones(gray.shape,dtype="uint8")*60
	darknessForGray=cv2.subtract(gray,Darkness)

	Contrast=cv2.add(brigthnessForGray,darknessForGray)

	face_cascade = cv2.CascadeClassifier('/home/flitzcore/opencv_build/opencv/data/haarcascades/haarcascade_frontalface_alt2.xml')
	faces = face_cascade.detectMultiScale(brigthnessForGray, 1.1, 4)
	
	
	for x,y,w,h in faces:
		frame[y:y+h,x:x+h]=cv2.medianBlur(frame[y:y+h,x:x+h],55)


	cv2.imshow('frame',frame)

	ret,frame=camera.read()

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
camera.release()
cv2.destroyAllWindows()
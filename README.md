#Dokumentasi
###Hari senin
Hari pertama, saya membaca hingga bagian threshold. Beberapa penjelasan seperti cara perhitungan lumayan sulit jadi saya coba search di youtube
###Hari selasa
Hari kedua, saya pikir akan lebih baik kalau saya memulai proyek, supaya lebih mudah mengerti. Saya membaca hingga contours, namun ada beberapa logika kerja yang masih kurang dimengerti
###Hari Rabu

# OpenCV_BlurFace
First of all, i set everything that i will need and take picture from my webcam
```
import cv2
import numpy as np


camera=cv2.VideoCapture(0)

ret,frame=camera.read()
```
After that, i use while loop, to do thing while my cammera is on
```
while(camera.isOpened()):
```
Then, i apply some effect, like grayscale, and contrast
```
  gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

	Brightness= np.ones(gray.shape,dtype="uint8")*60
	brigthnessForGray=cv2.add(gray,Brightness)
	
	Darkness= np.ones(gray.shape,dtype="uint8")*60
	darknessForGray=cv2.subtract(gray,Darkness)

	Contrast=cv2.add(brigthnessForGray,darknessForGray)
  ```
This effects aims to facilitate the cascade method. Then,i apply the cascade method
  ```
  face_cascade = cv2.CascadeClassifier('/home/flitzcore/opencv_build/opencv/data/haarcascades/haarcascade_frontalface_alt2.xml')
	faces = face_cascade.detectMultiScale(brigthnessForGray, 1.1, 4)
  ```
I use this method to detect my face. After that, i use for loop to blur my face
```
for x,y,w,h in faces:
		frame[y:y+h,x:x+h]=cv2.medianBlur(frame[y:y+h,x:x+h],55)
```

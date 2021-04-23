# Dokumentasi
### Hari senin
Hari pertama, saya membaca hingga bagian threshold. Beberapa penjelasan seperti cara perhitungan lumayan sulit jadi saya coba search di youtube
### Hari selasa
Hari kedua, saya pikir akan lebih baik kalau saya memulai proyek, supaya lebih mudah mengerti. Saya membaca hingga contours, namun ada beberapa logika kerja yang masih kurang dimengerti
### Hari rabu
Saya memutuskan untuk membuat proyek face blur. Saya mencari cara kerjanya di youtube, setelah saya mengikuti cara kerjanya, ternyata terjadi kesalahan detect sehingga background saya juga kena blur. Saya mempelajari ulang mengenai blur,serta mencari cara untuk meningkatkan kontras pada gambar, untuk meningkatkan kualitas seleksi. Saya sempat mencoba metode threshold tapi hasilnya justru lebih tidak akurat.
### Hari kamis
Mendekati pengumpulan, saya memutuskan untuk menerapkan metode kontras pada projek saya, dan melanjutkan pembelajaran di tutorial pada contour karena masih banyak bagian yang kurang saya mengerti.
### Hari jumat
Hari terakhir, saya menyelesaikan materi, namun tetap ada beberapa bagian yang masih belum saya kuasai. Setelah itu, saya menyelesaikan proyek saya, dan membuat dokumentasi.

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

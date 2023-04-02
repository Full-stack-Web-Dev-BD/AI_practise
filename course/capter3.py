import cv2
import numpy as np

kernel = np.ones((5,5), np.uint8)




path = "../Resources/lena.png"
img = cv2.imread(path)
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(19,19),0 )
imgCanny = cv2.Canny(imgBlur, 10 , 50)
imgDilation = cv2.dilate(imgCanny,kernel, iterations=1 )
imgEroded = cv2.erode(imgDilation, kernel, iterations= 3)

cv2.imshow("Image", img)
cv2.imshow("Gray Image", imgGray)
cv2.imshow("Gaussing Image",imgBlur)
cv2.imshow("Image Canny",imgCanny)
cv2.imshow("Image Dilation ",imgDilation)
cv2.imshow("Image Eroded",imgEroded)
cv2.waitKey(0)

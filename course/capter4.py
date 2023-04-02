import cv2
import numpy as np
img= cv2.imread("Resources/card.png")

circles= np.zeros((4,2), np.int32)
counter = 0

def mousePoints(event, x , y , flags, params):
    global counter
    if event == cv2.EVENT_LBUTTONDOWN and counter < 4:
        print(x,y)
        circles[ counter] = x,y
        counter= counter+1
        print(circles)
    elif event== cv2.EVENT_LBUTTONDOWN and counter >=4:
        print("Requirment already fullfilled")


while True:
    if counter ==4:

        width, height= 300, 300
        pts1= np.float32([circles[0], circles[1], circles[2], circles[3]])
        pts2  = np.float32([[0,0], [width,0], [height,0], [width, height]])
        matrix= cv2.getPerspectiveTransform(pts1, pts2)
        imgOutput = cv2.warpPerspective(img, matrix, (width, height))
        cv2.imshow("Output Image", imgOutput)

    for x in range( 0 , 4):
        cv2.circle(img, (circles[x][0], circles[x][1]),3, (0,255, 0), cv2.FILLED)

    cv2.imshow("Main Image", img)
    cv2.setMouseCallback("Main Image", mousePoints)
    cv2.waitKey(1)



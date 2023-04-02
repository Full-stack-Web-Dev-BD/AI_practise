import cv2
import numpy as np

frameWidthHeight= 600

cap= cv2.VideoCapture(0)
cap.set(3, frameWidthHeight)
cap.set(4, frameWidthHeight)

def empty (a):
    pass


cv2.namedWindow("HSV")
cv2.resizeWindow("HSV",frameWidthHeight, frameWidthHeight)
cv2.createTrackbar("HUE_MIN", "HSV", 0, 179, empty)
cv2.createTrackbar("HUE_MAX", "HSV", 179, 179, empty)
cv2.createTrackbar("SAT_MIN", "HSV", 0, 255, empty)
cv2.createTrackbar("SAT_MAX", "HSV", 255, 255, empty)
cv2.createTrackbar("VALUE_MIN", "HSV", 0,255, empty)
cv2.createTrackbar("VALUE_MAX", "HSV", 255, 255, empty)

while True:
    _, img= cap.read()
    imgHsv= cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h_min= cv2.getTrackbarPos("HUE_MIN", "HSV")
    h_max= cv2.getTrackbarPos("HUE_MAX", "HSV")
    s_min= cv2.getTrackbarPos("SAT_MIN", "HSV")
    s_max= cv2.getTrackbarPos("SAT_MAX", "HSV")
    v_min= cv2.getTrackbarPos("VALUE_MIN", "HSV")
    v_max= cv2.getTrackbarPos("VALUE_MAX", "HSV")

    lower= np.array([h_min, s_min, v_min])
    upper= np.array([h_max, s_max, v_max])
    mask= cv2.inRange(imgHsv, lower, upper)
    result= cv2.bitwise_and(img, img, mask=mask)


    mask= cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    hStack= np.hstack([img, mask, result])

    # cv2.imshow("HSV",imgHsv)
    # cv2.imshow("Mask",mask)
    # cv2.imshow("Result",result)
    cv2.imshow("H Stack",hStack)
    # cv2.imshow("Video", img)
    if cv2.waitKey(1) and  0xff == ord('q'):
        break
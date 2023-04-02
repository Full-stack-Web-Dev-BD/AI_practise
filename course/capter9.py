import cv2


cap= cv2.VideoCapture(0)

while True:
    _, img= cap.read()

    imgBlur= cv2.GaussianBlur(img, (7,7), 1)
    imgGray= cv2.cvtColor(imgBlur, cv2.COLOR_BGR2GRAY)



    cv2.imshow("Video", img)
    if cv2.waitKey(1) and 0xFF== ord('q'):
        break

def stackImages(scale, imgArray):
    rows= len(imgArray)
    cols= len(imgArray[0])
    rowsAvailble= isinstance(imgArray[0], list)
    width= imgArray[0][0].shape[1]
    height= imgArray[0][0].shape[0]
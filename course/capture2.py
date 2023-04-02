import cv2

frameWidth = 640
frameHeight = 240

cap = cv2.VideoCapture("Resources/ct.mp4")
# cap.set(3,frameWidth) # 3 is specified for width
# cap.set(4,frameHeight) # 4 is specified for height

while True:
    success, frame= cap.read()
    # frame= cv2.resize(frame, (frameWidth, frameHeight))
    cv2.imshow("Video", frame)
    cv2.waitKey(1)

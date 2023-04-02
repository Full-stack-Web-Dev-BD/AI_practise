import cv2

cap = cv2.VideoCapture("Resources/ct.mp4")

frame_time = 20
press_q = 113
pressed_space = 32
paused = False
while True:
    success, frame = cap.read()
    cv2.imshow("Video", frame)
    pressed_key = cv2.waitKey(frame_time)
    print("Pressed Key ")

    if pressed_key == pressed_space:
        if not paused:
            frame_time = 0
            paused = True
            print("Video Paused ")
        else:
            frame_time = 20
            paused = False
            print("Video Resumed ")
    elif pressed_key == press_q:
        print("Video  exit")
        break



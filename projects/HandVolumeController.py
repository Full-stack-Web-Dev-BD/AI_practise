import cv2             #type in the shell pip install cv2
import mediapipe as mp  # type in the shell pip install mediapipe
import time
import math
import numpy as np
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands(static_image_mode=False,
                      max_num_hands=2,
                      min_detection_confidence=0.5,
                      min_tracking_confidence=0.7)
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0

# PyCaw
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
# volume.GetMasterVolumeLevel()
volumeRange= volume.GetVolumeRange()
minVolume=volumeRange[0]
maxVolume=volumeRange[1]


while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)
    lmlist= []
    if results.multi_hand_landmarks:
        hand_landmarks = results.multi_hand_landmarks[0]

        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x *w), int(lm.y*h)
                if id ==4 or id==8:
                    cv2.circle(img, (cx,cy), 3, (255,0,255), cv2.FILLED)
                mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                for id, lm in enumerate(handLms.landmark):
                    x_px = round(lm.x * img.shape[1])
                    y_px = round(lm.y * img.shape[0])
                    z_px = round(lm.z * img.shape[1])

                    # Add the pixel coordinates to the list
                    lmlist.append([id, x_px, y_px])
    if len(lmlist) != 0 :
        x1, y1= lmlist[4][1], lmlist[4][2]
        x2, y2= lmlist[8][1], lmlist[8][2]
        cx, cy= (x1+x2) //2, (y1+y2)//2


        cv2.circle(img, (x1, y1), 7, (255, 0 , 255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 7, (255, 0 , 255), cv2.FILLED)
        cv2.circle(img, (cx, cy), 7, (255, 0 , 255), cv2.FILLED)

        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 2)

        length= math.hypot(x2-x1, y2-y1)
        # Hand Range is : 120-30

        vol= np.interp(length, [30, 120], [minVolume, maxVolume])
        volume.SetMasterVolumeLevel(vol, None)



        if length<30:
            cv2.circle(img ,(cx, cy), 5 ,(0, 255,0), cv2.FILLED)


    cv2.rectangle(img, (30, 40), (0, 0), (0,255, 0 ), 4)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img,f"FPS:{str(int(fps))}", (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
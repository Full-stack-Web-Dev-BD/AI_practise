import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Read the input image
cap= cv2.VideoCapture(0)

while True:
    _, img = cap.read()
    # Detect faces
    faces = face_cascade.detectMultiScale(img, 1.1, 4)

    # # Draw rectangle around the faces with filled color
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # # Display the output image with the detected faces
    # cv2.imshow('Detected Faces', img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    cv2.imshow("Video", img)
    cv2.waitKey(1)
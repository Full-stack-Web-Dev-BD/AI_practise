
import cv2
import cv2.face

# Load the video
video = cv2.VideoCapture('Resources/eye.mp4')

# Create the face mesh detector
meshDetector = cv2.face.FaceMeshDetector()

# Face detection using the mesh detector
faces = meshDetector.fit(video)

# Initialize the eye blink counter
blinkCount = 0

# Loop over each frame of the video
while video.isOpened():
    # Read the frame
    ret, frame = video.read()
    # Check if frame is valid
    if ret == True:
        # Loop over each face detected in the frame
        for face in faces:
            # Get the eye region from the face
            eyeRegion = face['eyes']
            # Check if eyes are present in the face
            if len(eyeRegion) > 0:
                # Loop over each eye
                for eye in eyeRegion:
                    # Get the eye ROI
                    eyeROI = frame[eye[0][1]:eye[1][1], eye[0][0]:eye[1][0]]
                    # Check if eye has blinked
                    if cv2.mean(eyeROI)[2] < 100:
                        blinkCount += 1
        # Display the frame
        cv2.imshow('frame', frame)
        # Check for keypress
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release the video capture
video.release()
# Destroy all windows
cv2.destroyAllWindows()

# Print the blink count
print("Number of blinks:", blinkCount)
import cv2  # Import the OpenCV library # pip install opencv-python

# Load the pre-trained Haar cascade classifier for face detection
face_cascade = cv2.CascadeClassifier("C:/Users/hp/AppData/Local/Programs/Python/Python311/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml") # Give Your Actual Path to the pre-Trained opencv model 

# Initialize the video capture device (webcam)
video_capture = cv2.VideoCapture(0)

# Start an infinite loop to continuously capture and process video frames
while True:
    # Read a frame from the video capture device
    ret, frame = video_capture.read()

    # Convert the frame to grayscale (face detection works on grayscale images)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,         # Scale factor for multi-scale face detection
        minNeighbors=5,         # Minimum number of neighbor rectangles for a detected face
        minSize=(30, 30),       # Minimum size of a detected face
        flags=cv2.CASCADE_SCALE_IMAGE  # Flag to use the new cascade classifier
    )

    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the frame with detected faces
    cv2.imshow("video_live", frame)

    # Check for the "a" key press to terminate the program
    if cv2.waitKey(10) == ord("a"):
        break

# Release the video capture device
video_capture.release()




# video_cap = cv2.VideoCapture(0)
# while True:
#     ret , video = video_cap.read()
#     cv2.imshow("video_live", video)
#     if cv2.waitKey(10) == ord("a"):
#         break
# video_cap.release()
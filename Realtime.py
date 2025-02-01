import cv2

# Initialize the webcam
cap = cv2.VideoCapture(0)
cap.set(4, 640)  # Set width
cap.set(4, 480)  # Set height

# Load the Haar Cascade Classifiers
face_cascade = cv2.CascadeClassifier(r"C:\Users\Hp\Downloads\haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(r"C:\Users\Hp\Downloads\haarcascade_eye.xml")

# Verify cascade loading
if face_cascade.empty():
    print("Error: Face cascade file not loaded!")
    exit()
if eye_cascade.empty():
    print("Error: Eye cascade file not loaded!")
    exit()

while True:
    # Read the video stream
    success, img = cap.read()
    if not success:
        print("Failed to capture frame from webcam. Exiting...")
        break

    # Convert the image to grayscale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(img_gray, 1.3, 2) #scaleFactor = Adjust the size of image
                                                            #minNeighbors = Specify how many neighbors person can have


    # Loop through detecqted faces
    for (x, y, w, h) in faces:
        # Draw a rectangle around each face
        cv2.rectangle( img, (x, y), (x + w, y + h), (0, 0, 255), 2 )

        # Focus on the face region to detect eyes
        roi_gray = img_gray[y:y + h, x:x + w]
        roi_color =  img[y:y + h, x:x + w]

        # Detect eyes within the face region
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 4)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

    # Display the output
    cv2.imshow("Face and Eye Detection",  img)

    # Exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close windows
cap.release()
cv2.destroyAllWindows()

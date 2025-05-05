import cv2 #Import OpenCV, a library for computer vision tasks like face detection and webcam access.
from deepface import DeepFace # Imports DeepFace, a Python library that provides pre-built facial recognition functions.
import pandas as pd #Imports pandas, used for handling tabular data (like the attendance file).
from datetime import datetime #Lets you work with current date and time, used for timestamping attendance.
import os #Gives access to file and directory operations, like checking if a file exists.s

# Path to known faces database
db_path = "known_faces"

# Initialize webcam
cap = cv2.VideoCapture(0)

# Create attendance file if not exists
if not os.path.exists("attendance.csv"):
    with open("attendance.csv", "w") as f:
        f.write("Name,Time\n")

# A set to keep track of people who have already been marked present during this session (avoids duplicate entries).
marked = set()

print("📸 Starting face recognition. Press 'q' to quit...")

try:
    while True:
        '''
           Reads a frame (snapshot) from the webcam.
           ret is True if the frame is captured successfully.
        '''
        ret, frame = cap.read()
        if not ret:
            print("❌ Failed to grab frame.")
            break

        # Makes a copy of the frame to draw rectangles and text on it (so the original image is untouched).
        display_frame = frame.copy()

        try:
            # Face recognition
            '''
            This line searches for the face in the frame by comparing it with the faces in the known_faces folder.
            detector_backend='opencv' tells DeepFace to use OpenCV’s face detector.
            enforce_detection=False allows the process to continue even if no face is detected.
            silent=True suppresses print messages.
            '''
            results = DeepFace.find( 
                img_path=frame,
                db_path=db_path,
                detector_backend='opencv',  # or 'mediapipe'
                enforce_detection=False,
                silent=True
            )

            if len(results) > 0 and not results[0].empty:
                '''
                    Checks if any matching face was found.
                    results[0] is a pandas DataFrame that contains matches.
                '''
                identity_path = results[0].iloc[0]['identity'] #Gets the path to the matching image, and extracts the person's name from the folder name.
                name = os.path.basename(os.path.dirname(identity_path))

                # Optional: Draw face rectangle using OpenCV face detector
                face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml') # Loads a pre-trained Haar Cascade classifier for face detection.
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # Converts the image to grayscale since face detection works better on grayscale.
                '''
                Detects faces in the grayscale image.
                Returns a list of rectangles around each detected face.
                '''
                faces = face_cascade.detectMultiScale(gray, 1.3, 5)

                for (x, y, w, h) in faces:# For each face, it draws a green rectangle and writes the name above it on the display frame.
                    cv2.rectangle(display_frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                    cv2.putText(display_frame, name, (x, y - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

                if name not in marked:
                    '''
                    If the person is not already marked, then:
                    Get the current date and time.
                    Append their name and timestamp to the attendance.csv file.
                    Add their name to the marked set.
                    '''
                    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    with open("attendance.csv", "a") as f:
                        f.write(f"{name},{now}\n")
                    marked.add(name)
                    print(f"✅ Marked attendance for: {name} at {now}")
                else:
                    print(f"👀 {name} already marked.") #If the name was already recorded in this session, show a message but don’t record again.
            else:
                print("😕 Unknown Face") #If DeepFace didn’t find a match, print this.

        except Exception as e:
            print("⚠️ Error:", str(e)) #If something goes wrong (like no camera, no face, etc.), show the error.

        # Show webcam frame
        cv2.imshow("Face Recognition", display_frame) #Displays the webcam frame with rectangles and names.

        # Exit on 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'): #Checks if the user pressed 'q' key to stop the loop.
            break

except KeyboardInterrupt: #If the user presses Ctrl+C, stop the loop gracefully.
    print("\n🛑 Stopped by user.")

finally: # Release the webcam and close all OpenCV windows after the program finishes.
    cap.release()
    cv2.destroyAllWindows()

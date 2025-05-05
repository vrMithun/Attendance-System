import cv2
from deepface import DeepFace
import pandas as pd
from datetime import datetime
import os

# Path to known faces database
db_path = "known_faces"

# Initialize webcam
cap = cv2.VideoCapture(0)

# Create attendance file if not exists
if not os.path.exists("attendance.csv"):
    with open("attendance.csv", "w") as f:
        f.write("Name,Time\n")

# Track already marked names
marked = set()

print("📸 Starting face recognition. Press 'q' to quit...")

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("❌ Failed to grab frame.")
            break

        # Copy of frame for drawing
        display_frame = frame.copy()

        try:
            # Face recognition
            results = DeepFace.find(
                img_path=frame,
                db_path=db_path,
                detector_backend='opencv',  # or 'mediapipe'
                enforce_detection=False,
                silent=True
            )

            if len(results) > 0 and not results[0].empty:
                identity_path = results[0].iloc[0]['identity']
                name = os.path.basename(os.path.dirname(identity_path))

                # Optional: Draw face rectangle using OpenCV face detector
                face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(gray, 1.3, 5)

                for (x, y, w, h) in faces:
                    cv2.rectangle(display_frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                    cv2.putText(display_frame, name, (x, y - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

                if name not in marked:
                    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    with open("attendance.csv", "a") as f:
                        f.write(f"{name},{now}\n")
                    marked.add(name)
                    print(f"✅ Marked attendance for: {name} at {now}")
                else:
                    print(f"👀 {name} already marked.")
            else:
                print("😕 Unknown Face")

        except Exception as e:
            print("⚠️ Error:", str(e))

        # Show webcam frame
        cv2.imshow("Face Recognition", display_frame)

        # Exit on 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    print("\n🛑 Stopped by user.")

finally:
    cap.release()
    cv2.destroyAllWindows()

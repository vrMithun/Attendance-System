# Attendance System using Face Recognition

This project implements an **Attendance System** using **Face Recognition** and stores the attendance in a CSV file. It uses OpenCV and DeepFace for real-time face detection and recognition from your webcam.

## Features:
- **Face Recognition:** Recognizes faces using your webcam.
- **Attendance Marking:** Marks attendance for recognized individuals.
- **CSV Export:** Saves the attendance log with name and timestamp to a CSV file (`attendance.csv`).
- **Real-time Display:** Displays the webcam feed with face detection.

---

## Requirements:

The project requires the following libraries:

- `opencv-python` - For accessing the webcam and processing the video stream.
- `deepface` - For facial recognition and comparison.
- `tensorflow` - Backend for DeepFace.
- `pandas` - For handling attendance data and writing to CSV.
- `numpy` - For array operations.
- `face_recognition` - Used for face recognition.

You can install all the required libraries using the `requirements.txt` file.

---

## Installation Steps:

### 1. Set Up Python Virtual Environment (Recommended)

To avoid version conflicts, it's best to set up a virtual environment for this project. Follow these steps:

#### a. Install Python:
Make sure you have Python installed. You can download Python from [here](https://www.python.org/downloads/).

#### b. Create a Virtual Environment:
Navigate to the project folder and create a virtual environment:
```bash
python -m venv venv

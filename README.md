# 🎓 Attendance System using Face Recognition

This project implements an **Attendance System** using **Face Recognition** and stores the attendance in a CSV file. It uses **OpenCV**, **DeepFace**, and other Python libraries for real-time face detection and recognition via your webcam.

---

## 🚀 Features

- 🔍 **Face Recognition:** Recognizes faces in real time using your webcam.
- 📝 **Attendance Marking:** Automatically marks attendance for recognized individuals.
- 📁 **CSV Export:** Stores attendance with name and timestamp in `attendance.csv`.
- 🎥 **Live Webcam Display:** Shows real-time video feed with face detection boxes.

---

## 📦 Requirements

Install the following Python libraries:

- `opencv-python` – Webcam access and video processing.
- `deepface` – Facial recognition and analysis.
- `tensorflow` – Backend for DeepFace.
- `pandas` – Attendance data manipulation and CSV writing.
- `numpy` – Array operations.
- `face_recognition` – Face detection and encoding.

> ✅ You can install all dependencies using the `requirements.txt` file.

---

## ⚙️ Installation Steps

### 1. 📁 Set Up a Python Virtual Environment (Recommended)

Avoid version conflicts by using a virtual environment.

#### a. 🔽 Install Python

Download and install Python from [python.org](https://www.python.org/downloads/).

#### b. 🛠️ Create a Virtual Environment

Navigate to your project directory and run:

```bash
python -m venv venv
```

#### c. 🚀 Activate the Virtual Environment

**On Windows:**

```bash
.env\Scriptsctivate
```

**On macOS/Linux:**

```bash
source venv/bin/activate
```

When active, your terminal will show the virtual environment name like `(venv)`.

---

### 2. 📥 Install Dependencies

With the virtual environment activated, install dependencies:

```bash
pip install -r requirements.txt
```

This will install all required packages listed in the `requirements.txt` file.

---

## ▶️ Usage

1. Ensure your webcam is connected.
2. Run the main script:
   ```bash
   python attendance_system.py
   ```
3. The webcam feed will display, and faces will be detected and recognized in real time.
4. Recognized faces will be logged into `attendance.csv` with the current timestamp.

---

## 📂 Output

- **`attendance.csv`** – A file that stores attendance records in the format:

  ```
  Name, Time
  John Doe, 2025-04-20 10:23:45
  ```

---

## 🧠 Notes

- Ensure good lighting for better face detection accuracy.
- You can improve accuracy by training with higher-quality face images.
- Make sure to test the system with a few known faces for verification.

---

## 🤝 Contributing

Want to improve the project? Feel free to fork and contribute!

1. Fork the repo
2. Create a new branch (`git checkout -b feature/feature-name`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/feature-name`)
5. Open a Pull Request

---

## 📝 License

This project is open source and free to use under the [MIT License](LICENSE).

---

## 📸 Demo (Optional)

You can add demo screenshots or screen recordings here to showcase the system in action.

---

Made with ❤️ using OpenCV, DeepFace, and Python.

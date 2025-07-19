# FcaeRecognitionAttendanceSystemUsingFlask
A real-time Face Recognition Attendance System built with Flask, OpenCV, and Firebase. Automatically detects and recognizes faces, marks attendance with timestamps, and provides a simple web interface for management.
# Face Recognition Attendance System Using Flask

A real-time **Face Recognition Attendance System** built with **Flask**, **OpenCV**, **face_recognition**, and **Firebase**.  
It detects and recognizes faces using a webcam, marks attendance automatically with timestamps, and stores data in **Firebase Realtime Database**.

---

## Features
- Real-time face detection and recognition  
- Automatic attendance marking with timestamps  
- Firebase Realtime Database and Storage integration  
- Secure face encodings for multiple users  
- Simple web interface built with Flask  

---

## Tech Stack
- **Backend:** Flask (Python)
- **Computer Vision:** OpenCV, face_recognition
- **Database:** Firebase Realtime Database, Firebase Storage
- **Frontend:** HTML, CSS, JavaScript

---

## Project Structure
FaceRecognitionAttendanceSystem/
│
├── app.py # Main Flask application
├── EncodeGenerator.py # Generates and saves face encodings
├── static/ # Static files (CSS, JS, images)
├── templates/ # HTML templates
├── AttendanceImages/ # Images of registered users
└── README.md # Project documentation


---

## Installation

### 1. Clone the repository
bash
git clone https://github.com/yourusername/FaceRecognitionAttendanceSystem.git
cd FaceRecognitionAttendanceSystem

2. Create a virtual environment and activate it
bash
Copy
Edit
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt

4. Setup Firebase
Create a Firebase project.

Enable Realtime Database and Storage.

Download your serviceAccountKey.json and place it in the project root.

5. Run the application
bash
Copy
Edit
python app.py
Open your browser and go to http://127.0.0.1:5000.

Usage
Add images of users in AttendanceImages/.

Run EncodeGenerator.py to generate encodings.

Start the Flask server with app.py.

The system will mark attendance automatically when a registered face appears.

Use Cases
Educational institutions

Offices and organizations

Events and seminars



Author
Bhabani S Biswal

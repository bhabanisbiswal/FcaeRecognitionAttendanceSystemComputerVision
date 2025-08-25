---

# 🎓 Face Recognition Attendance System

This project is a **real-time face recognition attendance system** that automates the process of marking attendance using a webcam.
It combines **computer vision** 👁️ and **AI-based face recognition** 🤖 with cloud integration for seamless attendance tracking.

---

## ✨ Features

### 🖥 Real-Time Recognition

* 🎥 Captures live video from a webcam.
* 👤 Detects and recognizes faces using **dlib’s deep learning model**.
* 🔄 Updates student information dynamically.

### 📊 Smart Attendance Management

* ⏳ Prevents duplicate attendance within a time interval (e.g., 30 sec).
* 🖼 Displays student card with **photo, name, course, and attendance count**.
* 🔒 Data stored securely in **Firebase Realtime Database**.

### ☁ Cloud Integration

* ☁️ Attendance records are updated in real-time on Firebase.
* 📂 Student images stored in **Firebase Storage**.

---

## 🛠 Tech Stack

* 🐍 **Python**
* 🎥 **OpenCV** – Live video and image processing.
* 🤖 **face\_recognition** – Face encoding & recognition.
* 🔢 **NumPy** – Data handling.
* 🖼 **cvzone** – Custom UI elements.
* ☁ **Firebase Realtime Database & Storage** – Cloud data management.
* 📦 **pickle** – Saves & loads face encodings.

---

## 📂 Project Structure

```
Face-Recognition-Attendance/
│── EncodeFile.py           # Prepares face encodings for known students
│── main.py                 # Main attendance system (real-time recognition)
│── serviceAccountKey.json  # Firebase credentials
│── Resources/              # UI assets (background, modes, etc.)
│── Images/                 # Student face images
│── EncodeFile.p            # Saved face encodings
│── README.md               # Project documentation
```

---

## ⚙ How It Works

### 1️⃣ Face Encoding

* Known student images are encoded using **face\_recognition**.
* Encodings are stored in a `.p` file for fast lookup.

### 2️⃣ Real-Time Detection

* Webcam captures live feed.
* Faces are detected & compared with stored encodings.

### 3️⃣ Attendance Marking

* If a student is recognized:

  * ✅ Attendance is marked in Firebase.
  * ✅ Student details (name, course, attendance count, last login) are displayed.
* Duplicate attendance is prevented within a set interval.

---

## 📥 Installation

1. 📂 Clone the repository:

```bash
git clone https://github.com/bhabanisbiswal/Face-Recognition-Attendance.git
```

2. 📁 Navigate into the folder:

```bash
cd Face-Recognition-Attendance
```

3. 📦 Install dependencies:

```bash
pip install opencv-python face-recognition numpy cvzone firebase-admin
```

4. 🔑 Add your Firebase credentials:

* Place `serviceAccountKey.json` in the root folder.
* Update the database URL inside `main.py`.

5. ▶ Run the system:

```bash
python main.py
```

---

## 🚀 Usage

* 🎥 Ensure your webcam is connected.
* 🖼 Add student images in the `Images/` folder before encoding.
* ⚡ Run `EncodeFile.py` to generate encodings.
* ▶ Start `main.py` to begin real-time attendance.
* ❌ Press **any key** to exit the system.

---

## 📸 Demo

![UI Demo 1](https://github.com/bhabanisbiswal/FcaeRecognitionAttendanceSystemComputerVision/blob/8e996df90f97a23b61ab005202f9fb3841f04a53/sample1.png)

![UI Demo 2](https://github.com/bhabanisbiswal/FcaeRecognitionAttendanceSystemComputerVision/blob/8e996df90f97a23b61ab005202f9fb3841f04a53/sample2.png)


---

## 🔮 Future Improvements

* 📱 Mobile app for attendance tracking.
* 🌍 Multi-database support (MySQL, MongoDB).
* 🖼 Enhanced UI with advanced animations.
* 🔊 Voice feedback on recognition.

---

## 👤 Author

**Bhabani S Biswal** – Python & AI/ML Developer, Student at GIET University
📧 Email: [bhabanibiswalb17@gmail.com](mailto:bhabanibiswalb17@gmail.com)
🔗 GitHub: [Bhabani S Biswal](https://github.com/bhabanisbiswal)

---


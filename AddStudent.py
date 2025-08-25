import firebase_admin
from firebase_admin import credentials, db
import cv2
import os
from datetime import datetime

# Initialize Firebase
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendancerealtimeda-39bfc-default-rtdb.firebaseio.com/"
})

# Folder where images are stored locally
images_folder = "Images"
os.makedirs(images_folder, exist_ok=True)

# === Step 1: Input student details ===
student_id = input("Enter Student ID (or type 'exit' to quit): ").strip()
if student_id.lower() == "exit":
    print("Program exited.")
    exit()

# Check if this student ID already exists
ref = db.reference('Students')
if ref.child(student_id).get():
    print(f"Student ID {student_id} already exists! No new data added.")
    exit()

name = input("Enter Student Name: ")
major = input("Enter Major: ")
starting_year = int(input("Enter Starting Year: "))
year = int(input("Enter Current Year: "))
standing = input("Enter Standing (e.g., G, B, etc.): ")

# === Step 2: Capture or select student image ===
choice = input("Capture image from webcam? (y/n): ").strip().lower()

if choice == 'y':
    cap = cv2.VideoCapture(0)
    print("Press 's' to save the image or 'q' to cancel.")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture image.")
            break

        cv2.imshow("Capture Student Image", frame)
        key = cv2.waitKey(1)

        if key & 0xFF == ord('s'):
            img_path = os.path.join(images_folder, f"{student_id}.png")
            cv2.imwrite(img_path, frame)
            print(f"Image saved as {img_path}")
            break
        elif key & 0xFF == ord('q'):
            print("Image capture cancelled.")
            break

    cap.release()
    cv2.destroyAllWindows()
else:
    image_path = input("Enter path to existing image: ")
    img = cv2.imread(image_path)
    if img is not None:
        save_path = os.path.join(images_folder, f"{student_id}.png")
        cv2.imwrite(save_path, img)
        print(f"Image saved as {save_path}")
    else:
        print("Invalid image path. Exiting...")
        exit()

# === Step 3: Add student data to Realtime Database ===
student_data = {
    "name": name,
    "major": major,
    "starting_year": starting_year,
    "total_attendance": 0,
    "standing": standing,
    "year": year,
    "last_attendance_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
}

ref.child(student_id).set(student_data)
print(f"Student {name} (ID: {student_id}) added successfully without overwriting existing data!")


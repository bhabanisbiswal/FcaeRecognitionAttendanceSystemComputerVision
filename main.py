import os
import pickle
import numpy as np
import cv2
import face_recognition
import cvzone
import firebase_admin
from firebase_admin import credentials, db
from datetime import datetime, timedelta

# Initialize Firebase
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendancerealtimeda-39bfc-default-rtdb.firebaseio.com/"
})

# Setup camera
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

# Load background and modes
imgBackground = cv2.imread('Resources/background.png')
folderModePath = 'Resources/Modes'
imgModeList = [cv2.imread(os.path.join(folderModePath, path)) for path in sorted(os.listdir(folderModePath))]

print("Loading Encode File ...")
with open('EncodeFile.p', 'rb') as file:
    encodeListKnown, studentIds = pickle.load(file)
print("Encode File Loaded")

modeType = 0  # 0 - active, 1 - info, 2 - marked, 3 - already marked
id = -1
imgStudent = []
studentInfo = None
display_start_time = None
marked_start_time = None

while True:
    success, img = cap.read()
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    faceCurFrame = face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition.face_encodings(imgS, faceCurFrame)

    imgBackground[162:162 + 480, 55:55 + 640] = img

    # --- Time-based transitions ---
    if modeType == 1 and display_start_time and (datetime.now() - display_start_time).total_seconds() > 5:
        modeType = 2  # Show marked
        marked_start_time = datetime.now()

    if modeType == 2 and marked_start_time and (datetime.now() - marked_start_time).total_seconds() > 2:
        modeType = 0  # Reset to active
        id = -1
        studentInfo = None
        imgStudent = []
        display_start_time = None
        marked_start_time = None

    if modeType == 3 and marked_start_time and (datetime.now() - marked_start_time).total_seconds() > 2:
        modeType = 0  # Reset to active
        id = -1
        studentInfo = None
        imgStudent = []
        marked_start_time = None

    # --- Display modes ---
    if 0 <= modeType < len(imgModeList):
        imgBackground[44:44 + 633, 808:808 + 414] = imgModeList[modeType]

    # --- Face detection ---
    if faceCurFrame and modeType == 0:
        for encodeFace, faceLoc in zip(encodeCurFrame, faceCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
            matchIndex = np.argmin(faceDis)

            if matches[matchIndex]:
                id = studentIds[matchIndex]

                studentInfo = db.reference(f'Students/{id}').get()
                imgPath = f"Images/{id}.png"
                imgStudent = cv2.imread(imgPath) if os.path.exists(imgPath) else np.zeros((216, 216, 3), dtype=np.uint8)

                last_time = datetime.strptime(studentInfo['last_attendance_time'], "%Y-%m-%d %H:%M:%S")
                seconds_elapsed = (datetime.now() - last_time).total_seconds()

                if seconds_elapsed > 30:
                    # Update attendance
                    ref = db.reference(f'Students/{id}')
                    studentInfo['total_attendance'] += 1
                    ref.child('total_attendance').set(studentInfo['total_attendance'])
                    ref.child('last_attendance_time').set(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

                    modeType = 1  # Show info page
                    display_start_time = datetime.now()
                else:
                    # Already marked
                    modeType = 3  # Show already marked page
                    marked_start_time = datetime.now()

    # --- Info page rendering ---
    if modeType == 1 and studentInfo:
        cv2.putText(imgBackground, str(studentInfo['total_attendance']), (861, 125),
                    cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1)
        cv2.putText(imgBackground, str(studentInfo['major']), (1006, 550),
                    cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
        cv2.putText(imgBackground, str(id), (1006, 493),
                    cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
        cv2.putText(imgBackground, str(studentInfo['standing']), (910, 625),
                    cv2.FONT_HERSHEY_COMPLEX, 0.6, (100, 100, 100), 1)
        cv2.putText(imgBackground, str(studentInfo['year']), (1025, 625),
                    cv2.FONT_HERSHEY_COMPLEX, 0.6, (100, 100, 100), 1)
        cv2.putText(imgBackground, str(studentInfo['starting_year']), (1125, 625),
                    cv2.FONT_HERSHEY_COMPLEX, 0.6, (100, 100, 100), 1)

        (w, h), _ = cv2.getTextSize(studentInfo['name'], cv2.FONT_HERSHEY_COMPLEX, 1, 1)
        offset = (414 - w) // 2
        cv2.putText(imgBackground, str(studentInfo['name']), (808 + offset, 445),
                    cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 50), 1)

        imgBackground[175:175 + 216, 909:909 + 216] = imgStudent

    cv2.imshow("Face Attendance", imgBackground)
    exit_key=cv2.waitKey(1)
    if exit_key !=-1:
        break
cap.release()
cv2.destroyAllWindows()



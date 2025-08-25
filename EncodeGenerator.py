import cv2
import face_recognition
import pickle
import os
import numpy as np

# Path to the folder containing student images
folderPath = 'Images'
pathList = os.listdir(folderPath)
print("Found image files:", pathList)

imgList = []
studentIds = []

for path in pathList:
    imgPath = os.path.join(folderPath, path)
    img = cv2.imread(imgPath)

    if img is None:
        print(f"Skipped {path}: Cannot read file.")
        continue

    # Check if image is in the right format (8-bit, 3-channel BGR)
    if img.dtype != np.uint8 or len(img.shape) != 3 or img.shape[2] != 3:
        print(f"Fixing {path}: Unsupported format detected.")
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert to RGB
        fixed_path = os.path.join(folderPath, path)
        cv2.imwrite(fixed_path, img)
        print(f"Saved fixed image as {fixed_path}")

    imgList.append(img)
    studentIds.append(os.path.splitext(path)[0])

print("Student IDs detected:", studentIds)

def findEncodings(imagesList):
    encodeList = []
    for img, sid in zip(imagesList, studentIds):
        rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encodings = face_recognition.face_encodings(rgb_img)
        if encodings:
            encodeList.append(encodings[0])
            print(f"Encoding generated for {sid}")
        else:
            print(f"No face found in {sid}, skipped.")
    return encodeList

print("Encoding Started ...")
encodeListKnown = findEncodings(imgList)
encodeListKnownWithIds = [encodeListKnown, studentIds]
print("Encoding Complete")

# Save the encodings
with open("EncodeFile.p", 'wb') as file:
    pickle.dump(encodeListKnownWithIds, file)

print("File Saved as EncodeFile.p")

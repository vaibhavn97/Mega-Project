import urllib.request
import numpy as np
import cv2
import face_recognition
import os


path = 'Images'
images = []
className = []
myList = os.listdir(path)

for i in myList:
    img = cv2.imread(f"{path}/{i}")
    images.append(img)
    className.append(os.path.splitext(i)[0])

print(className)

def find_encodings(images):
    encodedImages = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodedImages.append(encode)
    return encodedImages

encodedListKnowned = find_encodings(images)




# Replace the URL with the IP camera's stream URL
url = 'http://192.168.243.3/cam-hi.jpg'
cv2.namedWindow("live Cam Testing", cv2.WINDOW_AUTOSIZE)


# Create a VideoCapture object
cap = cv2.VideoCapture(url)

# Check if the IP camera stream is `opened` successfully
if not cap.isOpened():
    print("Failed to open the IP camera stream")
    exit()

# Read and display video frames
while True:
    # Read a frame from the video stream
    img_resp=urllib.request.urlopen(url)
    imgnp=np.array(bytearray(img_resp.read()),dtype=np.uint8)
    #ret, frame = cap.read()
    im = cv2.imdecode(imgnp,-1)
    imgS = cv2.resize(im, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)

    currFacesLoc = face_recognition.face_locations(imgS)
    print(currFacesLoc)
    encodedCurrFrame = face_recognition.face_encodings(imgS, currFacesLoc)
    for encodedFace, faceLoc in zip(encodedCurrFrame, currFacesLoc):
        print("I am in for loop")
        matches = face_recognition.compare_faces(encodedListKnowned, encodedFace)
        faceDis = face_recognition.face_distance(encodedListKnowned, encodedFace)
        matchIndex = np.argmin(faceDis)
        if matches[matchIndex]:
            name = className[matchIndex]
            print(name)
            y1, x2, y2, x1 = faceLoc
            y1 = y1*4
            y2 = y2*4
            x1 = x1*4
            x2 = x2*4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 255), 2)
            cap.release()
            break
        else :
            print("Not Matched")
    cv2.imshow('live Cam Testing',im)
    key=cv2.waitKey(5)
    if key==ord('q'):
        break
    

cap.release()
cv2.destroyAllWindows()
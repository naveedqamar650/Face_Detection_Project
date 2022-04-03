import cv2
import numpy as np
import sqlite3

faceDetect = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0);
rec = cv2.face.LBPHFaceRecognizer_create()
rec.read("C:/Users/navee/PycharmProjects/pythonProject3/image-detection/recognizer/trainningData.yml")

fontface = cv2.FONT_HERSHEY_SIMPLEX
fontscale = 0.5
fontcolor = (0, 255, 0)


def getProfile(id):
    conn = sqlite3.connect("FaceBase.db")
    cmd = "SELECT * FROM People WHERE ID=" + str(id)
    cursor = conn.execute(cmd)
    profile = None
    for row in cursor:
        profile = row
    conn.close()
    return profile


while (True):
    ret, img = cam.read();
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceDetect.detectMultiScale(gray, 1.3, 5);
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        id, conf = rec.predict(gray[y:y + h, x:x + w])
        print(id)
        profile = getProfile(id)
        if (profile != None):
            cv2.putText(img, "Name : " + str(profile[1]), (x, y + h + 20), fontface, fontscale, fontcolor);
            cv2.putText(img, "Age : " + str(profile[2]), (x, y + h + 45), fontface, fontscale, fontcolor);
            cv2.putText(img, "Gender : " + str(profile[3]), (x, y + h + 70), fontface, fontscale, fontcolor);
    cv2.imshow("Face", img);
    if (cv2.waitKey(1) == ord('q')):
        break;
cam.release()
cv2.destroyAllWindows()

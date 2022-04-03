import os
import cv2
import numpy as np
from PIL import Image

recognizer = cv2.face.LBPHFaceRecognizer_create()
path = 'C:/Users/navee/PycharmProjects/pythonProject3/image-detection/dataSet'


def getImagesWithID(path):
    imagepaths = [os.path.join(path, f) for f in os.listdir(path)]
    faces = []
    IDs = []
    for imagepath in imagepaths:
        if ".DS_Store" in imagepath:
            print("Junk!")
        else:
            faceImg = Image.open(imagepath).convert('L');
            faceNp = np.array(faceImg, 'uint8')
            ID = int(os.path.split(imagepath)[-1].split('.')[1])
            faces.append(faceNp)
            IDs.append(ID)
            cv2.imshow("training", faceNp)
            cv2.waitKey(10)
    return np.array(IDs), faces


IDs, faces = getImagesWithID(path)
recognizer.train(faces, IDs)
recognizer.save('C:/Users/navee/PycharmProjects/pythonProject3/image-detection/recognizer/trainningData.yml')
cv2.destroyAllWindows()

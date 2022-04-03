import cv2
import numpy as np
import sqlite3
from tkinter import *

faceDetect = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)


def face():
    sampleNum = 0
    # Loop
    while (True):

        # Read the video frame
        ret, img = cam.read()

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Detect frames of different sizes, list of faces rectangles
        faces = faceDetect.detectMultiScale(gray, 1.3, 5)

        # Loops for each faces
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

            # Incrementing sample number
            sampleNum = sampleNum + 1

            # Saving the captured face in the dataset folder
            cv2.imwrite(
                "C:/Users/navee/PycharmProjects/pythonProject3/image-detection/dataSet/User." + id.get() + '.' + str(
                    sampleNum) + ".jpg", gray[y:y + h, x:x + w])

            # Display the video frame with the bounded rectangle
            cv2.imshow('Face', img)

        # wait for 100 miliseconds & If 'q' is pressed, close program
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break

        # break if the sample number is morethan 20
        elif sampleNum > 30:
            break
    # Stop the camera
    cam.release()
    # Close all windows
    cv2.destroyAllWindows()


def insertOrUpdate():
    conn = sqlite3.connect("FaceBase.db")
    cmd = "SELECT * FROM People WHERE ID=" + str(id.get())
    cursor = conn.execute(cmd)
    isRecordExist = 0
    for row in cursor:
        isRecordExist = 1
    if (isRecordExist == 1):
        cmd = "UPDATE People SET Name=" + str(name.get()) + "WHERE ID=" + str(id.get())
        cmd2 = "UPDATE People SET Age=" + str(age.get()) + "WHERE ID=" + str(id.get())
        cmd3 = "UPDATE People SET Gender=" + str(gen.get()) + "WHERE ID=" + str(id.get())
        conn.execute(cmd)
        face()
    else:
        params = (id.get(), name.get(), age.get(), gen.get())
        cmd = "INSERT INTO People(ID, Name, Age, Gender) Values(?, ?, ?, ?)"
        cmd2 = ""
        cmd3 = ""
        cmd4 = ""
        conn.execute(cmd, params)
        face()

    conn.execute(cmd2)
    conn.execute(cmd3)
    conn.execute(cmd4)
    conn.commit()
    conn.close()


def Loginform():
    global login_screen
    login_screen = Tk()
    # setting height and width of screen
    login_screen.geometry("500x250")
    # declaring variable
    global message
    global id
    global name
    global age
    global gen

    id = StringVar()
    name = StringVar()
    age = StringVar()
    gen = StringVar()
    message = StringVar()
    # Creating layout of login form
    Label(login_screen, width="300", text="Please Enter Details Below", bg="black", fg="white").pack()
    # ID Label
    Label(login_screen, text="ID * ").place(x=20, y=40)
    # ID textbox
    Entry(login_screen, textvariable=id).place(x=90, y=42)
    # name Label
    Label(login_screen, text="NAME * ").place(x=20, y=80)
    # name textbox
    Entry(login_screen, textvariable=name).place(x=90, y=82)
    # age Label
    Label(login_screen, text="AGE * ").place(x=20, y=120)
    # age textbox
    Entry(login_screen, textvariable=age).place(x=90, y=122)
    # gen Label
    Label(login_screen, text="GENDER * ").place(x=20, y=160)
    # gen textbox
    Entry(login_screen, textvariable=gen).place(x=90, y=162)
    # Label for displaying login status[success/failed]
    Label(login_screen, text="", textvariable=message).place(x=95, y=180)
    # Login button
    Button(login_screen, text="Add Student", width=10, height=1, bg="black", fg="white", command=insertOrUpdate).place(
        x=105, y=190)
    login_screen.mainloop()


# calling function Loginform
Loginform()

# Id = input('Enter User Id')
# name = input('Enter User Name')
# age = input('Enter User Age')
# gen = input('Enter User Gender')
# insertOrUpdate(Id, name, age, gen)
# sampleNum = 0
# # Loop
# while (True):
#
#     # Read the video frame
#     ret, img = cam.read()
#
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
#     # Detect frames of different sizes, list of faces rectangles
#     faces = faceDetect.detectMultiScale(gray, 1.3, 5)
#
#     # Loops for each faces
#     for (x, y, w, h) in faces:
#         cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
#
#         # Incrementing sample number
#         sampleNum = sampleNum + 1
#
#         # Saving the captured face in the dataset folder
#         cv2.imwrite("C:/Users/navee/PycharmProjects/pythonProject3/image-detection/dataSet/User." + Id + '.' + str(
#             sampleNum) + ".jpg", gray[y:y + h, x:x + w])
#
#         # Display the video frame with the bounded rectangle
#         cv2.imshow('Face', img)
#
#     # wait for 100 miliseconds & If 'q' is pressed, close program
#     if cv2.waitKey(100) & 0xFF == ord('q'):
#         break
#
#     # break if the sample number is morethan 20
#     elif sampleNum > 30:
#         break

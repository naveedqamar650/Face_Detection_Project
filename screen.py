import os
from tkinter import *
from PIL import ImageTk, Image
import pyttsx3


def text_to_speech(user_text):
    engine = pyttsx3.init()
    engine.say(user_text)
    engine.runAndWait()


# print(1)
text_to_speech('Authentication Successful!')
text_to_speech('Welcome!')


def quit(*args):
    root.destroy()


root = Tk()
root.attributes("-fullscreen", False)
root.geometry("1386x750")
root.configure(background='black')
root.bind("<Escape>", quit)
root.bind("x", quit)

Label(root, text="Welcome to the Facial Recognition", bg="black", fg="yellow",
      font=("arial", 56)).pack()

ri = Image.open("register.png")
r = ImageTk.PhotoImage(ri)
label1 = Label(root, image=r)
label1.image = r
label1.place(x=180, y=300)

ai = Image.open("attendance.png")
a = ImageTk.PhotoImage(ai)
label2 = Label(root, image=a)
label2.image = a
label2.place(x=980, y=300)

vi = Image.open("verifyy.png")
v = ImageTk.PhotoImage(vi)
label3 = Label(root, image=v)
label3.image = v
label3.place(x=600, y=300)


def add_new_face():
    os.system('facedata.py')


def train():
    os.system('facetrain.py')


def recognition():
    os.system('facerecognisation.py')


Button(root, text="Add New Student", bd=10,
       command=add_new_face, font=('times new roman', 12), bg="black", fg="yellow", height=5).place(x=225, y=570)

Button(root, text="Train Model", bd=10,
       command=train, font=('times new roman', 12), bg="black", fg="yellow", height=5).place(x=660, y=570)

Button(root, text="Recognition", bd=10,
       command=recognition, font=('times new roman', 12), bg="black", fg="yellow", height=5).place(x=1080, y=570)

Button(root, text="EXIT", bd=10,
       command=quit, font=('times new roman', 12), bg="black", fg="yellow", height=2, width=10).place(x=637, y=700)

# if __name__ == '__main__':
root.mainloop()

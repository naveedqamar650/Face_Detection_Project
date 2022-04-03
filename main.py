# Import
from tkinter import *
import os


# FRAME
def quit(*args):
    root.destroy()


root = Tk()
root.attributes("-fullscreen", False)
root.configure(background='black')
root.bind("<Escape>", quit)
root.bind("x", quit)


# Login Page
def Login(event=None):
    if USERNAME.get() == "" or PASSWORD.get() == "":
        lbl_text.config(text="Please complete the required field!", fg="red")
    else:
        if USERNAME.get() == 'admin' and PASSWORD.get() == 'admin':
            screen()
            USERNAME.set("")
            PASSWORD.set("")
            lbl_text.config(text="")
        else:
            lbl_text.config(text="Invalid username or password", fg="red")
            USERNAME.set("")
            PASSWORD.set("")


def screen():
    os.system('screen.py')


# Back Button
def Back():
    screen().destroy()
    Login().destroy()
    root.deiconify()


# ==============================VARIABLES======================================
USERNAME = StringVar()
PASSWORD = StringVar()

# ==============================FRAMES=========================================
Top = Frame(root, bd=10, relief=RIDGE)
Top.pack(side=TOP, fill=X)
Faltu = Frame(root, height=500, relief=RIDGE)
Faltu.pack(side=TOP, fill=X, ipady=50, ipadx=200)
Form = Frame(root, height=50, bd=30)
Form.pack(side=TOP, pady=20)

# ==============================LABELS=========================================
lbl_title = Label(Top, text="Face Recognition System", bg="black", fg="green", font=('Helvetica', 64))
lbl_title.pack(fill=BOTH, expand=1)
cre = Label(Faltu, text="Enter your credentials: ", fg="green", bg="black", font=('Verdana', 20))
cre.pack(fill=BOTH, expand=1)
lbl_username = Label(Form, text="Username:", font=('arial', 14), bd=15)
lbl_username.grid(row=0, sticky="e")
lbl_password = Label(Form, text="Password:", font=('arial', 14), bd=15)
lbl_password.grid(row=1, sticky="e")
lbl_text = Label(Form)
lbl_text.grid(row=2, columnspan=2)

# ==============================ENTRY WIDGETS==================================
username = Entry(Form, textvariable=USERNAME, font=(14))
username.grid(row=0, column=1)
password = Entry(Form, textvariable=PASSWORD, show="*", font=(14))
password.grid(row=1, column=1)

# ==============================BUTTON WIDGETS=================================
btn_login = Button(Form, text="Login", width=45, command=Login)
btn_login.grid(pady=25, row=3, columnspan=2)
btn_login.bind("<Return>", Login)

# ==============================INITIALIATION==================================
# if __name__ == '__main__':
root.mainloop()

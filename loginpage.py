from tkinter import *
import os

def delete3():
    screen4.destroy()

def delete4():
    screen5.destroy()

def view_notes1():
    filename1 = new_filename1.get()
    data = open(filename1, "r")
    data1 = data.read()
    screen12=Toplevel(screen)
    screen12.title("Notes")
    screen12.geometry("400x400")
    Label(screen12, text = data1).pack()
    #Label(screen12,text = all_files).pack()



def view_notes():
    global new_filename1
    screen11=Toplevel(screen)
    screen11.title("Info")
    screen11.geometry("250x250")
    all_files = os.listdir()
    Label(screen11,text="Please use one of the filename below").pack()
    Label(screen11,text = all_files).pack()
    new_filename1 = StringVar()
    Entry(screen11,textvariable=new_filename1).pack()
    Button(screen11,command=view_notes1,text="OK").pack()



def saved():
    screen10=Toplevel(screen)
    screen10.title("saved")
    screen10.geometry("100x100")
    Label(screen10,text="saved").pack()

def save():
    filename=raw_filename.get()
    notes=raw_notes.get()
    data = open(filename,"w")
    data.write(notes)
    data.close()
    saved()

def create_node():
    global raw_filename
    raw_filename = StringVar()
    global raw_notes
    raw_notes = StringVar()

    screen9=Toplevel(screen)
    screen9.title("Info")
    screen9.geometry("300x300")
    Label(screen9,text="Please enter the file name:").pack()
    Entry(screen9,textvariable=raw_filename).pack()
    Label(screen9,text="Please enter the file notes:").pack()
    Entry(screen9,textvariable=raw_notes).pack()
    Button(screen9,text = "save",command = save).pack()

def delete_notes():
    global new_filename2
    screen13=Toplevel(screen)
    screen13.title("Info")
    screen13.geometry("250x250")
    all_files = os.listdir()
    Label(screen13,text="Please use one of the filename below").pack()
    Label(screen13,text = all_files).pack()
    new_filename2 = StringVar()
    Entry(screen13,textvariable=new_filename2).pack()
    Button(screen13,command=delete_notes1,text="OK").pack()

def delete_notes1():
    filename3 = new_filename2.get()
    os.remove(filename3)
    screen14 = Toplevel(screen)
    screen14.title("Notes")
    screen14.geometry("400x400")
    Label(screen14, text = filename3+" removed").pack()






def session():
    global screen8
    screen8=Toplevel(screen)
    screen8.title("dashboard")
    screen8.geometry("400x400")
    Label(screen8,text="Welcome to the dashboard",bg="red", font=("Times New Roman", 25)).pack()
    Button(screen8,text="create Note",width=30,height=2,command=create_node).pack()
    Label(screen8, text="").pack()
    Button(screen8,text="View Note",width=30,height=2,command=view_notes).pack()
    Label(screen8, text="").pack()
    Button(screen8,text="Delete Note",width=30,height=2,command=delete_notes).pack()
    Label(screen8, text="").pack()

def login_sucess():
    session()
    '''
    global screen3
    screen3 = Toplevel(screen)
    screen3.title("Success")
    screen3.geometry("250x150")
    Label(screen3, text="Login Success").pack()
    Button(screen3, text="OK", command=delete2).pack()
    '''


def password_not_recognised():
    global screen4
    screen4 = Toplevel(screen)
    screen4.title("Success")
    screen4.geometry("250x150")
    Label(screen4, text="Login Failed Incorrect Password").pack()
    Button(screen4, text="OK", command=delete3).pack()


def user_not_found():
    global screen5
    screen5 = Toplevel(screen)
    screen5.title("Success")
    screen5.geometry("250x150")
    Label(screen5, text="Login Failed Incorrect Username").pack()
    Button(screen5, text="OK", command=delete4).pack()


def register_user():
    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write(username_info + "\n")
    username_entry.delete(0, END)
    file.write(password_info + "\n")
    password_entry.delete(0, END)
    file.close()
    Label(screen1, text="Registration Successfully Done", fg="green", font=("calibri", 13)).pack()


def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register Form")
    screen1.geometry("300x250")
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(screen1, text="Enter the detail").pack()
    Label(screen1, text="").pack()
    Label(screen1, text="UserName", width=30, height=2).pack()
    username_entry = Entry(screen1, textvariable=username)
    username_entry.pack()
    Label(screen1, text="").pack()
    Label(screen1, text="PassWord", width=30, height=2).pack()
    password_entry = Entry(screen1, textvariable=password)
    password_entry.pack()
    Label(screen1, text="").pack()
    Button(screen1, text="Register", width=30, height=2, command=register_user).pack()


def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)
    list_of_item = os.listdir()
    # print(list_of_item)
    if username1 in list_of_item:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()

        else:
            password_not_recognised()
    else:
        user_not_found()
    file1.close()


def login():
    global screen2
    global username_verify
    global password_verify
    global username_entry1
    global password_entry1
    screen2 = Toplevel(screen)
    screen2.title("Login Page")
    screen2.geometry("300x250")
    Label(screen2, text="Please Enter the detail to login..").pack()
    Label(screen2, text="").pack()

    username_verify = StringVar()
    password_verify = StringVar()

    Label(screen2, text="Username").pack()
    username_entry1 = Entry(screen2, textvariable=username_verify)
    username_entry1.pack()
    Label(screen2, text="").pack()
    password_entry1 = Entry(screen2, textvariable=password_verify)
    password_entry1.pack()
    Label(screen2, text="").pack()
    Button(screen2, text="Login", width=30, height=2, command=login_verify).pack()


def main_screen():
    global screen
    screen = Tk()
    screen.geometry("300x250")
    screen.title("Login Page")
    Label(text='Login Page', bg="red", font=("Times New Roman", 40)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="40", command=login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="40", command=register).pack()
    screen.mainloop()


main_screen()

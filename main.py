from tkinter import *
import os

def delete1():
    screen1.destroy()

def register_user():
    username_info = username.get()
    password_info = password.get()

    with open('userinfo.txt',"w") as file:

        file.write(username_info+"\n")
        file.write(password_info+"\n")

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(screen1, text="Success").pack()
    Button(screen1, text="OK", command=delete1).pack()

def register():
    global screen1
    screen1 = Toplevel(wn)
    screen1.title("Register")
    screen1.geometry("300x250")

    global username
    global password
    global username_entry
    global password_entry

    username = StringVar()
    password = StringVar()
    Label(screen1, text = "Please enter your details below").pack()
    Label(screen1, text = "").pack()
    Label(screen1, text = "Username * ").pack()

    username_entry = Entry(screen1, textvariable = username)
    username_entry.pack()
    Label(screen1, text = "Password * ").pack()
    password_entry =  Entry(screen1, textvariable = password)
    password_entry.pack()
    Label(screen1, text = "").pack()
    Button(screen1, text = "Register", width = 10, height = 1, command = register_user).pack()

def login():
    print('Test')

def main():
    global wn
    wn = Tk()
    wn.geometry("300x250")
    wn.title("User Management")
    Label(text = "User Management", bg = "grey", width = "300", height = "2", font = ("Inconsolata", 13)).pack()
    Label(text = "").pack()
    Button(text = "Login", height = "2", width = "30", command = login).pack()
    Label(text = "").pack()
    Button(text = "Register", height = "2", width = "30", command = register).pack()
    Label(text = "").pack()
    wn.mainloop()

main()

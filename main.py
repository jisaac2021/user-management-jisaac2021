from tkinter import *
from tkinter import messagebox
import os
import sqlite3

conn = sqlite3.connect("userinfo.db")
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS user(username TEXT,password TEXT)")
c.execute("SELECT * FROM user")
conn.commit()

def delete1():
    screen1.destroy()

def delete2():
    screen2.destroy()

def register_user():
    username_info = username.get()
    password_info = password.get()

    find_user = ("SELECT * FROM user WHERE username = ?")
    c.execute(find_user,[(username.get())])
    if c.fetchall():
        messagebox.showerror("Error")
    else:
        messagebox.showinfo("Success")
    params = (username_info, password_info)
    c.execute('INSERT INTO user VALUES(?,?)', params)
    conn.commit()


    """with open('userinfo.txt',"w") as file:

        file.write(username_info)
        file.write(",")
        file.write(password_info)
        file.write("\n")"""

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

    username_entry = Entry(screen1, textvariable = username).pack()
    Label(screen1, text = "Password * ").pack()
    password_entry =  Entry(screen1, textvariable = password).pack()
    Label(screen1, text = "").pack()
    Button(screen1, text = "Register", width = 10, height = 1, command = register_user).pack()

def main():
    global wn
    wn = Tk()
    wn.geometry("300x250")
    wn.title("User Management")

    head = Label(text = "User Management", bg = "grey", width = "300", height = "2", font = ("freesansbold", 13), pady=40).pack()
    logf = Frame(padx=10,pady=10)
    Button(text = "Login", height = "2", width = "30", command = login).pack()
    Button(text = "Register", height = "2", width = "30", command = register).pack()
    wn.mainloop()

main()

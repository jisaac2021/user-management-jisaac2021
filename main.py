from tkinter import *
import os

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

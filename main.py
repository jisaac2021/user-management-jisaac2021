from tkinter import *
from tkinter import messagebox
import sqlite3

conn = sqlite3.connect("userinfo.db")
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS user(username text NOT NULL UNIQUE, password text NOT NULL UNIQUE)")
c.execute("SELECT * FROM user")
conn.commit()

def delete1():
    screen1.destroy()

def delete2():
    screen2.destroy()

def delete3():
    screen3.destroy()

def register_user():
    find_user = ("SELECT * FROM user WHERE username = ?")
    c.execute(find_user,[(username.get())])

    if c.fetchall():
        messagebox.showerror("Error!", "There is already an account with that username")
    else:
        c.execute('INSERT INTO user VALUES(?,?)', (username.get(), password.get()))
        conn.commit()
        messagebox.showinfo("Success!", "Account created")
        Label(screen1, text="Account created!").pack()
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
    Label(screen1, text = "")
    password_entry =  Entry(screen1, textvariable = password).pack()
    Label(screen1, text = "").pack()
    Button(screen1, text = "Register", width = 10, height = 1, command = register_user).pack()

def login_user():
    find_user = ("SELECT * FROM user WHERE username = ? AND password = ?")
    c.execute(find_user,[username_verify.get(),password_verify.get()])
    if c.fetchall():
        #Label(screen2, text="Logged in!").pack()
        #Button(screen2, text="OK", command=delete2).pack()
        dashboard()
    else:
        messagebox.showerror("Error!", "Your account information is invalid")

def login():
    global screen2
    screen2 = Toplevel(wn)
    screen2.title("Login")
    screen2.geometry("300x250")

    global username_verify
    global password_verify
    global username_entry1
    global password_entry1

    username_verify = StringVar()
    password_verify = StringVar()

    Label(screen2, text = "Please enter your details below to login").pack()
    Label(screen2, text = "").pack()
    Label(screen2, text = "Username * ").pack()
    username_entry1 = Entry(screen2, textvariable = username_verify)
    username_entry1.pack()
    Label(screen2, text = "Password * ").pack()
    Label(screen2, text = "")
    password_entry1 =  Entry(screen2, textvariable = password_verify)
    password_entry1.pack()
    Label(screen2, text = "").pack()
    Button(screen2, text = "Login", width = 10, height = 1, command = login_user).pack()

def logout():
    screen3.destroy()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)
    print("Logging out...")

def edit():
    global screen4
    screen4 = Toplevel(wn)
    screen4.title("Edit")
    screen4.geometry("300x250")

    global oldusername
    global oldpassword
    global newusername
    global newpassword

    oldusername = StringVar()
    oldpassword = StringVar()

    newusername = StringVar()
    newpassword = StringVar()

    Label(screen4, text = "Old Username * ").pack()
    username_entry2 = Entry(screen4, textvariable = oldusername).pack()
    Label(screen4, text = "Old Password * ").pack()
    password_entry2 =  Entry(screen4, textvariable = oldpassword).pack()

    Label(screen4, text = "New Username * ").pack()
    username_entry3 = Entry(screen4, textvariable = newusername).pack()
    Label(screen4, text = "New Password * ").pack()
    password_entry3 =  Entry(screen4, textvariable = newpassword).pack()
    Label(screen4, text = "").pack()
    Button(screen4, text = "Update", width = 10, height = 1, command = update_user).pack()

def update_user():
    c.execute('SELECT * FROM user')
    if (newusername.get() == oldusername.get()) and (newpassword.get() == oldpassword.get()):
        messagebox.showerror('The information is the same. Try again')
    else:
        c.execute('UPDATE user SET username = ? WHERE username = ?', (newusername.get(), oldusername.get()))
        c.execute('UPDATE user SET password = ? WHERE password = ?', (newpassword.get(), oldpassword.get()))
        conn.commit()

        if c.fetchall():
            messagebox.showerror("Error", "We could not update your account information")
        else:
            messagebox.showinfo("Success!", "Account information updated")

def delete():
    result = messagebox.askquestion("Delete", "Are you sure? This will delete your account.", icon='warning')
    if result == 'yes':
        print("Deleting...")
        c.execute('DELETE FROM user WHERE username = ?', (username_verify.get(),))
        conn.commit()
        delete3()
        username_entry1.delete(0, END)
        password_entry1.delete(0, END)

    else:
        print("Your account remains active")


def dashboard():
    global screen3
    screen3 = Toplevel(wn)
    screen3.title("Dashboard")
    screen3.geometry("300x250")
    Label(screen3, text = "Welcome " + username_verify.get() + " to your dashboard!").pack()
    Button(screen3, text = "Log out", command = logout).pack()
    Button(screen3, text = "Edit account information", command = edit).pack()
    Button(screen3, text = "Delete account", command = delete).pack()

def main():
    global wn
    wn = Tk()
    wn.geometry("300x250")
    wn.title("User Management")

    Label(text = "User Management", bg = "grey", width = "300", height = "2", pady=40).pack()
    Button(text = "Login", height = "2", width = "30", command = login).pack()
    Label(text = "")
    Button(text = "Register", height = "2", width = "30", command = register).pack()
    wn.mainloop()

main()

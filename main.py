from tkinter import *
from tkinter import messagebox
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo
import sqlite3
import hashlib
import sendgrid
import os
import random

conn = sqlite3.connect("userinfo.db")
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS user(username text NOT NULL UNIQUE, password text NOT NULL, email text NOT NULL)")
c.execute("SELECT * FROM user")
conn.commit()

def delete3():
    """Destroy screen3 from a user's screen"""
    screen3.destroy()

def register_user():
    """Take a username and password and save it to the userinfo.db database.
    Send an email (if provided) in the user or return an error in the case that there already exists a user with that username."""
    find_user = ("SELECT * FROM user WHERE username = ?")
    c.execute(find_user,[(username.get())])
    if len(username.get()) == 0:
        messagebox.showerror("Error!", "Please enter a valid username.")
    elif len(password.get()) == 0:
        messagebox.showerror("Error!", "Please enter a valid password.")
    elif len(email.get()) > 0 and ("@" not in email.get()):
        messagebox.showerror("Error!", "Please enter a valid email.")
    elif c.fetchall():
        messagebox.showerror("Error!", "There is already an account with that username.")
    else:
        password_hash = hashlib.md5(password.get().encode('utf-8')).hexdigest()
        c.execute('INSERT INTO user VALUES(?,?,?)', ((username.get(), password_hash, email.get())))
        conn.commit()
        messagebox.showinfo("Success!", "Account created.\nLog in from the main menu.")
        if len(email.get()) != 0:
            sg = sendgrid.SendGridAPIClient(apikey='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')
            data = {
              "personalizations": [
                {
                  "to": [
                    {
                      "email": email_verify.get()
                    }
                  ],
                  "subject": "Your account has been created!"
                }
              ],
              "from": {
                "email": "admin@usermanagement.com"
              },
              "content": [
                {
                  "type": "text/plain",
                  "value": "Welcome to the User Management system! Log in to access your dashboard."
                }
              ]
            }
            response = sg.client.mail.send.post(request_body=data)
            print(response.status_code)
            print(response.body)
            print(response.headers)
            # Button(screen1, text="Exit", command=delete1).pack()
        else:
            pass

def register():
    """Create the register window and prompt a user to enter their username, password, and email"""
    global screen1
    screen1 = Toplevel(wn)
    screen1.title("Register")
    screen1.geometry("300x250")

    global username
    global password
    global email
    global username_entry
    global password_entry
    global email_entry

    username = StringVar()
    password = StringVar()
    email = StringVar()
    Label(screen1, text = "Please enter your details below").pack()
    Label(screen1, text = "").pack()
    Label(screen1, text = "Username * ").pack()
    username_entry = Entry(screen1, textvariable = username).pack()
    Label(screen1, text = "Password * ").pack()
    password_entry =  Entry(screen1, textvariable = password).pack()
    Label(screen1, text = "Email").pack()
    email_entry =  Entry(screen1, textvariable = email).pack()
    Button(screen1, text = "Register", width = 10, height = 1, command = register_user).pack()

def login_user():
    """Take an inputted username and password and check it against the database containing users' info.
    Return an error for a non-existent username or incorrect password."""
    find_user = ("SELECT * FROM user WHERE username = ? AND password = ?")
    password_checkhash = hashlib.md5(password_verify.get().encode('utf-8')).hexdigest()
    c.execute(find_user,[username_verify.get(),password_checkhash])
    if c.fetchall():
        dashboard()
    else:
        messagebox.showerror("Error!", "Your account information is invalid.")

def login():
    """Create the login window and prompt a user to enter their username and password"""
    global screen2
    screen2 = Toplevel(wn)
    screen2.title("Login")
    screen2.geometry("300x250")

    global username_verify
    global password_verify
    global username_entry1
    global password_entry1
    global reset

    username_verify = StringVar()
    password_verify = StringVar()

    Label(screen2, text = "Please enter your details below to login").pack()
    Label(screen2, text = "").pack()
    Label(screen2, text = "Username * ").pack()
    username_entry1 = Entry(screen2, textvariable = username_verify)
    username_entry1.pack()
    Label(screen2, text = "Password * ").pack()
    password_entry1 = Entry(screen2, textvariable = password_verify)
    password_entry1.pack()
    Button(screen2, text = "Login", width = 15, height = 1, command = login_user).pack()
    reset = Label(screen2, text = "Forgot password?", width = 15, height = 1)
    reset.pack()
    reset.bind("<Button-1>",forgot_password)
    reset.bind("<Enter>",red_text)
    reset.bind("<Leave>",black_text)

def forgot_password(event=None):
    """Create the reset password window and prompt a user to enter their username and email"""
    global screen5
    screen5 = Toplevel(wn)
    screen5.title("Reset Password")
    screen5.geometry("300x250")

    global username_verify4
    global email_verify
    global username_entry4
    global email_entry

    username_verify4 = StringVar()
    email_verify = StringVar()

    Label(screen5, text = "Username * ").pack()
    username_entry4 = Entry(screen5, textvariable = username_verify4)
    username_entry4.pack()

    Label(screen5, text = "Email * ").pack()
    email_entry = Entry(screen5, textvariable = email_verify)
    email_entry.pack()

    Button(screen5, text = "Reset Password", width = 15, height = 1, command = reset_password).pack()


def reset_password():
    """Allow a user to reset their password through a secret verification key sent via email."""
    find_user = ("SELECT * FROM user WHERE username = ? AND email = ?")
    c.execute(find_user,[username_verify4.get(),email_verify.get()])
    if c.fetchall():

        resetpass = random.randint(100000,999999)

        sg = sendgrid.SendGridAPIClient(apikey='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')
        data = {
          "personalizations": [
            {
              "to": [
                {
                  "email": email_verify.get()
                }
              ],
              "subject": "Reset your password"
            }
          ],
          "from": {
            "email": "admin@usermanagement.com"
          },
          "content": [
            {
              "type": "text/plain",
              "value": "Hello, %s. Enter this verification code to reset your password: %d." % (username_verify4.get(), resetpass)
            }
          ]
        }
        response = sg.client.mail.send.post(request_body=data)
        print(response.status_code)
        print(response.body)
        print(response.headers)

        code = askstring('Verification code', 'Enter your 6-digit verification code.')

        if int(code) == resetpass:

            newpass = askstring('Set new password', 'Enter your new password.')
            hashnewpass = hashlib.md5(newpass.encode('utf-8')).hexdigest()

            c.execute('UPDATE user SET password = ? WHERE username = ? and email = ?', (hashnewpass, username_verify4.get(), email_verify.get()))
            conn.commit()
            messagebox.showinfo("Success!", "Account information updated.")

        else:
            messagebox.showinfo("Error!", "The verification code you entered was invalid.")

    else:
        messagebox.showerror("Error!", "Your account information is invalid.")

def red_text(event=None):
    """Changes the text to red"""
    reset.config(fg="red")

def black_text(event=None):
    """Changes the text to black"""
    reset.config(fg="black")

def logout():
    """Logs the user out"""
    screen3.destroy()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

def edit():
    """Create the edit window and prompt a user to choose a new username/password"""
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
    Button(screen4, text = "Update", width = 10, height = 1, command = update_user).pack()

def update_user():
    """Update the database with a user's new username and/or password"""
    find_user = ("SELECT * FROM user WHERE username = ? AND password = ?")
    password_hash2 = hashlib.md5(oldpassword.get().encode('utf-8')).hexdigest()
    c.execute(find_user,[oldusername.get(),password_hash2])
    if (newusername.get() == oldusername.get()) and (newpassword.get() == oldpassword.get()):
        messagebox.showerror("Error!", "The information is the same. Try again.")
    elif not c.fetchall():
        messagebox.showerror("Error!", "Please enter valid account information.")
    else:
        try:
            c.execute('UPDATE user SET username = ? WHERE username = ?', (newusername.get(), oldusername.get()))
            c.execute('UPDATE user SET password = ? WHERE password = ?', (newpassword.get(), oldpassword.get()))
            conn.commit()
            messagebox.showinfo("Success!", "Account information updated.")
        except sqlite3.IntegrityError:
            messagebox.showerror("Error!", "An account already exists with that information.")

def delete():
    """Delete a user's account from the database"""
    result = messagebox.askquestion("Delete", "Are you sure? This will permanently delete your account.", icon='warning')
    if result == 'yes':
        c.execute('DELETE FROM user WHERE username = ?', (username_verify.get(),))
        conn.commit()
        delete3()
        username_entry1.delete(0, END)
        password_entry1.delete(0, END)
    else:
        messagebox.showinfo("Alert!", "Your account remains active.")

def dashboard():
    """Create the dashboard window and allow the user to log out, edit their information, or delete their account"""
    global screen3
    screen3 = Toplevel(wn)
    screen3.title("Dashboard")
    screen3.geometry("300x250")
    Label(screen3, text = "Welcome " + username_verify.get() + " to your dashboard!").pack()
    Button(screen3, text = "Log out", command = logout).pack()
    Button(screen3, text = "Edit account information", command = edit).pack()
    Button(screen3, text = "Delete account", command = delete, fg = 'red').pack()

def main():
    """Create the main menu window so that a user can choose to login or register"""
    global wn
    wn = Tk()
    wn.geometry("300x250")
    wn.title("User Management")

    Label(text = "User Management", bg = "grey", width = "300", height = "2", pady=40).pack()
    Button(text = "Login", height = "2", width = "30", command = login).pack()
    Button(text = "Register", height = "2", width = "30", command = register).pack()
    wn.mainloop()

main()

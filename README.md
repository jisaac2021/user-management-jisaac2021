# User Management

## Challenge
This project is a GUI user management system that allows users to register an account, login with a username and password, and logout. After logging in, a user will be allowed to edit their profile data and/or delete their
account. This application is able to register multiple users and store their information in a SQL database.

***You will not need to install any extra programs but the file does use Tkinter for GUI functionality and MessageBox and Sqlite to store each user's information in the file userinfo.db.***

Run main.py in terminal (CodingClass/user-management-jisaac2021) to start the program:
```terminal
cd CodingClass/user-management-jisaac2021
python3 main.py
```

Notice how a database is not stored in this repository because it is created once the file main.py is first run.
Here is the snippet of code that does this:

```python
c.execute("CREATE TABLE IF NOT EXISTS user(username text NOT NULL UNIQUE, password text NOT NULL UNIQUE)")
```

This should prompt the user with the two options: to Login or Register.

![image](https://github.com/kehillah-coding-2019/user-management-jisaac2021/blob/master/mainmenu.png)

### Functions

#### `register()`
This function takes a username and password and saves it the the userinfo.db database. It returns an error in the case that there already exists a user with that username. Note that the `.gitignore` file is created in order to avoid
committing sensitive user data to your repository! DO NOT COMMIT THE DATABASE!

![image](https://github.com/kehillah-coding-2019/user-management-jisaac2021/blob/master/register.png)

#### `login()`
This function takes an inputted username and password and checks it against
the database containing users' info. It returns an error for
a non-existent username or incorrect password. 

![image](https://github.com/kehillah-coding-2019/user-management-jisaac2021/blob/master/register.png)

#### `logout()`
This function does not take any parameters. It clears the data containing
the logged in user from the main loop.

#### `edit()`
Only for a logged in user, this function allows them to change their
username or password by editing the database.

#### `delete()`
Only for a logged in user, this function prompts the user with a
warning and then deletes their data from the user database.

Here is the overall look of the dashboard (once a user logs in).
![image](https://github.com/kehillah-coding-2019/user-management-jisaac2021/blob/master/dashboard.png)


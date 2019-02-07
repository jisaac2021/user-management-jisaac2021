# User Management

## Challenge
For this project, you need to create a user management system.
That is, a program that allows users to register an account,
login with a username and password, and logout. The program should
also allow a user to edit their profile data and delete their
account. Your application needs to be able to register multiple users.

### Functions
To meet the goals of the challenge you will need to create at least
the following functions:

#### `register()`
This function needs to take all the profile data (minimum username
and password) and save it in a file. It should return an error if there
already exists a user with that username. Use `.gitignore` to avoid
committing sensitive user data to your repository!

#### `login()`
This function needs to take a username and password and check against
the data file containing users' info. It should return an error for
a non-existent username or incorrect password, it should return all the
user data on success. Save the user data in a variable in the main loop of
the program.

#### `logout()`
This function does not take any parameters. It clears the data containing
the logged in user from the main loop.

#### `edit()`
Only for a logged in user, this function should allow them to change their
username or password by editing the file containing all user data.

#### `delete()`
Only for a logged in user, this function should prompt the user with a
warning and then delete their data from the file containing all user data.

## Code
Code snippets and hints that might be useful

#### Open a file for writing
```python
with open('numbers.txt', 'w') as myFile:

    for x in range(10):
        myFile.write('line: ' + str(x) + '\n') #newline character is necessary.
```

#### Open a file for reading
```python
with open('someFile.txt', 'r') as myFile: #someFile.txt must exist

    for x in myFile.readlines():
        print(x)
```

#### Split a line of text
```python
>>> line = "Martha Stewart, 75, NJ"
>>> line.split()
['Martha', 'Stewart,', '75,', 'NJ']
>>> line.split(",")
['Martha Stewart', ' 75', ' NJ']
>>> myList = line.split(",")
>>> myList[1]
' 75'
>>>
```

#### Create a navigation prompt
```python
exit = False

while not exit:

    print('1. Stuff')
    print('2. Other Stuff')
    print('3. Different Stuff')
    print('4. Exit')

    s = input('Make a selection: ')

    if s == '4':
        exit = True
```

#### Create an md5 hash
```python
>>> import hashlib
>>> password = 'super secret pass phrase'
>>> hash = hashlib.md5(password.encode('utf-8')).hexdigest()
>>> hash
'187813013127e6b4679f0378ec99afb5'
>>>
```

## Grading
Please review the rubrics for grading. When you are finished,
modify this README file with entirely your own content. Be sure
to use markdown to make the README professionally formatted.


#### Level 1
The system has a main menu and a `register` function that allows the user to save a username and password in a text file. The system also has a `login` function that allows a user to type in a username and password and then opens the file to see if it matches and returns `True` on a successful login.

#### Level 2
The system allows for logging out and for multiple users to register accounts. This means the system will save multiple lines (users) in the text file and search through it when one tries to log in.

#### Level 3.1
The system allows users to save extra profile data and view/edit their info.

#### Level 3.2
The system stores passwords as md5 hashes or similar to enhance security.

#### Level 4
The system is more sophisticated than Level 3. For example, instead of storing a plain text file, use a json file, or use a
database such as sqlite or MongoDB. Another idea is to implement password reset functionality so that if a user forgets
their password, their account can be recovered (see sendgrid in your GitHub student developer pack). You can also use a web server like Flask to create a web app implementing a user management system.

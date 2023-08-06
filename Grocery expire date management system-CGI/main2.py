#!C:\Python311\python.exe
print("Content-Type: text/html\r\n\r\n")


import cgi
import pymysql
form = cgi.FieldStorage()
mydb =pymysql.Connect(host="localhost",user="root",password="Abdul@123",database="project4")
mycursor =mydb.cursor()

username =form.getvalue("u")
email =form.getvalue("e")
password =form.getvalue("p")


sqlform ="Insert into emp values(%s,%s,%s)"
employees =[username,email,password]
mycursor.execute(sqlform,employees)
mydb.commit()
print('''<!DOCTYPE html>
    <html>
    <head>
        <title>slidee Navbar</title>
        <link rel="stylesheet" type="text/css" href="slidestyle.css">
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans:ital,wght@1,100;1,300&display=swap" rel="stylesheet">
    </head>
    <body>
        <div class="main">
            <input type="checkbox" id="chk" aria-hidden="true">

            <div class="signup">
                <form action="main2.py" >
                    <label for="chk" aria-hidden="true">sign up</label>
                    <input type="text"  placeholder="User name" required="" >
                    <input type="email"  placeholder="Email" required="" >
                    <input type="password"  placeholder="Password" required="">
                    <button>Sign up</button>
                </form>
            </div>
            <div class="login">
                <form action="main3.py">
                    <label for="chk" aria-hidden="true">Login</label>
                    <input type="email" name="email" placeholder="Email" required="">
                    <input type="password" name="pswd" placeholder="Password" required="">
                    <button>Login</button>
                </form>
        </div>

    </body>
    </html>''')

#!C:\Python311\python.exe
print("Content-Type: text/html\r\n\r\n")


import cgi
import pymysql
form = cgi.FieldStorage()
mydb =pymysql.Connect(host="localhost",user="root",password="Abdul@123",database="project1")
mycursor =mydb.cursor()

username =form.getvalue("u")
password =form.getvalue("p")
address =form.getvalue("a")
contact =form.getvalue("c")
mail =form.getvalue("m")


sqlform ="Insert into employee values(%s,%s,%s,%s,%s)"
employees =[username,password,address,contact,mail]
mycursor.execute(sqlform,employees)
mydb.commit()

print('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Resistration</title>
</head>
<style>
    legend{
        text-align: center;
    }
    fieldset{
        height:530px;
        width:400px;
        margin-top:100px;
        border-color: black;
        box-shadow:inset -3px -3px rgba(0,0,0,0.5);
        background-color:rgba(0,0,0,0.5);
        border-radius: 10px;
        transform: translateY(30px);
    }
    input{
        height: 30px;
        width: 200px;
        background: transparent;
        border-radius: 10px;
        border-block-width: 3px;
        color:white;
        background-color:rgba(0,0,0,0.5);   

    }
    button{
        height:28;
        width:150px;
        background-color:rgba(0,0,0,0.7);
        border-radius: 10px;
        color:white;
    }
    #chk{
        height:25px;
        width:150px;
        background-color:rgba(0,0,0,0.7);
        border-radius: 10px;
        color:white;
    }
    #kol{
        text-align: left;
        display: block;
        margin-top: 5px; 
        color: chartreuse;
        font-size:15px;
    }
    a{
     color:chartreuse;
     
    }
    body{
        background-image: url("register.jpg");
        background-size: 1400px;
                   
    }
</style>
<body>
    <center>
        <fieldset>
            <lable><b style="font-size: 20px;color: chartreuse;">Registration</b></label>
            <label id=kol><b>*Register Successfully</b></label>
            <form  action="register.html" method="post" >
                <table border="0px" cellpadding="15px">
                    <tr>
                        <td><b style="color:white;">UserName</b></td>
                        <td><input type="text" name="u" ></td>
                    </tr>
                    <tr>
                        <td><b style="color:white;">Password</b></td>
                        <td><input type="password" name="p" ></td>
                    </tr>
                    <tr>
                        <td><b style="color:white;">Address</b></td>
                        <td><input type="text" name="a" ></td>
                    </tr>
                    <tr>
                        <td><b style="color:white;">Contact</b></td>>
                        <td><input type="text" name="c" ></td>
                    </tr>
                    <tr>
                        <td><b style="color:white;">Email</b></td>
                        <td><input type="email" name="m" ></td>
                    </tr>
                    <tr>
                        <td colspan="2">
                            <center>
                                <input  id=chk type="reset" value="Clear">
                                <button>Register</button>
                            </center>   
                        </td>  
                    </tr>
                    <tr>
                        <td colspan="2">
                            <center><h3><a href="login.html">Login</a></h3></center>
                        </td>
                    </tr>
                </table>
            </form>
        </fieldset>
    </center>
</body>
</html>''')










#!C:\Python311\python.exe
print("Content-Type: text/html\r\n\r\n")


import cgi
import pymysql
form = cgi.FieldStorage()
mydb =pymysql.Connect(host="localhost",user="root",password="Abdul@123",database="project1")
mycursor =mydb.cursor()

username =form.getvalue("u")
password =form.getvalue("p")


mycursor.execute("select * from employee")
c=[]
#ce=[('',''),('','')]
for i in mycursor:
        c.append(i)
#c=cn+ce

for j in range (len(c)):
    if ((c[j][0])==username and (c[j][1])==password ):
         with open("navibar.html")as f:
            print(f.read())
            
         
 
            
    
    #elif((c[1][0])==username and (c[1][1])==password ):
       # print("Location: /navibar.html")
       # print("Content-type: text/html")
       # print()
       # break
    
    #elif((c[2][0])==username and (c[2][1])==password ):
        #print("<h1>welcome",username,"<h1>")
       # break


   
        
        
    
        
    else:
         print('''<!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta http-equiv="X-UA-Compatible" content="IE=edge">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Login</title>
                </head>
                <style>
                    legend {
                
                }
                    fieldset{
                        height:350px;
                        width:400px;
                        margin-top: 100px;
                        border-color: black;
                        box-shadow:inset -3px -3px rgba(0,0,0,0.5);
                        background-color:rgba(0,0,0,0.5);
                    
                    }
                    table{
                        border-collapse: collapse;
                        margin-top: 20px;
                    }
                    input{
                        height:30px;
                        width:200px;
                        background: transparent;
                        border-radius: 10px;
                        border-block-width: 3px;
                        color:white;
                    }
                    #clr,#log{
                        height:30px;
                        width:150px;
                        color:white;
                        background-color:rgba(0,0,0,0.7);
                        

                    }
                    button{
                        height: 30px;
                        width:150px;
                        background-color:rgba(0,0,0,0.7);
                        border-radius: 10px;
                        color:white;
                        
                    }
                    #kol{
                        text-align: left;
                        display: block;
                        margin-top: 5px; 
                        color: red;
                    }
                    body{
                    background-image: url("lake.jpg");
                    background-size: 1400px;
                    
                    }
                    a{
                    color:black;
                    }
                </style>
                <body>
                    <center>
                        <fieldset>
                            <label><b style="color:white;font-size:25px;">Login</b></legend>
                            <label id=kol><b>*Invalid username or Password!</b></label>
                            <form action="cgilog.py">
                                <table border="0.5px" cellpadding="15px">
                                    <tr>
                                        <td><b style="color:white;">User Name</b></td>
                                        <td><input type="text" name="u"></td>
                                    </tr>
                                    <tr>
                                        <td><b style="color:white;">PassWord</b></td>
                                        <td><input type="password" name="p"></td>
                                    </tr>
                                    <tr>
                                        <td colspan="2">
                                            <center>
                                                <input id="clr" type="reset" value="Clear">
                                                <button>Login</button>
                                            </center>
                                        </td> 
                                    </tr>
                                    <tr>
                                        <td colspan="2" style="color:white;"><center><h3>Are you new user?<a href="register.html">Sigup Here</a></h3></center></td>
                                    </tr>

                                </table>
                            </form>
                        </fieldset>
                    </center>
                </body>
                </html>''')

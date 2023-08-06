#!C:\Python311\python.exe
print("Content-Type: text/html\r\n\r\n")


import cgi
import pymysql
from datetime import date
import datetime
form = cgi.FieldStorage()
mydb =pymysql.Connect(host="localhost",user="root",password="Abdul@123",database="project5")
mycursor =mydb.cursor()
product =form.getvalue("d1")

now = datetime.date.today()
#cur= now.strftime("%y-%m-%d")
#print(cur)

c=[]

mycursor.execute("select * from store")
for i in mycursor:
        c.append(i)
g1= now-c[0][2]
g2= now-c[1][2]
g3= now-c[2][2]
g4= now-c[3][2]


m1=g1.days
m2=g2.days
m3=g3.days
m4=g4.days

k1=abs(m1)
k2=abs(m2)
k3=abs(m3)
k4=abs(m4)

if m1<=0 and product==c[0][0]:
    print('''<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
            <link rel="stylesheet" href="super3.css">
        </head>
        <style>
            #ng{
                margin-left: 220px;
                width:600px;
                height: 750px;;
                transform: translateY(5%);
            }
            #ro{
                background-color: green;
            }

        </style>
        <body>
            <div class="navbar">
                <h2><b style="color:white;"><center>ABDUL SUPER MARKET</center></b></h2>
                <ul>
                    <li><a href="super1.html">Home</a></li>
                    <li><a href="#">Store</a></li>
                    <li><a href="first.html">logout</a></li>
                </ul>
            </div>
                <fieldset id="ng">
                    <center><img src="dark.jpg" border="5px"  height="200px"; width="400px" style="margin-top: 20px;"></center><br>
                    <center>
                        <hr>
                        <center><b><h2>Product Details</h2></b></center>
                        <hr>
                        <div >
                            <table>
                                <tr>
                                    <td><h3><b style="font-size: large; font-family: Arial, Helvetica, sans-serif; margin-right: 300px;">product name:darkfantacy</b></h3></td><br>
                                </tr>
                                <tr>
                                    <td><h3><b style="font-size: large; font-family: Arial, Helvetica, sans-serif; margin-right: 300px;">Total Quantity:''',c[0][1],''' nos</b></h3></td><br>
                                </tr>
                                    <td><h3><b style="font-size: large; font-family: Arial, Helvetica, sans-serif; margin-right: 300px;">Current date:''',now,'''</b></h3></td><br>
                                </tr>
                                </tr>
                                    <td><h3><b style="font-size: large; font-family: Arial, Helvetica, sans-serif; margin-right: 300px;">Expire date:''',c[0][2],'''</b></h3></td><br>
                                </tr>
                                <tr>
                                    <td><h3><b style="font-size: large; font-family: Arial, Helvetica, sans-serif; margin-right: 300px;">Status: Not Expired( Expires in''',k1,'''days) </b></h3></td> 
                                </tr>
                            </table>
                        </div>
                    </center>
                </fieldset>
                ''')
elif m2<=0 and product==c[1][0]:
     print('''<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
            <link rel="stylesheet" href="super3.css">
        </head>
        <style>
            #ng{
                margin-left: 220px;
                width:600px;
                height: 750px;;
                transform: translateY(5%);
            }
            #ro{
                background-color: green;
            }

        </style>
        <body>
            <div class="navbar">
                <h2><b style="color:white;"><center>ABDUL SUPER MARKET</center></b></h2>
                <ul>
                    <li><a href="super1.html">Home</a></li>
                    <li><a href="#">Store</a></li>
                    <li><a href="first.html">logout</a></li>
                </ul>
            </div>
                <fieldset id="ng">
                    <center><img src="coke.jpg" border="5px"  height="200px"; width="400px" style="margin-top: 20px;"></center><br>
                    <center>
                        <hr>
                        <center><b><h2>Product Details</h2></b></center>
                        <hr>
                        <div >
                            <table>
                                <tr>
                                    <td><h3><b style="font-size: large; font-family: Arial, Helvetica, sans-serif; margin-right: 300px;">product name:Coke</b></h3></td><br>
                                </tr>
                                <tr>
                                    <td><h3><b style="font-size: large; font-family: Arial, Helvetica, sans-serif; margin-right: 300px;">Total Quantity:''',c[1][1],''' nos</b></h3></td><br>
                                </tr>
                                    <td><h3><b style="font-size: large; font-family: Arial, Helvetica, sans-serif; margin-right: 300px;">Current date:''',now,'''</b></h3></td><br>
                                </tr>
                                </tr>
                                    <td><h3><b style="font-size: large; font-family: Arial, Helvetica, sans-serif; margin-right: 300px;">Expire date:''',c[1][2],'''</b></h3></td><br>
                                </tr>
                                <tr>
                                    <td><h4><b style="font-size: large; font-family: Arial, Helvetica, sans-serif; margin-right: 300px;">Status: Not Expired(Expires in''',k2,'''days) </b></h4></td> 
                                </tr>
                            </table>
                        </div>
                    </center>
                </fieldset>
                ''')
elif m3<=0 and product==c[2][0]:
     print('''<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
            <link rel="stylesheet" href="super3.css">
        </head>
        <style>
            #ng{
                margin-left: 220px;
                width:600px;
                height: 750px;;
                transform: translateY(5%);
            }
            #ro{
                background-color: green;
            }

        </style>
        <body>
            <div class="navbar">
                <h2><b style="color:white;"><center>ABDUL SUPER MARKET</center></b></h2>
                <ul>
                    <li><a href="super1.html">Home</a></li>
                    <li><a href="#">Store</a></li>
                    <li><a href="first.html">logout</a></li>
                </ul>
            </div>
                <fieldset id="ng">
                    <center><img src="maggi.png" border="5px"  height="200px"; width="400px" style="margin-top: 20px;"></center><br>
                    <center>
                        <hr>
                        <center><b><h2>Product Details</h2></b></center>
                        <hr>
                        <div >
                            <table>
                                <tr>
                                    <td><h3><b style="font-size: large; font-family: Arial, Helvetica, sans-serif; margin-right: 300px;">product name:Maggi</b></h3></td><br>
                                </tr>
                                <tr>
                                    <td><h3><b style="font-size: large; font-family: Arial, Helvetica, sans-serif; margin-right: 300px;">Total Quantity:''',c[2][1],''' nos</b></h3></td><br>
                                </tr>
                                    <td><h3><b style="font-size: large; font-family: Arial, Helvetica, sans-serif; margin-right: 300px;">Current date:''',now,'''</b></h3></td><br>
                                </tr>
                                </tr>
                                    <td><h3><b style="font-size: large; font-family: Arial, Helvetica, sans-serif; margin-right: 300px;">Expire date:''',c[2][2],'''</b></h3></td><br>
                                </tr>
                                <tr>
                                    <td><h3><b style="font-size: large; font-family: Arial, Helvetica, sans-serif; margin-right: 300px;">Status: Not Expired(Expires in ''',k3,'''days) </b></h3></td> 
                                </tr>
                            </table>
                        </div>
                    </center>
                </fieldset>
                ''')
elif m4<=0 and product==c[3][0]:
     print('''<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
            <link rel="stylesheet" href="super3.css">
        </head>
        <style>
            #ng{
                margin-left: 220px;
                width:600px;
                height: 750px;;
                transform: translateY(5%);
            }
            #ro{
                background-color: green;
            }

        </style>
        <body>
            <div class="navbar">
                <h2><b style="color:white;"><center>ABDUL SUPER MARKET</center></b></h2>
                <ul>
                    <li><a href="super1.html">Home</a></li>
                    <li><a href="#">Store</a></li>
                    <li><a href="first.html">logout</a></li>
                </ul>
            </div>
                <fieldset id="ng">
                    <center><img src="milk1.jpg" border="5px"  height="200px"; width="400px" style="margin-top: 20px;"></center><br>
                    <center>
                        <hr>
                        <center><b><h2>Product Details</h2></b></center>
                        <hr>
                        <div >
                            <table>
                                <tr>
                                    <td><h3><b style="font-size: large; font-family: Arial, Helvetica, sans-serif; margin-right: 300px;">product name:DairyMilk</b></h3></td><br>
                                </tr>
                                <tr>
                                    <td><h3><b style="font-size: large; font-family: Arial, Helvetica, sans-serif; margin-right: 300px;">Total Quantity:''',c[3][1],''' nos</b></h3></td><br>
                                </tr>
                                    <td><h3><b style="font-size: large; font-family: Arial, Helvetica, sans-serif; margin-right: 300px;">Current date:''',now,'''</b></h3></td><br>
                                </tr>
                                </tr>
                                    <td><h3><b style="font-size: large; font-family: Arial, Helvetica, sans-serif; margin-right: 300px;">Expire date:''',c[3][2],'''</b></h3></td><br>
                                </tr>
                                <tr>
                                    <td><h3><b style="font-size: large; font-family: Arial, Helvetica, sans-serif; margin-right: 300px;">Status: Not Expired(Expires in''',k4,'''days) </b></h3></td>
                                </tr>
                            </table>
                        </div>
                    </center>
                </fieldset>
                ''')

else:
    if product==c[0][0]:
         print('''<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
            <link rel="stylesheet" href="super3.css">
        </head>
        <style>
            #ng{
                margin-left: 220px;
                width:600px;
                height: 750px;;
                transform: translateY(5%);
            }

        </style>
        <body>
            <div class="navbar">
                <h2><b style="color:white;"><center>ABDUL SUPER MARKET</center></b></h2>
                <ul>
                    <li><a href="super1.html">Home</a></li>
                    <li><a href="#">Store</a></li>
                    <li><a href="first.html">logout</a></li>
                </ul>
            </div>
                <fieldset id="ng">
                    <center><img src="e1.jpg" border="5px"  height="200px"; width="400px" style="margin-top: 20px;"></center><br
                    <form action="super2.py" border="3px">
                    <center>
                        <hr>
                        <center><h2>Product Details</h2></center>
                        <hr>
                        <div >
                            <table>
                                <tr>
                                    <td><h3><b style="font-size: large; font-family: Arial, Helvetica, sans-serif; margin-right: 300px;">product name:darkfantacy</b></h3></td><br>
                                </tr>
                                <tr>
                                    <td><h3><b style="font-size: large; font-family: Arial, Helvetica, sans-serif; margin-right: 300px;">Total Quantity:''',c[0][1],''' nos</b></h3></td><br>
                                </tr>
                                    <td><h3><b style="font-size: large; font-family: Arial, Helvetica, sans-serif; margin-right: 300px;">Current date:''',now,'''</b></h3></td><br>
                                </tr>
                                </tr>
                                    <td><h3><b style="font-size: large; font-family: Arial, Helvetica, sans-serif; margin-right: 300px;">Expire date:''',c[0][2],'''</b></h3></td><br>
                                </tr>
                                <tr>
                                    <td><h3><b style="font-size: large; font-family: Arial, Helvetica, sans-serif; margin-right: 300px;">Status: Expired </b></h3></td><br> 
                                </tr>
                            </table>
                        </div>
                    </center>
                ''')
    elif product==c[1][0]:
         print('''<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
            <link rel="stylesheet" href="super3.css">
        </head>
        <style>
            #ng{
                margin-left: 220px;
                width:600px;
                height: 750px;;
                transform: translateY(5%);
            }

        </style>
        <body>
            <div class="navbar">
                <h2><b style="color:white;"><center>ABDUL SUPER MARKET</center></b></h2>
                <ul>
                    <li><a href="super1.html">Home</a></li>
                    <li><a href="#">Store</a></li>
                    <li><a href="first.html">logout</a></li>
                </ul>
            </div>
                <fieldset id="ng">
                    <center><img src="e2.jpeg" border="5px"  height="200px"; width="400px" style="margin-top: 20px;"></center><br
                    <form action="super2.py" border="3px">
                    <center>
                        <hr>
                        <center><h2>Product Details</h2></center>
                        <hr>
                        <div >
                            <table>
                                <tr>
                                    <td><h3><b style="font-size: large; font-family: Arial, Helvetica, sans-serif; margin-right: 300px;">product name:Coke</b></h3></td><br>
                                </tr>
                                <tr>
                                    <td><h3><b style="font-size: large; font-family: Arial, Helvetica, sans-serif; margin-right: 300px;">Total Quantity:''',c[1][1],''' nos</b></h3></td><br>
                                </tr>
                                    <td><h3><b style="font-size: large; font-family: Arial, Helvetica, sans-serif; margin-right: 300px;">Current date:''',now,'''</b></h3></td><br>
                                </tr>
                                </tr>
                                    <td><h3><b style="font-size: large; font-family: Arial, Helvetica, sans-serif; margin-right: 300px;">Expire date:''',c[1][2],'''</b></h3></td><br>
                                </tr>
                                <tr>
                                    <td><h3><b style="font-size: large; font-family: Arial, Helvetica, sans-serif; margin-right: 300px;">Status: Expired </b></h3></td><br> 
                                </tr>
                            </table>
                        </div>
                    </center>
                ''')
    elif product==c[2][0]:
         print('''<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
            <link rel="stylesheet" href="super3.css">
        </head>
        <style>
            #ng{
                margin-left: 220px;
                width:600px;
                height: 750px;;
                transform: translateY(5%);
            }

        </style>
        <body>
            <div class="navbar">
                <h2><b style="color:white;"><center>ABDUL SUPER MARKET</center></b></h2>
                <ul>
                    <li><a href="super1.html">Home</a></li>
                    <li><a href="#">Store</a></li>
                    <li><a href="first.html">logout</a></li>
                </ul>
            </div>
                <fieldset id="ng">
                    <center><img src="e3.jpeg" border="5px"  height="200px"; width="400px" style="margin-top: 20px;"></center><br
                    <form action="super2.py" border="3px">
                    <center>
                        <hr>
                        <center><h2>Product Details</h2></center>
                        <hr>
                        <div >
                            <table>
                                <tr>
                                    <td><h3><b style="font-size: large; font-family: Arial, Helvetica, sans-serif; margin-right: 300px;">product name:Maggi</b></h3></td><br>
                                </tr>
                                <tr>
                                    <td><h3><b style="font-size: large; font-family: Arial, Helvetica, sans-serif; margin-right: 300px;">Total Quantity:''',c[2][1],''' nos</b></h3></td><br>
                                </tr>
                                    <td><h3><b style="font-size: large; font-family: Arial, Helvetica, sans-serif; margin-right: 300px;">Current date:''',now,'''</b></h3></td><br>
                                </tr>
                                </tr>
                                    <td><h3><b style="font-size: large; font-family: Arial, Helvetica, sans-serif; margin-right: 300px;">Expire date:''',c[2][2],'''</b></h3></td><br>
                                </tr>
                                <tr>
                                    <td><h3><b style="font-size: large; font-family: Arial, Helvetica, sans-serif; margin-right: 300px;">Status: Expired </b></h3></td><br> 
                                </tr>
                            </table>
                        </div>
                    </center>
                ''')
    elif product==c[3][0]:
         print('''<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
            <link rel="stylesheet" href="super3.css">
        </head>
        <style>
            #ng{
                margin-left: 220px;
                width:600px;
                height: 750px;;
                transform: translateY(5%);
            }

        </style>
        <body>
            <div class="navbar">
                <h2><b style="color:white;"><center>ABDUL SUPER MARKET</center></b></h2>
                <ul>
                    <li><a href="super1.html">Home</a></li>
                    <li><a href="#">Store</a></li>
                    <li><a href="first.html">logout</a></li>
                </ul>
            </div>
                <fieldset id="ng">
                    <center><img src="e4.jpeg" border="5px"  height="200px"; width="400px" style="margin-top: 20px;"></center><br
                    <form action="super2.py" border="3px">
                    <center>
                        <hr>
                        <center><h2>Product Details</h2></center>
                        <hr>
                        <div >
                            <table>
                                <tr>
                                    <td><h3><b style="font-size: large; font-family: Arial, Helvetica, sans-serif; margin-right: 300px;">product name:DairyMilk</b></h3></td><br>
                                </tr>
                                <tr>
                                    <td><h3><b style="font-size: large; font-family: Arial, Helvetica, sans-serif; margin-right: 300px;">Total Quantity:''',c[3][1],''' nos</b></h3></td><br>
                                </tr>
                                    <td><h3><b style="font-size: large; font-family: Arial, Helvetica, sans-serif; margin-right: 300px;">Current date:''',now,'''</b></h3></td><br>
                                </tr>
                                </tr>
                                    <td><h3><b style="font-size: large; font-family: Arial, Helvetica, sans-serif; margin-right: 300px;">Expire date:''',c[3][2],'''</b></h3></td><br>
                                </tr>
                                <tr>
                                    <td><h3><b style="font-size: large; font-family: Arial, Helvetica, sans-serif; margin-right: 300px;">Status: Expired </b></h3></td><br> 
                                </tr>
                            </table>
                        </div>
                    </center>
                ''')
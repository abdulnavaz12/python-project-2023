#!C:\Python311\python.exe
print("Content-Type: text/html\r\n\r\n")


import cgi
import pymysql
form = cgi.FieldStorage()
mydb =pymysql.Connect(host="localhost",user="root",password="Abdul@123",database="project5")
mycursor =mydb.cursor()

product =form.getvalue("s")
quantity =form.getvalue("e")
exp =form.getvalue("d")

sqlform ="Insert into store values(%s,%s,%s)"
employees =[product,quantity,exp]
mycursor.execute(sqlform,employees)
mydb.commit()
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
                margin-left: 450px;
                transform: translateY(-110%);
            }
            #mg{
                margin-left: 0px;
                transform: translateY(-110%);
            }
            #rss{
                margin-left: 460px;
                transform: translateY(-220%);
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
            <fieldset style="bgcolor:red;">
                <center><img src="dark.jpg" border="5px"  height="200px"; width="300px"></center><br>
                <form action="super2.py" border="3px">
                    <center>
                        <center><h5>*Incoming Product Entry</h5></center>
                        <input type="text" name="s" placeholder="product name">
                        <input type="text" name="e" placeholder="quantity"><br><br>
                        Expire date:<input type="date" name="d"><br>
                    </center>
                    <br><br>
                    <center><button><b>Submit</b></button></center>
                </form>
                <form action="date.py">
                    <center><h5>*Check Expire Date</h5></center>
                    <center><input type="text" name="d1" placeholder="product name" required=""></center><br>
                    <center><button><b>Check</b></button></center>
                </form>       
            </fieldset>
            <div id="ng">
                <fieldset style="bgcolor:red;">
                    <center><img src="coke.jpg" border="5px"  height="200px"; width="300px"></center><br>
                    <form action="super2.py" border="3px">
                        <center>
                            <center><h5>*Incoming Product Entry</h5></center>
                            <input type="text" name="s" placeholder="product name">
                            <input type="text" name="e" placeholder="quantity"><br><br>
                            Expire date:<input type="date" name="d"><br>
                        </center>
                        <br><br>
                        <center><button><b>Submit</b></button></center>
                    </form>
                    <form action="date.py">
                        <center><h5>*Check Expire Date</h5></center>
                        <center><input type="text" name="d1" placeholder="product name"></center><br>
                        <center><button><b>Check</b></button></center>
                    </form>       
                </fieldset>
            </div>
            <div id="mg">
                <fieldset style="bgcolor:red;">
                    <center><img src="maggi.png" border="5px"  height="200px"; width="300px"></center><br>
                    <form action="super2.py" border="3px">
                        <center>
                            <center><h5>*Incoming Product Entry</h5></center>
                            <input type="text" name="s" placeholder="product name">
                            <input type="text" name="e" placeholder="quantity"><br><br>
                            Expire date:<input type="date" name="d"><br>
                        </center>
                        <br><br>
                        <center><button><b>Submit</b></button></center>
                    </form>
                    <form action="date.py">
                        <center><h5>*Check Expire Date</h5></center>
                        <center><input type="text" name="d1" placeholder="product name" required=""></center><br>
                        <center><button><b>Check</b></button></center>
                    </form>       
                </fieldset>
            </div>
            <div id="rss">
                <fieldset>
                    <center><img src="milk1.jpg" border="5px"  height="200px"; width="300px"></center><br>
                    <form action="super2.py" border="3px">
                        <center>
                            <center><h5>*Incoming Product Entry</h5></center>
                            <input type="text" name="s" placeholder="product name">
                            <input type="text" name="e" placeholder="quantity"><br><br>
                            Expire date:<input type="date" name="d"><br>
                        </center>
                        <br><br>
                        <center><button><b>Submit</b></button></center>
                    </form>
                    <form action="date.py">
                        <center><h5>*Check Expire Date</h5></center>
                        <center><input type="text" name="d1" placeholder="product name"></center><br>
                        <center><button><b>Check</b></button></center>
                    </form>       
                </fieldset>
            </div>
        </body>
        </html>
        ''')
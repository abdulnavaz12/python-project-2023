#!C:\Python311\python.exe
print("Content-Type: text/html\r\n\r\n")


import cgi
import pymysql
form = cgi.FieldStorage()
mydb =pymysql.Connect(host="localhost",user="root",password="Abdul@123",database="project3")
mycursor =mydb.cursor()

start =form.getvalue("s")
end =form.getvalue("e")
mycursor.execute("select * from traffic")
c=[]
for i in mycursor:
        c.append(i)


if c[0][0]==start and c[0][1]==end:
    print('''<!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Document</title>
                <link rel="stylesheet" href="nav.css">
            </head>
            <style>
                #rk{
                    width:1150px;
                    height: 600px;
                    background-color: white;
                    transform:translateY(-70%)
                    
                }
                #mk{
                    margin-left: 700px;
                    transform: translateY(-480px);
                    margin-right: 50px;

                }
                #jk{
                    margin-left: 700px;
                    transform:translateY(-290%)
                }
                @keyframes bind {
                0% {
                    transform: scale(1);
                    opacity: 5;
                    background-color: green;
                }
                50%{
                    opacity: 1;
                    background-color: yellow;
                }
                100% {
                    opacity: 1;
                    background-color:red;
                }
                
                }
                .bind {
                    border-radius: 50%;
                    width: 35px;
                    height: 35px;
                    opacity: 2;
                    -webkit-animation: bind 50s infinite;
                    text-shadow: ok;
                    -moz-animation: bind 50s infinite;
                    -o-animation: bind 50s infinite;
                    animation: bind 50s infinite;
                    transform: translateX(60%);
                }
                .bind:after{
                    border-radius: 50%;
                    content: "";
                    position: absolute;
                    top: 1px;
                    left: 1px;
                    right: 1px;
                    bottom: 1px;
                    border: 5px solid #ffffff;
                    
                }

            </style>
            <body>
                <div class="navbar">
                    <h1><b ><center>TRAFFIC SIGNAL TRACKER</center></b></h1>
                    <ul>
                        <li><a href="navibar.html">Home</a></li>
                        <li><a href="#">AboutUs</a></li>
                        <li><a href="#">Location</a></li>
                        <li><a href="#">search</a></li>
                        <li><a href="login.html">logout</a></li>
                    </ul>
                </div>
                <div>
                    <body>
                        <fieldset>
                            <form action="brain.py" method="post">)    
                                <input type="text" name="s" placeholder="choose start location">
                                <input type="text" name="e" placeholder="choose destination"><br><br><br><br>
                                <button><b>Submit</b></button>
                            </form>   
                        </fieldset>
                            
                        <center><iframe src="https://www.google.com/maps/embed?pb=!1m28!1m12!1m3!1d15546.502510600325!2d80.19930321953461!3d13.059485355581637!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!4m13!3e6!4m5!1s0x3a5266bf5a08c45f%3A0x9478e1cd7e7f1723!2sVadapalani%2C%20Chennai%2C%20Tamil%20Nadu!3m2!1d13.049971099999999!2d80.2121306!4m5!1s0x3a5266bcb821fe8b%3A0x8c47272f7397ba4f!2s3694%2B26F%20Puratchi%20Thalaivar%20Dr.%20M.G.R.%20Bus%20Terminus%20(CMBT%20Koyembedu)%2C%20CMBT%20Passenger%20Way%2C%20Koyambedu%2C%20Chennai%2C%20Tamil%20Nadu%20600107!3m2!1d13.0675522!2d80.20555499999999!5e0!3m2!1sen!2sin!4v1678955311161!5m2!1sen!2sin"
                            width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></center>
                            <fieldset id=rk>
                                <div>
                                    <table>
                                        <tr>
                                            <td>
                                                <h2>vadapalani to mgr.cmbt-total(''',c[0][2],'''km)</h2>
                                                <ul>
                                                    <li><b>ARUMPAKKAM</b></li>
                                                    <li><b>THIRUNAGAR</b></li>
                                                    <li><b>MMDA</b></li>
                                                    <li><b>M.G.R.CMBT</b></li>
                                                </ul>
                                                <h3>Total''',c[0][3],'''stages </h3>
                                                <h2>Trasport mode</h2>
                                                <ul>
                                                    <li><b>bike(6min)</b></li>
                                                    <li><b>bus(15min)</b></li>
                                                    <li><b>car(10min)</b></li>
                                                    <li><b>walk(33min)</b></li>
                                                </ul>
                                                <h2>Meaning of blinking light</h2>
                                                <ul>
                                                    <li><b style="color:red; font-size:20px;">red color-stop the vehicle</b></li>
                                                    <li><b style="color:yellow;font-size:20px;">yellow color-slow the vehicle</b></li>
                                                    <li><b style="color:green;font-size:20px;">green color-go</b></li>
                                                </ul>
                                                
                                            </td>
                                        </tr>
                                    </table>
                                    <table id=mk>
                                        <tr>
                                            <td>
                                                <h1>Traffic light tracker</h1>
                                                <h3>Your destination found 2 signals only</h3>
                                                <ul>
                                                    <h3>signal Area</h3>
                                                    <li><b>ARUMPAKKAM</b></li>
                                                    <li><b>M.G.R.CMBT</b></li>
                                                </ul>
                                                <h2>current light blinking</h2>
                                            </td>
                                        </tr>
                                    </table>
                                    <div id=jk>
                                        <h4 class="blink"><h4>ARUMPAKAM
                                        <div>
                                            <h1 class="bind"></h1>M.G.R.CMBT
                                        </div>
                                        
                                    </div>
                                </div>
                            </fieldset>
                    </body>
                </div>
            </body>

            </html>''')

elif c[1][0]==start and c[1][1]==end:
    # print(c[1][0],c[1][1])
    # print("<h1>hello<h1>")
     print('''<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
            <link rel="stylesheet" href="nav.css">
            <link rel="stylesheet" href="font/css/all.min.css">
        </head>
        <style>
            #rk{
                width:1150px;
                height: 600px;
                background-color: white;
                transform:translateY(-70%)
                
            }
            #mk{
                margin-left: 700px;
                transform: translateY(-530px);
                margin-right: 50px;

            }
            #jk{
                margin-left: 700px;
                transform:translateY(-200%)
            }
            @keyframes bind {
            0% {
                transform: scale(1);
                opacity: 5;
                background-color: green;
            }
            50%{
                opacity: 1;
                background-color: yellow;
            }
            100% {
                opacity: 1;
                background-color:red;
            }
            
            }
            .bind {
                border-radius: 50%;
                width: 35px;
                height: 35px;
                opacity: 2;
                -webkit-animation: bind 50s infinite;
                text-shadow: ok;
                -moz-animation: bind 50s infinite;
                -o-animation: bind 50s infinite;
                animation: bind 50s infinite;
                transform: translateX(60%);
            }
            .bind:after{
                border-radius: 50%;
                content: "";
                position: absolute;
                top: 1px;
                left: 1px;
                right: 1px;
                bottom: 1px;
                border: 5px solid #ffffff;
                
            }
            @keyframes bush {
            0% {
                transform: scale(1);
                opacity: 5;
                background-color: red;
            }
            50%{
                opacity: 1;
                background-color:green;
            }
            100% {
                opacity: 1;
                background-color:yellow;
            }
            
            }

            .bush{
                border-radius: 50%;
                width: 35px;
                height: 35px;
                opacity: 2;
                -webkit-animation: bush 50s infinite;
                text-shadow: ok;
                -moz-animation: bush 50s infinite;
                -o-animation: bush 50s infinite;
                animation: bush 50s infinite;
                transform: translateX(60%);
            }
            .bush:after{
                border-radius: 50%;
                content: "";
                position: absolute;
                top: 1px;
                left: 1px;
                right: 1px;
                bottom: 1px;
                border: 5px solid #ffffff;
                
            }


        </style>
        <body>
            <div class="navbar">
                <h1><b ><center>TRAFFIC SIGNAL TRACKER</center></b></h1>
                <ul>
                    <li><a href="navibar.html">Home</a></li>
                    <li><a href="#">AboutUs</a></li>
                    <li><a href="#">Location</a></li>
                    <li><a href="#">search</a></li>
                    <li><a href="login.html">logout</a></li>
                </ul>
            </div>
            <div>
                <body>
                    <fieldset>
                        <form action='brain.py'>
                            <input type="text" name="s" placeholder="choose start location">
                            <input type="text" name="e" placeholder="choose destination"><br><br><br><br>
                            <button><b>Submit</b></button>
                        </form>   
                    </fieldset>
                        
                    <center><iframe src="https://www.google.com/maps/embed?pb=!1m28!1m12!1m3!1d31098.046115782436!2d80.19835548844652!3d13.019378025399375!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!4m13!3e6!4m5!1s0x3a52671fd09f3cbf%3A0xa0d7b686ccb55af0!2sAshok%20Pillar%2C%20Ashok%20Nagar%2C%20Chennai%2C%20Tamil%20Nadu%20600083!3m2!1d13.033545!2d80.212086!4m5!1s0x3a5267709aa40a7d%3A0xca348695fc512750!2sGuindy%2C%20Chennai%2C%20Tamil%20Nadu!3m2!1d13.0066625!2d80.2206369!5e0!3m2!1sen!2sin!4v1678974960779!5m2!1sen!2sin" 
                        width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></center>
                        <fieldset id=rk>
                            <div>
                                <table>
                                    <tr>
                                        <td>
                                            <h2>Ashok pillar to Guindy-total(''',c[1][2],'''km)</h2>
                                            <ul>
                                                <li><b>KASI THEATRE</b></li>
                                                <li><b>KALAIMAGAL NAGAG</b></li>
                                                <li><b>EKKATTUTHANGAL</b></li>
                                                <li><b>C.I.P.E.T.(TECHNO PARK)</b></li>
                                                <li><b>GUINDY BUS TERMINAL</b></li>
                                            </ul>
                                            <h3>Total''',c[1][3],''' stages </h3>
                                            <h2>Trasport mode</h2>
                                            <ul>
                                                <li><b>bike(16min)</b></li>
                                                <li><b>bus(25min)</b></li>
                                                <li><b>car(19min)</b></li>
                                                <li><b>walk(57min)</b></li>
                                            </ul>
                                            <h2>Meaning of blinking light</h2>
                                            <ul>
                                                <li><b style="color:red; font-size:20px;">red color-stop the vehicle</b></li>
                                                <li><b style="color:yellow;font-size:20px;">yellow color-slow the vehicle</b></li>
                                                <li><b style="color:green;font-size:20px;">green color-go</b></li>
                                            </ul>
                                            
                                        </td>
                                    </tr>
                                </table>
                                <table id=mk>
                                    <tr>
                                        <td>
                                            <h1>Traffic light tracker</h1>
                                            <h2>Your destination have 3 signals so, go carefully</h2>
                                            <ul>
                                                <h3>signal Area</h3>
                                                <li><b>KASI THEATRE</b></li>
                                                <li><b>EKKATTUTHANGAL</b></li>
                                                <li><b>TECHNO PARK</b></li>
                                            </ul>
                                            <h2>current light blinking</h2>
                                        </td>
                                    </tr>
                                </table>
                                <div id=jk>
                                    <h4 class="blink"><h4>KASI THEATRE
                                    <div>
                                        <h1 class="bind"></h1>EKKATTUTHANGAL
                                    </div>
                                    <div>
                                        <h1 class="bush"></h1>TECHNO PARK
                                    </div>
                                </div>
                            </div>
                        </fieldset>
                </body>
            </div>
        </body>

        </html>
        </html>''')
     
elif c[2][0]==start and c[2][1]==end:
      print('''<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
            <link rel="stylesheet" href="nav.css">
            <link rel="stylesheet" href="font/css/all.min.css">
        </head>
        <style>
            #rk{
                width:1150px;
                height: 600px;
                background-color: white;
                transform:translateY(-70%)
                
            }
            #mk{
                margin-left: 700px;
                transform: translateY(-500px);
                margin-right: 50px;

            }
            #jk{
                margin-left: 700px;
                transform:translateY(-650%)
            }

        </style>
        <body>
            <div class="navbar">
                <h1><b ><center>TRAFFIC SIGNAL TRACKER</center></b></h1>
                <ul>
                    <li><a href="navibar.html">Home</a></li>
                    <li><a href="#">AboutUs</a></li>
                    <li><a href="#">Location</a></li>
                    <li><a href="#">search</a></li>
                    <li><a href="login.html">logout</a></li>
                </ul>
            </div>
            <div>
                <body>
                    <fieldset>
                        <form action='brain.py'>
                            <input type="text" name="s" placeholder="choose start location">
                            <input type="text" name="e" placeholder="choose destination"><br><br><br><br>
                            <button><b>Submit</b></button>
                        </form>   
                    </fieldset>
                        
                    <center><iframe src="https://www.google.com/maps/embed?pb=!1m28!1m12!1m3!1d408.5703335449382!2d80.204570359272!3d13.035800237653882!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!4m13!3e6!4m5!1s0x3a52671fd09f3cbf%3A0xa0d7b686ccb55af0!2sAshok%20Pillar%2C%20Ashok%20Nagar%2C%20Chennai%2C%20Tamil%20Nadu!3m2!1d13.033545!2d80.212086!4m5!1s0x3a52677fa934c62d%3A0x8160900374515685!2sSLA%20Jobs%20-%20Placement%20Training%20Institute%20in%20Chennai%2C%20Softlogic%20Systems%2C%20PT%20Rajan%20Road%2C%20Sector%201%2C%20K.%20K.%20Nagar%2C%20Chennai%2C%20Tamil%20Nadu!3m2!1d13.0360208!2d80.2043316!5e0!3m2!1sen!2sin!4v1678988069931!5m2!1sen!2sin"
                        width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></center>
                        <fieldset id=rk>
                            <div>
                                <table>
                                    <tr>
                                        <td>
                                            <h3>ASHOK PILLAR to SLA JOBS-PLACEMENT TRAINING(''',c[2][2],'''km)</h3>
                                            <ul>
                                                <li><b>GOVERNMENT PERIPHERAL</b></li>
                                                <li><b>ESIC HOSPITAL</b></li>
                                                <li><b>CORPORATION PARK</b></li>
                                                <li><b>M.G.R.NAGAR BUS TERMINUS</b></li>
                                                <li><b>SLA INSTITUDE</b></li>
                                            </ul>
                                            <h3>Total''',c[2][3],'''stages </h3>
                                            <h2>Trasport mode</h2>
                                            <ul>
                                                <li><b>bike(4min)</b></li>
                                                <li><b>bus(8min)</b></li>
                                                <li><b>car(4min)</b></li>
                                                <li><b>walk(12min)</b></li>
                                            </ul>
                                            <h2>Meaning of blinking light</h2>
                                            <ul>
                                                <li><b style="color:red; font-size:20px;">red color-stop the vehicle</b></li>
                                                <li><b style="color:yellow;font-size:20px;">yellow color-slow the vehicle</b></li>
                                                <li><b style="color:green;font-size:20px;">green color-go</b></li>
                                            </ul>
                                            
                                        </td>
                                    </tr>
                                </table>
                                <table id=mk>
                                    <tr>
                                        <td>
                                            <h1>Traffic light tracker</h1>
                                            <h2>Your destination found 1 signal only</h2>
                                            <ul>
                                                <h3>signal Area</h3>
                                                <li><b>ASHOK PILLAR</b></li>
                                            </ul>
                                            <h2>current light blinking</h2>
                                        </td>
                                    </tr>
                                </table>
                                <div id=jk>
                                    <h4 class="blink"><h4>ASHOK PILLAR

                                </div>
                            </div>
                        </fieldset>
                </body>
            </div>
        </body>

        </html>
        ''')
elif c[3][0]==start and c[3][1]==end:
      print('''<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
            <link rel="stylesheet" href="nav.css">
            <link rel="stylesheet" href="font/css/all.min.css">
        </head>
        <style>
            #rk{
                width:1150px;
                height: 600px;
                background-color: white;
                transform:translateY(-70%)
                
            }
            #mk{
                margin-left: 700px;
                transform: translateY(-450px);
                margin-right: 50px;

            }
            #jk{
                margin-left: 700px;
                transform:translateY(-580%)
            }
            @keyframes bind {
            0% {
                transform: scale(1);
                opacity: 5;
                background-color: green;
            }
            50%{
                opacity: 1;
                background-color: yellow;
            }
            100% {
                opacity: 1;
                background-color:red;
            }
            
            }

        </style>
        <body>
            <div class="navbar">
                <h1><b ><center>TRAFFIC SIGNAL TRACKER</center></b></h1>
                <ul>
                    <li><a href="navibar.html">Home</a></li>
                    <li><a href="#">AboutUs</a></li>
                    <li><a href="#">Location</a></li>
                    <li><a href="#">search</a></li>
                    <li><a href="login.html">logout</a></li>
                </ul>
            </div>
            <div>
                <body>
                    <fieldset>
                        <form action="brain.py">
                            <input type="text" name="s" placeholder="choose start location">
                            <input type="text" name="e" placeholder="choose destination"><br><br><br><br>
                            <button><b>Submit</b></button>
                        </form>   
                    </fieldset>
                        
                    <center><iframe src="https://www.google.com/maps/embed?pb=!1m28!1m12!1m3!1d15549.396977719733!2d80.21402931952791!3d13.01341780995642!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!4m13!3e6!4m5!1s0x3a5267709aa40a7d%3A0xca348695fc512750!2sGuindy%2C%20Chennai%2C%20Tamil%20Nadu!3m2!1d13.0066625!2d80.2206369!4m5!1s0x3a52671aa10c448b%3A0xf62cad8de2391803!2sSaidapet%2C%20Chennai%2C%20Tamil%20Nadu!3m2!1d13.0212805!2d80.2231037!5e0!3m2!1sen!2sin!4v1679032495522!5m2!1sen!2sin"
                        width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></center>
                        <fieldset id=rk>
                            <div>
                                <table>
                                    <tr>
                                        <td>
                                            <h2>GUINDY to SAIDAPET-total(''',c[3][2],'''km)</h2>
                                            <ul>
                                                <li><b>LITTLE MOUNT</b></li>
                                                <li><b>SAIDAPET</b></li>
                                            </ul>
                                            <h3>Total''',c[3][3],'''stages </h3>
                                            <h2>Trasport mode</h2>
                                            <ul>
                                                <li><b>bike(4min)</b></li>
                                                <li><b>car(7min)</b></li>
                                                <li><b>walk(25min)</b></li>
                                            </ul>
                                            <h2>Meaning of blinking light</h2>
                                            <ul>
                                                <li><b style="color:red; font-size:20px;">red color-stop the vehicle</b></li>
                                                <li><b style="color:yellow;font-size:20px;">yellow color-slow the vehicle</b></li>
                                                <li><b style="color:green;font-size:20px;">green color-go</b></li>
                                            </ul>
                                            
                                        </td>
                                    </tr>
                                </table>
                                <table id=mk>
                                    <tr>
                                        <td>
                                            <h1>Traffic light tracker</h1>
                                            <h3>Your destination found 1 signals ONLY</h3>
                                            <ul>
                                                <h3>signal Area</h3>
                                                <li><b>LITTLE MOUNT</b></li>
                                            </ul>
                                            <h2>Current light blinking</h2>
                                        </td>
                                    </tr>
                                </table>
                                <div id=jk>
                                    <h4 class="blink"><h4>LITTLE MOUNT   
                                </div>
                            </div>
                        </fieldset>
                </body>
            </div>
        </body>
        </html>
        ''')
elif c[4][0]==start and c[4][1]==end:
      print('''<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
            <link rel="stylesheet" href="nav.css">
            <link rel="stylesheet" href="font/css/all.min.css">
        </head>
        <style>
            #rk{
                width:1150px;
                height: 600px;
                background-color: white;
                transform:translateY(-70%)
                
            }
            #mk{
                margin-left: 700px;
                transform: translateY(-570px);
                margin-right: 50px;

            }
            #jk{
                margin-left: 700px;
                transform:translateY(-210%)
            }
            @keyframes bind {
            0% {
                transform: scale(1);
                opacity: 5;
                background-color: green;
            }
            50%{
                opacity: 1;
                background-color: yellow;
            }
            100% {
                opacity: 1;
                background-color:red;
            }
            
            }
            .bind {
                border-radius: 50%;
                width: 35px;
                height: 35px;
                opacity: 2;
                -webkit-animation: bind 50s infinite;
                text-shadow: ok;
                -moz-animation: bind 50s infinite;
                -o-animation: bind 50s infinite;
                animation: bind 50s infinite;
                transform: translateX(60%);
            }
            .bind:after{
                border-radius: 50%;
                content: "";
                position: absolute;
                top: 1px;
                left: 1px;
                right: 1px;
                bottom: 1px;
                border: 5px solid #ffffff;
                
            }
            @keyframes bush {
            0% {
                transform: scale(1);
                opacity: 5;
                background-color: red;
            }
            50%{
                opacity: 1;
                background-color:green;
            }
            100% {
                opacity: 1;
                background-color:yellow;
            }
            
            }

            .bush{
                border-radius: 50%;
                width: 35px;
                height: 35px;
                opacity: 2;
                -webkit-animation: bush 50s infinite;
                text-shadow: ok;
                -moz-animation: bush 50s infinite;
                -o-animation: bush 50s infinite;
                animation: bush 50s infinite;
                transform: translateX(60%);
            }
            .bush:after{
                border-radius: 50%;
                content: "";
                position: absolute;
                top: 1px;
                left: 1px;
                right: 1px;
                bottom: 1px;
                border: 5px solid #ffffff;
                
            }


        </style>
        <body>
            <div class="navbar">
                <h1><b ><center>TRAFFIC SIGNAL TRACKER</center></b></h1>
                <ul>
                    <li><a href="navibar.html">Home</a></li>
                    <li><a href="#">AboutUs</a></li>
                    <li><a href="#">Location</a></li>
                    <li><a href="#">search</a></li>
                    <li><a href="login.html">logout</a></li>
                </ul>
            </div>
            <div>
                <body>
                    <fieldset>
                        <form action="brain.py">
                            <input type="text" name="s" placeholder="choose start location">
                            <input type="text" name="e" placeholder="choose destination"><br><br><br><br>
                            <button><b>Submit</b></button>
                        </form>   
                    </fieldset>
                        
                    <center><iframe src="https://www.google.com/maps/embed?pb=!1m28!1m12!1m3!1d31095.633290670765!2d80.17320683845767!3d13.03858977134929!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!4m13!3e6!4m5!1s0x3a5266df5d1ed063%3A0xd1d7cf3a46b5c88a!2sK.K.%20Nagar%20Bus%20Depo%20Rd%2C%20K.%20K.%20Nagar%2C%20Chennai%2C%20Tamil%20Nadu%20600083!3m2!1d13.0351059!2d80.20514589999999!4m5!1s0x3a526130ee5d7a2b%3A0x2e22e53ce9c67720!2sValasaravakkam%2C%20Chennai%2C%20Tamil%20Nadu%20600087!3m2!1d13.040272499999999!2d80.1722913!5e0!3m2!1sen!2sin!4v1679036691154!5m2!1sen!2sin"
                        width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></center>
                        <fieldset id=rk>
                            <div>
                                <table>
                                    <tr>
                                        <td>
                                            <h2>KKNAGAR to VALASAVAKKAM(''',c[4][2],'''km)</h2>
                                            <ul>
                                                <li><b>SIVAN PARK</b></li>
                                                <li><b>NAGATHAMMAN KOIL</b></li>
                                                <li><b>VADPALANI</b></li>
                                                <li><b>AVICHI SCHOOL</b></li>
                                                <li><b>VIRUGAMBAKKAM</b></li>
                                                <li><b>ALWARTHIRUNAGAR</b></li>
                                                <li><b>KESAVARDHINI</b></li>
                                                <li><b>VALASAVAKKAM</b></li>
                                            </ul>
                                            <h3>Total''',c[4][3],''' stages </h3>
                                            <h2>Trasport mode</h2>
                                            <ul>
                                                <li><b>bike(16min)</b></li>
                                                <li><b>bus(28min)</b></li>
                                                <li><b>car(20min)</b></li>
                                                <li><b>walk(53min)</b></li>
                                            </ul>
                                            <h2>Meaning of blinking light</h2>
                                            <ul>
                                                <li><b style="color:red; font-size:20px;">red color-stop the vehicle</b></li>
                                                <li><b style="color:yellow;font-size:20px;">yellow color-slow the vehicle</b></li>
                                                <li><b style="color:green;font-size:20px;">green color-go</b></li>
                                            </ul>
                                            
                                        </td>
                                    </tr>
                                </table>
                                <table id=mk>
                                    <tr>
                                        <td>
                                            <h1>Traffic light tracker</h1>
                                            <h3>Your destination found 3 signal only</h3>
                                            <ul>
                                                <h3>signal Area</h3>
                                                <li><b>VADAPALANI</b></li>
                                                <li><b>AVICHI SCHOOL</b></li>
                                                <li><b>VALASARAVAKKAM</b></li>
                                            </ul>
                                            <h2>current light blinking</h2>
                                        </td>
                                    </tr>
                                </table>
                                <div id=jk>
                                    <h4 class="blink"><h4>VADAPALANI
                                    <div>
                                        <h1 class="bind"></h1>AVICHI SCHOOL
                                    </div>
                                    <div>
                                        <h1 class="bush"></h1>VALASARAVAKKAM
                                    </div>
                                </div>
                            </div>
                        </fieldset>
                </body>
            </div>
        </body>

        </html>
        </html>''')
elif c[5][0]==start and c[5][1]==end:
      print('''<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
            <link rel="stylesheet" href="nav.css">
            <link rel="stylesheet" href="font/css/all.min.css">
        </head>
        <style>
            #rk{
                width:1150px;
                height: 600px;
                background-color: white;
                transform:translateY(-70%)
                
            }
            #mk{
                margin-left: 700px;
                transform: translateY(-500px);
                margin-right: 50px;

            }
            #jk{
                margin-left: 700px;
                transform:translateY(-300%)
            }
            @keyframes bind {
            0% {
                transform: scale(1);
                opacity: 5;
                background-color: green;
            }
            50%{
                opacity: 1;
                background-color: yellow;
            }
            100% {
                opacity: 1;
                background-color:red;
            }
            
            }
            .bind {
                border-radius: 50%;
                width: 35px;
                height: 35px;
                opacity: 2;
                -webkit-animation: bind 50s infinite;
                text-shadow: ok;
                -moz-animation: bind 50s infinite;
                -o-animation: bind 50s infinite;
                animation: bind 50s infinite;
                transform: translateX(60%);
            }
            .bind:after{
                border-radius: 50%;
                content: "";
                position: absolute;
                top: 1px;
                left: 1px;
                right: 1px;
                bottom: 1px;
                border: 5px solid #ffffff;
                
            }
            @keyframes bush {
            0% {
                transform: scale(1);
                opacity: 5;
                background-color: red;
            }
            50%{
                opacity: 1;
                background-color:green;
            }
            100% {
                opacity: 1;
                background-color:yellow;
            }
            
            }


        </style>
        <body>
            <div class="navbar">
                <h1><b ><center>TRAFFIC SIGNAL TRACKER</center></b></h1>
                <ul>
                    <li><a href="navibar.html">Home</a></li>
                    <li><a href="#">AboutUs</a></li>
                    <li><a href="#">Location</a></li>
                    <li><a href="#">search</a></li>
                    <li><a href="login.html">logout</a></li>
                </ul>
            </div>
            <div>
                <body>
                    <fieldset>
                        <form action="brain.py">
                            <input type="text" name="s" placeholder="choose start location">
                            <input type="text" name="e" placeholder="choose destination"><br><br><br><br>
                            <button><b>Submit</b></button>
                        </form>   
                    </fieldset>
                        
                    <center><iframe src="https://www.google.com/maps/embed?pb=!1m28!1m12!1m3!1d15544.26854794835!2d80.16899251953973!3d13.094931602206547!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!4m13!3e6!4m5!1s0x3a5263deb77f4477%3A0xa94fa37dfead3491!2sAmbattur%20Industrial%20Estate%2C%20Chennai%2C%20Tamil%20Nadu!3m2!1d13.089191999999999!2d80.1613047!4m5!1s0x3a526585542ff163%3A0xd057b21dd0be7ceb!2sPadi%20saravana%20store%2C%20THE%20LEGEND%20NEW%20SARAVANA%20STORES%2C%20Padi%2C%20Chennai%2C%20Tamil%20Nadu%20600050!3m2!1d13.1006095!2d80.1903998!5e0!3m2!1sen!2sin!4v1679049552250!5m2!1sen!2sin"
                        width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></center>
                        <fieldset id=rk>
                            <div>
                                <table>
                                    <tr>
                                        <td>
                                            <h2>AMBATTUR I.E to PADI-total(''',c[5][2],'''km)</h2>
                                            <ul>
                                                <li><b>MANNUR PETTAI</b></li>
                                                <li><b>BRITANNIA.LTD</b></li>
                                                <li><b>EDAI STREET</b></li>
                                                <li><b>JUNCTION OF CENTRAL AVENUE&ERIKARI</b></li>
                                                <li><b>PADI</b></li>
                                            </ul>
                                            <h3>Total''',c[5][3],'''stages </h3>
                                            <h2>Trasport mode</h2>
                                            <ul>
                                                <li><b>bike(10min)</b></li>
                                                <li><b>car(16min)</b></li>
                                                <li><b>walk(58min)</b></li>
                                            </ul>
                                            <h2>Meaning of blinking light</h2>
                                            <ul>
                                                <li><b style="color:red; font-size:20px;">red color-stop the vehicle</b></li>
                                                <li><b style="color:yellow;font-size:20px;">yellow color-slow the vehicle</b></li>
                                                <li><b style="color:green;font-size:20px;">green color-go</b></li>
                                            </ul>
                                            
                                        </td>
                                    </tr>
                                </table>
                                <table id=mk>
                                    <tr>
                                        <td>
                                            <h1>Traffic light tracker</h1>
                                            <h3>Your destination found 2 signals only</h3>
                                            <ul>
                                                <h3>signal Area</h3>
                                                <li><b>AMBATTUR I.E</b></li>
                                                <li><b>PADI</b></li>
                                            </ul>
                                            <h2>Current light blinking</h2>
                                        </td>
                                    </tr>
                                </table>
                                <div id=jk>
                                    <h4 class="blink"><h4>AMBATTUR I.E
                                    <div>
                                        <h1 class="bind"></h1>PADI
                                    </div>   
                                </div>
                            </div>
                        </fieldset>
                </body>
            </div>
        </body>
        </html>
        ''')
elif c[6][0]==start and c[6][1]==end:
      print('''<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
            <link rel="stylesheet" href="nav.css">
            <link rel="stylesheet" href="font/css/all.min.css">
        </head>
        <style>
            #rk{
                width:1150px;
                height: 600px;
                background-color: white;
                transform:translateY(-70%)
                
            }
            #mk{
                margin-left: 700px;
                transform: translateY(-450px);
                margin-right: 50px;

            }
            #jk{
                margin-left: 700px;
                transform:translateY(-250%)
            }
            @keyframes bind {
            0% {
                transform: scale(1);
                opacity: 5;
                background-color: yellow;
            }
            50%{
                opacity: 1;
                background-color:red;
            }
            100% {
                opacity: 1;
                background-color:green;
            }
            
            }
            .bind {
                border-radius: 50%;
                width: 35px;
                height: 35px;
                opacity: 2;
                -webkit-animation: bind 50s infinite;
                text-shadow: ok;
                -moz-animation: bind 50s infinite;
                -o-animation: bind 50s infinite;
                animation: bind 50s infinite;
                transform: translateX(60%);
            }
            .bind:after{
                border-radius: 50%;
                content: "";
                position: absolute;
                top: 1px;
                left: 1px;
                right: 1px;
                bottom: 1px;
                border: 5px solid #ffffff;
                
            }
        

        </style>
        <body>
            <div class="navbar">
                <h1><b ><center>TRAFFIC SIGNAL TRACKER</center></b></h1>
                <ul>
                    <li><a href="navibar.html">Home</a></li>
                    <li><a href="#">AboutUs</a></li>
                    <li><a href="#">Location</a></li>
                    <li><a href="#">search</a></li>
                    <li><a href="login.html">logout</a></li>
                </ul>
            </div>
            <div>
                <body>
                    <fieldset>
                        <form action="brain.py">
                            <input type="text" name="s" placeholder="choose start location">
                            <input type="text" name="e" placeholder="choose destination"><br><br><br><br>
                            <button><b>Submit</b></button>
                        </form>   
                    </fieldset>
                        
                    <center><iframe src="https://www.google.com/maps/embed?pb=!1m28!1m12!1m3!1d15544.70872686798!2d80.17493796953872!3d13.087954752871479!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!4m13!3e6!4m5!1s0x3a526404c4ab93c1%3A0x2e6970d3b4900705!2sThirumangalam%20EB%20Office%2C%20Ambattur%20Estate%20Road%2C%20Gaingaiammaannagar%2C%20Natarajan%20Nagar%2C%20Thirumangalam%2C%20Chennai%2C%20Tamil%20Nadu!3m2!1d13.087081!2d80.1979442!4m5!1s0x3a5263e616346c39%3A0x31b8ec9577ae752e!2sMogaipair%20Road%20Junction%2C%20Mogappair%2C%20Chennai%2C%20Tamil%20Nadu!3m2!1d13.088787!2d80.16944!5e0!3m2!1sen!2sin!4v1679064892829!5m2!1sen!2sin"
                        width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></center>
                        <fieldset id=rk>
                            <div>
                                <table>
                                    <tr>
                                        <td>
                                            <h3>THIRUMANGALAM to MOGAIPAIR JUCTION(''',c[6][2],'''km)</h3>
                                            <ul>
                                                <li><b>COLLECTOR NAGAR</b></li>
                                                <li><b>KRISHNA NAGAR</b></li>
                                                <li><b>WAVIN</b></li>
                                                <li><b>MOGAIPAIR</b></li>
                                            </ul>
                                            <h3>Total''',c[6][3],'''stages </h3>
                                            <h2>Trasport mode</h2>
                                            <ul>
                                                <li><b>bike(9min)</b></li>
                                                <li><b>car(11min)</b></li>
                                                <li><b>walk(38min)</b></li>
                                            </ul>
                                            <h4>Meaning of blinking light</h4>
                                            <ul>
                                                <li><b style="color:red; font-size:20px;">red color-stop the vehicle</b></li>
                                                <li><b style="color:yellow;font-size:20px;">yellow color-slow the vehicle</b></li>
                                                <li><b style="color:green;font-size:20px;">green color-go</b></li>
                                            </ul>
                                            
                                        </td>
                                    </tr>
                                </table>
                                <table id=mk>
                                    <tr>
                                        <td>
                                            <h1>Traffic light tracker</h1>
                                            <h3>Your destination found 2 signals only</h3>
                                            <ul>
                                                <h3>signal Area</h3>
                                                <li><b>COLLECTOR NAGAR</b></li>
                                                <li><b>WAVIN</b></li>
                                            </ul>
                                            <h2>Current light blinking</h2>
                                        </td>
                                    </tr>
                                </table>
                                <div id=jk>
                                    <h4 class="blink"><h4>COLLECTOR NAGAR
                                    <div>
                                        <h4 class="bind"></h4>WAVIN
                                    </div>   
                                </div>
                            </div>
                        </fieldset>
                </body>
            </div>
        </body>
        </html>''')
else:
      print('''<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
            <link rel="stylesheet" href="nav.css">
            <link rel="stylesheet" href="font/css/all.min.css">
        </head>
        <style>
            .slide-text {
                    animation-name: slide;
                    animation-duration: 40s;
                    animation-iteration-count: infinite;
                    margin_right:20px;
                    color:lightseagreen;
                    
            }
            @keyframes slide {
                0% {
                transform: translateX(100%); 
                }
                100% { 
                    transform: translateX(0%);
                }
            }
        </style>
        <body>
            <div class="navbar">
                <h1><b style="color:white;"><center>TRAFFIC SIGNAL TRACKER</center></b></h1>
                <ul>
                    <li><a href="#">Home</a></li>
                    <li><a href="#">AboutUs</a></li>
                    <li><a href="#">Location</a></li>
                    <li><a href="#">search</a></li>
                    <li><a href="login.html">logout</a></li>
                </ul>
            </div>
            <div class='slide-text'><h1><b style="font-size: large; font-family: Arial, Helvetica, sans-serif;">Leave sooner,Drive slower,live longer.Keep calm and drive safety.Speed thrills but kills!.Drive,don't fly.</b></h1></div>
            <DIV>
                <body>
                    <fieldset>
                        <form action="brain.py">
                            <center><h4><b style="font-family:Arial, Helvetica, sans-serif ;color:red">*sorry not found!!</b></h4></center>
                            <input type="text" name="s" placeholder="choose start location">
                            <input type="text" name="e" placeholder="choose destination"><br><br><br><br>
                            <button><b>Submit</b></button>
                        </form>   
                    </fieldset>
                        
                    <center><iframe src="https://www.google.com/maps/embed?pb=!1m10!1m8!1m3!1d62194.141142593406!2d80.234495!3d13.027149!3m2!
                        1i1024!2i768!4f13.1!5e0!3m2!1sen!2sin!4v1678894864259!5m2!1sen!2sin"
                        width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></center>
                </body>
            </DIV>
        </body>
        </html>
        ''')

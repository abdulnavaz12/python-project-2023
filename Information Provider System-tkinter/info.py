from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
#from tkinter import  messagebox


my=Tk()
my.title("first page")
global e3

    
def about():
    us=Tk()
    us.title("first page")
    us.geometry('600x400')
    us.config(bg='#ffffff')
    text=Label(us,text='about us',font=('times',15,'bold'),bg='#227093',fg='white',width=350,height=2)
    text.pack(fill=X)
    text1=Label(us,text='''sorry not found''',font='arial 12 bold',bg='#ffffff',border=0)
    text1.place(x=0,y=70)

                

def hygiene():
    y=Toplevel(my)
    y.title("first page")
    y.geometry('1350x800')
    y.config(bg='#ffffff')
    scroll=Scrollbar(y)
    scroll.pack(side=RIGHT,fill=Y)
    text=Label(y,text='Health and Hygiene',font=('times',25,'bold'),bg='#227093',fg='white',width=500,height=3)
    text.pack(fill=X)
    e=Label(y,image=img11,bg='white')
    e.place(x=880,y=118)
    e1=Label(y,text='''*In modern times, it has become so important to take care of one’s health and hygiene.\n
*With the rising population levels, pollution levels, emission of harmful gases, it has to be a priority for everyone to maintain their health and hygiene.\n
*The health and hygiene essay guides you the different ways into which a person should be aware of his/her health.\n
*For the human body, health is a positive state where every part of the mind and body is in harmony.\n
*Additionally, it is also functioning and balancing the other parts. Thus, in other words,\n
*when all parts of the body are functioning well, this physical well-being state of the human body is called health.''',font='arial 9 bold',bg='#ffffff',border=0)
    e1.place(x=0,y=200)

    
def food():
    i=Toplevel(my)
    i.title("first page")
    i.geometry('1350x800')
    i.config(bg='#ffffff')
    scroll=Scrollbar(i)
    scroll.pack(side=RIGHT,fill=Y)
    text=Label(i,text='Benefits of Healthy Food',font=('times',25,'bold'),bg='#227093',fg='white',width=500,height=3)
    text.pack(fill=X)
    e=Label(i,image=img10,bg='white',border=0)
    e.place(x=880,y=118)
    e1=Label(i,text='''Healthy food does not have merely one but numerous benefits.\n
*It helps us in various spheres of life.\n
*Healthy food does not only impact our physical health but mental health too.

*When we intake healthy fruits and vegetables that are full of nutrients, we reduce the chances of diseases.\n
*For instance, green vegetables help us to maintain strength and vigor.\n
*In additioncertain healthy food items keep away long-term illnesses like diabetes and blood pressure.''',font='arial 12 bold',bg='#ffffff')
    e1.place(x=0,y=200)

    
def exercise():
    u=Toplevel(my)
    u.title("first page")
    u.geometry('1350x800')
    u.config(bg='#ffffff')
    scroll=Scrollbar(u)
    scroll.pack(side=RIGHT,fill=Y)
    text=Label(u,text='What is exercise and why is it important?',font=('times',25,'bold'),bg='#227093',fg='white',width=500,height=3)
    text.pack(fill=X)
    e=Label(u,image=img9,bg='white')
    e.place(x=880,y=118)
    e1=Label(u,text='''Exercise, \n*The training of the body to improve its function and enhance its fitness.
* Exercise is a component of physical activity.\n
* A successful exercise program incorporates a number of general principles of physical conditioning.\n
* Such programs can greatly benefit health.
*Exercise and physical activity are good for just about everyone, including older adults.\n 
*No matter your health and physical abilities, you can gain a lot by staying active.\n
*In fact, studies show that “taking it easy” is risky.\n
*Often, inactivity is more to blame than age when older people lose the ability to do things on their own.\n
*Lack of physical activity also can lead to more visits to the doctor, more hospitalizations, and more use of medicines for a variety of illnesses.

''',font='arial 10 bold',bg='#ffffff')
    e1.place(x=0,y=200)
    
def yoga():
    p=Toplevel(my)
    p.title("first page")
    p.geometry('1350x800')
    p.config(bg='#ffffff')
    scroll=Scrollbar(p)
    scroll.pack(side=RIGHT,fill=Y)
    text=Label(p,text='THE BENEFITS OF YOGA',font=('times',25,'bold'),bg='#227093',fg='white',width=500,height=3)
    text.pack(fill=X)
    e=Label(p,image=img5,bg='white')
    e.place(x=880,y=118)
    e1=Label(p,text='''*if you naturally take shallow inhales and long deep exhales, with regular,
                        \n* yoga breathing practice you will start to notice a change in your natural (involuntary) breathing pattern.
                        \n* Your natural breathing will eventually become more even – a similar length for inhale and exhale.
                        \n *This will have a knock-on positive impact in your health.''',font='arial 15 bold',bg='#ffffff')
    e1.place(x=0,y=200)

    


def login1():
    global e2,input_entry1
    o=e4.get()
    h=E2.get()
    us=cmb.get()
    rp=e1.get()
    
    
    if o==h and us=='ADMIN' and o!='' and h!='':
        global input_entry
        print('i am admin')
        r=Toplevel(my)
        r.geometry('1350x800')
        r.config(bg='#fff')
        b=e1.get()
        print(b)
        m1=Label(r,text='',bg='white',border=0,font='times 10 bold')
        m1.place(x=1245,y=120)
        m1.config(text='admin | '+b)
        r.resizable(0,0)        
        c1=Label(r,text='GOOD HEALTH INFORMATION PROVIDER SYSTEM',font=('times',25,'bold'),bg='#227093',fg='white',width=500,height=3)
        c1.pack(fill=X)
        m2=Label(r,image=img1,bg='white')#yogo
        m2.place(x=550,y=180)
        m3=Label(r,image=img2,bg='white')#gym
        m3.place(x=180,y=450)
        m4=Label(r,image=img3,bg='white')#hygen
        m4.place(x=950,y=450)
        m5=Label(r,image=img4,bg='white')#food
        m5.place(x=550,y=450)

        #buttons
        f1=Button(r,text='YOGA',bg='#227093',fg='white',font=('times',16,'bold'),width=15,command=yoga)
        f1.place(x=550,y=327)
        f2=Button(r,text='EXERCISE',bg='#227093',fg='white',font=('times',16,'bold'),width=15,command=exercise)
        f2.place(x=180,y=600)
        f3=Button(r,text='FOOD',bg='#227093',fg='white',font=('times',16,'bold'),width=15,command=food)
        f3.place(x=550,y=600)
        f3=Button(r,text='HYGIENE',bg='#227093',fg='white',font=('times',16,'bold'),width=15,command=hygiene)
        f3.place(x=950,y=600)
        
        def change():
            r.config(bg='black')
    
        def toggle():
            global input_entry,k2
            f1=Frame(r,width=250,height=800,bg='#227093')#,highlightbackground="black",highlightthicknes=1)
            f1.place(x=0,y=0)
            k1=Button(f1,text='?about us    ',font=('times',15,'bold'),fg='white',width=20,bg='#227093',command=about)
            k1.place(x=10,y=190)              
            k2=Button(f1,text='*night mode   ',font=('times',15,'bold'),fg='white',width=20,bg='#227093',command=change)
            k2.place(x=10,y=260)
            k3=Button(f1,text='[<-logout   ',font=('times',15,'bold'),fg='white',width=20,bg='#227093',command=main)
            k3.place(x=10,y=330)
            history_frame =Frame(f1,highlightbackground="#227093",highlightthicknes=1,width=400)
            history_frame.place(x=10,y=450)
            scrollbar = Scrollbar(history_frame)
            scrollbar.pack(side=RIGHT, fill=Y)
            history_listbox = Listbox(history_frame, yscrollcommand=scrollbar.set)
            history_listbox.pack(side=LEFT, fill=BOTH, expand=True)
            scrollbar.config(command=history_listbox.yview)
            input_entry = Entry(f1,font='times 10 bold',bg='#ffffff',fg='black')
            input_entry.place(x=10,y=615)
            scrollbar.config(command=history_listbox.yview)
            send_button = Button(f1, text="Send",bg='#0097e6',fg='white',activebackground='#0097e6',activeforeground='white')
            send_button.place(x=120,y=615)

                                
            #saend message to user
            def mychat():
                #input_entry=''
                if us!='USER':
                    print('user message')
                    message2=input_entry1.get()
                    if message2==message2:
                        history_listbox.insert(0,'user :'+message2)
                else:
                    history_listbox.insert(0,'none')


            def add_message(message):
                if message:
                    history_listbox.insert(0, message)
            def send_message():
               message = input_entry.get()
               if message:
                   add_message("you: " + message)
            
            send_button.config(command=send_message)
            show=Button(f1,text='show message',font='times 15 bold',command=mychat,width=20,bg='#227093',fg='white')
            show.place(x=10,y=400)
                    
            

            
            def dele():
                f1.destroy()
            s1=Button(f1,text='X',border=0,command=dele,bg='#227093',font=('times',25,'bold'),fg='white',activebackground='#227093',activeforeground='#227093')
            s1.place(x=5,y=90)
        c1=Button(r,command=toggle,text='=',border=0,font=('times',44,'bold'),fg='white',bg='#227093',height=0,width=0)
        c1.place(x=0,y=0)
    elif o==h and us=='USER' and o!='' and h!='':
        global input_entry
        s=Toplevel(my)
        print('iam user')
        s.title("user page")
        s.geometry('1400x800')
        s.config(bg='#ffffff')
        b=e1.get()
        m1=Label(s,text='',bg='white',border=0,font='times 10 bold')
        m1.place(x=1245,y=120)
        m1.config(text='user | '+b)
        #side frame
        #s.resizable(0,0)
        c1=Label(s,text='GOOD HEALTH INFORMATION PROVIDER SYSTEM',font=('times',25,'bold'),bg='#227093',fg='white',width=500,height=3)
        c1.pack(fill=X)
        m2=Label(s,image=img1,bg='white')#yogo
        m2.place(x=550,y=180)
        m3=Label(s,image=img2,bg='white')#gym
        m3.place(x=180,y=450)
        m4=Label(s,image=img3,bg='white')#hygen
        m4.place(x=950,y=450)
        m5=Label(s,image=img4,bg='white')#food
        m5.place(x=550,y=450)

        #buttons
        f1=Button(s,text='YOGA',bg='#227093',fg='white',font=('times',16,'bold'),width=15,command=yoga)
        f1.place(x=550,y=327)
        f2=Button(s,text='EXERCISE',bg='#227093',fg='white',font=('times',16,'bold'),width=15,command=exercise)
        f2.place(x=180,y=600)
        f3=Button(s,text='FOOD',bg='#227093',fg='white',font=('times',16,'bold'),width=15,command=food)
        f3.place(x=550,y=600)
        f3=Button(s,text='HYGIENE',bg='#227093',fg='white',font=('times',16,'bold'),width=15,command=hygiene)
        f3.place(x=950,y=600)
        def toggle():
            global input_entry1
            f1=Frame(s,width=250,height=800,bg='#227093')
            f1.place(x=0,y=0)
            k1=Button(f1,text='?about us    ',font=('times',15,'bold'),fg='white',width=20,bg='#227093',command=about)
            k1.place(x=10,y=190)
            k2=Button(f1,text='*feed back   ',font=('times',15,'bold'),fg='white',width=20,bg='#227093')
            k2.place(x=10,y=260)
            k3=Button(f1,text='[<-logout   ',font=('times',15,'bold'),fg='white',width=20,bg='#227093',command=main)
            k3.place(x=10,y=330)
            history_frame =Frame(f1,highlightbackground="black",highlightthicknes=1,width=400)
            history_frame.place(x=10,y=450)
            scrollbar = Scrollbar(history_frame)
            scrollbar.pack(side=RIGHT, fill=Y)
            history_listbox = Listbox(history_frame, yscrollcommand=scrollbar.set)
            history_listbox.pack(side=LEFT, fill=BOTH, expand=True)
            scrollbar.config(command=history_listbox.yview)
            input_entry1 = Entry(f1,font='times 10 bold',bg='#ffffff',fg='black')
            input_entry1.place(x=10,y=615)
            scrollbar.config(command=history_listbox.yview)
            send_button = Button(f1, text="Send",bg='#0097e6',fg='white',activebackground='#0097e6',activeforeground='white')
            send_button.place(x=120,y=615)
            

            def mychat1():
                print(c)
                if us!='ADMIN':
                    #c=cmb.get()
                    print('hi')
                    message2=input_entry.get()
                    if message2==message2:
                        history_listbox.insert(0,'admin: '+message2)
                else:
                   # print(input_entry.get())
                    history_listbox.insert(0,'none')

            show=Button(f1,text='show message',font='times 15 bold',command=mychat1,width=20,bg='#227093',fg='white')
            show.place(x=10,y=400)        
                     
            def add_message(message):
                history_listbox.insert(0, message)
            def send_message():
                message = input_entry1.get()
                if message:
                    add_message("you: " + message)
                    #input_entry1.delete(0, END)
            
            send_button.config(command=send_message)

            

            def dele():
                f1.destroy()
            s1=Button(f1,text='<',border=0,command=dele,bg='#227093',font=('times',25,'bold'),fg='white',activebackground='#227093',activeforeground='white')
            s1.place(x=5,y=90)
            
        c1=Button(s,command=toggle,text='=',border=0,font=('times',44,'bold'),fg='white',bg='#227093',height=0,width=0,activebackground='#227093',activeforeground='white')
        c1.place(x=0,y=0)
        
        ################################################################################################
   
    else:
        a4.config(text='*wrong password',fg='red')
        

def fra1():
    o=e4.get()
    b=e5.get()
    if o==b:
        print('hi')
        a7.config(text="register successfully",fg='green')
    else:
        a7.config(text='*password mismatch',fg='red')




#c=['abdul@gmail.com','abdul123@gmail.com']

def got():
    global e3,e4,e5,a7,E2,a4,e1
    #c1=e3.get()
    if cmb.get()=='ADMIN'or cmb.get()=='USER':
        global e2,e1
        v=Toplevel(my)
        v.title("ADMIN LOGIN")
        v.geometry("1000x600")
        v.config(bg='#fff')
        #v.config(bg='')
        ak=Label(v,image=img8,bg='white')
        ak.place(x=610,y=15)
        frame1=Frame(v,highlightbackground="black",highlightthicknes=2,padx=40,pady=80,bg='#fff')
        frame1.grid(row=0, column=1,padx=50,pady=50)
        #frame1 -labels-a1,a2,a3,a4
        a1=Label(frame1,text="REGISTRATION",font=('times',15,'bold'),fg='#57a1f8',pady=10,border=0,bg='#fff')
        a1.grid(columnspan=2)
        a2=Label(frame1,text="username      ",font=('times',15,'bold'),pady=10,border=0,bg='#fff')
        a2.grid(row=1,column=0)
        a3=Label(frame1,text="email        ",font=('times',15,'bold'),border=0,pady=10,bg='white')
        a3.grid(row=2,column=0)
        a4=Label(frame1,text="ph.no        ",font=('times',15,'bold'),pady=10,border=0,bg='white')
        a4.grid(row=3,column=0)
        a5=Label(frame1,text="password    ",font=('times',15,'bold'),border=0,bg='white')
        a5.grid(row=5,column=0)
        a6=Label(frame1,text="re-password",font=('times',15,'bold'),pady=10,border=0,bg='white')
        a6.grid(row=6,column=0)
        a7=Label(frame1,text='',font=('times',10,'bold'),pady=10,border=0,bg='white')
        a7.grid(row=9,column=0)
        
        #frame1-entrys-e1,e2,e3
        e1=Entry(frame1,font=('times',15),bg='white',border=0)
        e1.grid(row=1,column=1)
        f2=Frame(frame1,width=200,height=2,bg='black')
        f2.place(x=115,y=75)
        e2=Entry(frame1,font=('times',15),bg='white',border=0)#textvariable=var)
        e2.grid(row=2,column=1)
        f3=Frame(frame1,width=200,height=2,bg='black')
        f3.place(x=115,y=120)
        e3=Entry(frame1,font=('times',15),bg='white',border=0)
        e3.place(x=115,y=130)
        f4=Frame(frame1,width=200,height=2,bg='black')
        f4.place(x=115,y=155)
        
        
        e4=Entry(frame1,font=('times',15),bg='white',border=0,show='*')
        e4.place(x=115,y=160)
        f5=Frame(frame1,width=200,height=2,bg='black')
        f5.place(x=115,y=190)
        e5=Entry(frame1,font=('times',15),bg='white',border=0,show='*')
        e5.place(x=115,y=200)
        f5=Frame(frame1,width=200,height=2,bg='black')
        f5.place(x=115,y=228)
        
        #frame1-buttons-b1
        b1=Button(frame1,text='submit',bg='#57a1f8',fg='white',font=('times',10,'bold'),border=0,width=40,command=fra1)
        b1.place(x=10,y=270)
       
        #------------------------frame2-------------------------------------

        frame2=Frame(v,highlightbackground="black",highlightthicknes=2,width=200,padx=20,pady=20,bg='white')
        frame2.grid(row=0, column=6,padx=20,pady=50)
        #frame1 -labels-a1,a2,a3,a4
        a1=Label(frame2,text="LOGIN",font=('times',15,'bold'),fg='#57a1f8',pady=10,border=0,bg='white')
        a1.grid(columnspan=2)
        a2=Label(frame2,text="username  ",font=('times',15,'bold'),pady=10,border=0,bg='white')
        a2.grid(row=1,column=0)
        a3=Label(frame2,text="password  ",font=('times',15,'bold'),pady=10,border=0,bg='white')
        a3.grid(row=2,column=0)
        a4=Label(frame2,text="",font=('times',10,'bold'),pady=10,border=0,bg='white')
        a4.grid(row=5,column=0)
        #frame1-entrys-e1,e2,e3
        e1=Entry(frame2,font=('times',15),border=0,bg='white')
        e1.grid(row=1,column=1)
        f6=Frame(frame2,width=190,height=2,bg='black')
        f6.place(x=95,y=85)
        #var3=StringVar()
        E2=Entry(frame2,font=('times',15),border=0,bg='white',show='*')#textvariable=var3
        E2.grid(row=2,column=1)
        f7=Frame(frame2,width=190,height=2,bg='black')
        f7.place(x=95,y=128)
    
           
        b1=Button(frame2,text='LOGIN',bg='#57a1f8',fg='white',font=('times',8,'bold'),command=login1,width=18,border=0)
        b1.place(x=170,y=160)
        b2=Button(frame2,text='cancel',bg='#57a1f8',fg='white',font=('times',8,'bold'),command=v.destroy,width=18,border=0)
        b2.place(x=10,y=160)
#-------------------------------------------user page--------------------------------------------------------------------------------



global e3,e2,img5,cmb

def main():
    global cmb
    w=Toplevel(my)
    w.title('first page')
    w.geometry('925x500')
    w.config(bg="#fff")
    w.resizable(False,False)
    #image storage

    frame=Frame(w,width=600,height=600,bg='white')
    frame.place(x=465,y=70)
    l1=Label(frame,text="LOG IN",font=("times",17,"bold"),fg="#57a1f8",bg="white")
    l1.place(x=120,y=2)
    users=["SELECT","ADMIN","USER"]
    def on_enter(e):
        e1.delete(0,'end')
    def on_leave(e):
        name=e1.get()
        if name=='':
            e1.insert(0,'username')

    def on_enter1(e):
        e3.delete(0,'end')
    def on_leave1(e):
        name=e3.get()
        if name=='':
            e3.insert(0,'password')
    cmb=ttk.Combobox(frame,value=users,width=45)
    cmb.place(x=25,y=35)
    cmb.set("select")
    #image-w
    c=Label(w,image=img6,bg='white').place(x=50,y=40)

    e1=Entry(frame,fg='black',border=0,bg="white",font=("Microsoft YaHei uI Light",11))
    e1.place(x=30,y=90)
    e1.insert(0,'username')
    e1.bind('<FocusIn>',on_enter)
    e1.bind('<FocusOut>',on_leave)

    Frame(frame,width=295,height=2,bg='black').place(x=25,y=115)

    e3=Entry(frame,font=("Microsoft YaHei uI Light",11),bg='white',border=0,fg='black',width=25)
    e3.place(x=30,y=150)
    e3.insert(0,'password')
    e3.bind('<FocusIn>',on_enter1)
    e3.bind('<FocusOut>',on_leave1)

    Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)
    b1=Button(frame,width=42,text='LOGIN',bg='#57a1f8',fg='white',border=0,command=login1)
    b1.place(x=30,y=225)

    b2=Label(frame,pady=7,text="Don't have account?",bg="white",fg='black',font="times 10 bold")
    b2.place(x=75,y=270)

    b3=Button(frame,width=6,text="register",border=0,bg="white",fg='#57a1f8',font="times 10 bold",command=got,activebackground='white',activeforeground='#57a1f8')
    b3.place(x=212,y=276)





#my.geometry('427x250')
my.config(bg='#16a085')
c=Image.open('VV.jpg')
c1=c.resize((190,140))
p=Image.open('dum1.jpg')
p1=p.resize((190,140))
t=Image.open('hand.jpg')
t1=t.resize((190,140))
i=Image.open('jhonny (3).jpg')
i1=i.resize((190,140))
y=Image.open('yoga1.jpg')
y1=y.resize((400,400))
r=Image.open('hulk1.jpg')
r1=r.resize((400,400))
g=Image.open('blue.jpg')
g1=g.resize((1200,660))
k=Image.open('loco.jpg')#new
k1=k.resize((150,140))
e=Image.open('exer.jpg')#new
e1=e.resize((400,400))
a=Image.open('vegfood.jpeg')#new
a1=a.resize((400,400))
x=Image.open('hyge.jpg')#new
x1=x.resize((400,400))

#image variables
img1=ImageTk.PhotoImage(c1)
img2=ImageTk.PhotoImage(p1)
img3=ImageTk.PhotoImage(t1)
img4=ImageTk.PhotoImage(i1)
img5=ImageTk.PhotoImage(y1)
img6=ImageTk.PhotoImage(r1)
img7=ImageTk.PhotoImage(g1)
img8=ImageTk.PhotoImage(k1)#new
img9=ImageTk.PhotoImage(e1)#new
img10=ImageTk.PhotoImage(a1)#new
img11=ImageTk.PhotoImage(x1)#new

#################################main window#################################################
width_of_window=427
height_of_window=250
screen_width=my.winfo_screenwidth()
screen_height=my.winfo_screenheight()
x_coordinate=(screen_width/2)-(width_of_window/2)
y_coordinate=(screen_height/2)-(height_of_window/2)
my.geometry("%dx%d+%d+%d"%(width_of_window,height_of_window,x_coordinate,y_coordinate))
Label(my,text="welcome",fg='black',border=0,width=20,bg='#1abc9c',font=('times',20,'bold')).place(x=47,y=80)

b1=Button(my,width=10,text='GET STARTED',command=main,fg='white',bg='#1abc9c',activebackground='#1abc9c',activeforeground='white')
b1.place(x=170,y=200)
my.mainloop()


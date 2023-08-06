from tkinter import *
from PIL import ImageTk,Image
from tkinter import  messagebox
w=Tk()
w.title("quiz")
w.geometry('500x500')

score=[]

def total():
    global score
    j=Toplevel(w)
    j.geometry('500x500')
    n=Label(j,image=img5)
    n.pack(fill='both',expand='yes',side='bottom')
    a=str(len(score))
    l=Label(j,text='TOTAL SCORE : '+a,font='times 20 bold',bg='white')
    l.place(x=100,y=220)
    messagebox.showinfo('message','submited successfully')
def yes(x):
    global score
    if x==1:
        score.append(1)
        #print(score)

def quiz2():
    global c
    f=Toplevel(w)
    f.geometry('500x500')
    l11=Label(f,text='select the correct answer!',font='arial 15 bold',bg='green',width=130)
    l11.pack()
    #IMAGE
    l33=Label(f,image=img4,font='arial 15 bold')
    l33.pack(padx=15,pady=10,side=TOP)
    l22=Label(f,text='Q3.GUESS WHICH CAR BRAND MODEL THIS IS?',font='arial 15 bold',fg='black')
    l22.place(x=20,y=240)
    c=IntVar()
    c.set('none')
    r1 = Radiobutton(f,text="1.BMW",font='arial 15 bold',variable=c,value='1',command=lambda :yes(0))
    #r1.deselect()
    r1.place(x=40,y=310)
    r2 = Radiobutton(f,text="2.AUDI", font='arial 15 bold',variable=c,value='2',command=lambda :yes(0))
    #r2.deselect()
    r2.place(x=40,y=350)
    r3 = Radiobutton(f,text="3.TESLA", font='arial 15 bold',variable=c, value ='3',command=lambda :yes(1))
    r3.place(x=40,y=400)
    
    b3=Button(f,text='submit',font='time 10 bold',bg='green',fg='white',activebackground='#32ff7e',command=total)
    b3.place(x=250,y=450)
    b4=Button(f,text="close",font='time 10 bold',bg='green',fg='white',activebackground='#32ff7e',command=f.destroy)
    b4.place(x=180,y=450)


    
    
     
def quiz1():#third window
    global b
    u=Toplevel(w)
    u.title('tk2')
    u.geometry('500x500')
    #label
    x1=Label(u,text='select the correct answer!',font='arial 15 bold',bg='green',width=130)
    x1.pack()
    x2=Label(u,text='Q2.WHO IS THIS..?',font='arial 15 bold',fg='black')
    x2.place(x=40,y=270)
    #image
    x3=Label(u,image=img3,font='arial 15 bold')
    x3.pack(padx=15,pady=10,side=TOP)
    
    
    #variable
    b=IntVar()
    b.set('none')
    x=1

    #radio button
    r1 = Radiobutton(u,text="1.LEONARDO DICAPRIO",font='arial 15 bold',variable=b,value='3',command=lambda :yes(0))
    r1.place(x=40,y=310)
    r2 = Radiobutton(u,text="2.TOM CRUISE", font='arial 15 bold',variable=b,value='2',command=lambda :yes(0))
    r2.place(x=40,y=350)
    r3 = Radiobutton(u,text="3.JONNY DEPP", font='arial 15 bold',variable=b, value ='1',command=lambda :yes(1))
    r3.place(x=40,y=400)
    
    #button
    b3=Button(u,text='next',font='time 10 bold',bg='green',fg='white',activebackground='#32ff7e',command=quiz2,relief=RAISED)
    b3.place(x=250,y=450)
    b4=Button(u,text="close",font='time 10 bold',bg='green',fg='white',activebackground='#32ff7e',command=u.destroy,relief=RAISED)
    b4.place(x=180,y=450)
    
    u.mainloop() 
        
  
    
    
    
def quiz():#second window
    global a,i,result
    i=result=0
    f=Toplevel(w)
    f.title('tk1')
    f.geometry('500x500')
    #label
    m1=Label(f,text='select the correct answer!',font='arial 20 bold',bg='green',width=130)
    m1.pack()
    #image
    m2=Label(f,image=img2,font='arial 15 bold')
    m2.pack(padx=15,pady=10,side=TOP)
    m3=Label(f,text='Q1.which PLANT IS IN THE PICTURE?',font='arial 15 bold',fg='black')
    m3.place(x=40,y=250)
    #variable
    a=IntVar()
    a.set('none')
    
    #radio buttons
    r1 = Radiobutton(f,text="1.SUNFLOWER",font='arial 15 bold',variable=a,value='3',command=lambda :yes(1))
    r1.place(x=40,y=310)
    r2 = Radiobutton(f,text="2.ROSE", font='arial 15 bold',variable=a,value='2',command=lambda :yes(0))
    r2.place(x=40,y=355)
    r3 = Radiobutton(f,text="3.TULIP", font='arial 15 bold',variable=a, value = '1',command=lambda :yes(0))
    r3.place(x=40,y=400)
    #buttons
    b3=Button(f,text='next',font='time 10 bold',bg='green',fg='white',activebackground='#32ff7e',relief=RAISED,command=quiz1)
    b3.place(x=250,y=450)
    b4=Button(f,text="close",font='time 10 bold',bg='green',fg='white',activebackground='#32ff7e',command=f.destroy,relief=RAISED)
    b4.place(x=180,y=450)
   
    
    f.mainloop() 

#first window
#w=Tk()
#w.geometry('500x500')
#image
c=Image.open('quiz4.jpg')
c1=c.resize((1200,660))
p=Image.open('sun.jpg')
p1=p.resize((500,200))
t=Image.open('jhonny.jpg')
t1=t.resize((500,200))
i=Image.open('TESLA2.jpeg')
i1=i.resize((500,200))
y=Image.open('score.jpg')
y1=y.resize((1000,500))

img1=ImageTk.PhotoImage(c1)
img2=ImageTk.PhotoImage(p1)
img3=ImageTk.PhotoImage(t1)
img4=ImageTk.PhotoImage(i1)
img5=ImageTk.PhotoImage(y1)
#label
l1=Label(w,text='WELCOME TO SIMPLE QUIZ',font='arial 15 bold',bg='green',width=130)
l1.pack()
l2=Label(w,image=img1)
l2.pack(fill='both',expand='yes',side='bottom')
#buttons
b1=Button(w,text='START QUIZZ',font='time 15 bold',bg='green',fg='white',activebackground='#32ff7e',relief=RAISED,command=quiz)
b1.place(x=165,y=290)
b2=Button(w,text="close",font='time 13 bold',bg='green',fg='white',activebackground='#32ff7e',command=w.destroy,relief=RAISED)
b2.place(x=210,y=360)

w.mainloop()

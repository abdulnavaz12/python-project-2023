from tkinter import *
def add():
    e3.delete(0,END)
    f1=e1.get()
    f2=e2.get()
    c=(int(f1)+int(f2))
    e3.insert(0,c)
def sub():
    e3.delete(0,END)
    f1=e1.get()
    f2=e2.get()
    c=(int(f1)-int(f2))
    e3.insert(0,c)
def mul():
    e3.delete(0,END)
    f1=e1.get()
    f2=e2.get()
    c=(int(f1)*int(f2))
    e3.insert(0,c)
def div():
    e3.delete(0,END)
    f1=e1.get()
    f2=e2.get()
    c=(int(f1)/int(f2))
    e3.insert(0,c)
def modulus():
    e3.delete(0,END)
    f1=e1.get()
    f2=e2.get()
    c=(int(f1)%int(f2))
    e3.insert(0,c)
def exp():
    e3.delete(0,END)
    f1=e1.get()
    f2=e2.get()
    c=(int(f1)**int(f2))
    e3.insert(0,c)
w=Tk()
w.title('cal')
w.geometry("500x500")
w.config(bg='#dff9fb')

l1=Label(w,text="SIMPLE CALCULATOR",font='times 15 bold',bg='lime',width='50')
l1.pack()
l2=Label(w,text="TYPE-1:",font=('times 15 bold'),bg='#1B9CFC')
l2.place(x=40,y=50)
e1=Entry(w,font='times 10 bold',bg='#fff200')
e1.place(x=40,y=90)
l3=Label(w,text="TYPE-2:",font=('times 15 bold'),bg='#1B9CFC')
l3.place(x=330,y=50)
e2=Entry(w,font='times 10 bold',bg='#fff200')
e2.place(x=330,y=90)
l4=Label(w,text='RESULT:',font='times 15 bold',bg='#575fcf')
l4.place(x=100,y=160)
e3=Entry(w,text="",font='times 10 bold',bg='#fff200')
e3.place(x=200,y=160)
b1=Button(w,text="+",font='times 20 bold',width='8',bg='blue',command=add)
b1.place(x=40,y=200)
b2=Button(w,text="-",font='times 20 bold',width='8',bg='pink',command=sub)
b2.place(x=185,y=200)
b3=Button(w,text="*",font='times 20 bold',width='8',bg='green',command=mul)
b3.place(x=330,y=200)
b4=Button(w,text="/",font='times 20 bold',width='8',bg='#8e44ad',command=div)
b4.place(x=40,y=300)
b5=Button(w,text="%",font='times 20 bold',width='8',bg='magenta',command=modulus)
b5.place(x=185,y=300)
b6=Button(w,text="**",font='times 20 bold',width='8',bg='yellow',command=exp)
b6.place(x=330,y=300)
b7=Button(w,text="close",font='times 15 bold',width='4',bg='red',command=w.destroy)
b7.place(x=330,y=370)










from tkinter import *
from tkinter import messagebox
w=Tk()
w.title("my_f_window")
def cut():
    global balance
    
    #balance=1000
    amount = int(o2.get())
    if amount > balance:
        messagebox.showerror("Error", "Insufficient Balance")
    else:
        balance -= amount
        g5.config(text="Balance: Rs "+str(balance)+'/-')
        messagebox.showinfo("Success", "Withdrawal Successful")


    
def yes():
    global balance,c1
    #balance=1000
    balance=c1
    v=d1.get()
    print(v)
    amount = v
    c1+= int(amount)
    balance=c1
    #c=balance
    g5.config(text="Balance: Rs "+str(balance)+'/-')
    messagebox.showinfo("Success", "Deposit Successful")

   
    
    
def withdraw():
    global o2 
    q=Tk()
    q.geometry('500x500')
    x1=Label(q,text='WITHDRAW',font='arial 12 bold',fg='white',bg='#0a3d62')
    x1.place(x=40,y=60)
    x2=Label(q,text='ENTER THE AMOUNT:',font='arial 20 bold',fg='white',bg='#0a3d62')
    x2.place(x=40,y=100)
    o2=Entry(q,font=("arial",15),bg='silver',selectbackground='blue',selectforeground='white',text='')
    o2.place(x=40,y=160)
    j3=Button(q,text='confirm',font='times',bg='green',command=cut)
    j3.place(x=100,y=300)
    f1=Button(q,text="ok",font='arial 12 bold',bg='green',command=q.destroy)
    f1.place(x=60,y=300)
def deposit():
    global sco,c,balance
    global d1,num1
    s=Tk()
    s.geometry('500x500')
    sco=[]
    c=0
    x1=Label(s,text='DEPOSIT',font='arial 12 bold',fg='white',bg='#0a3d62')
    x1.place(x=40,y=60)
    x2=Label(s,text='ENTER THE AMOUNT:',font='arial 20 bold',fg='white',bg='#0a3d62')
    x2.place(x=40,y=100)
    #var=StringVar()
    d1=Entry(s,font=("arial",15),bg='silver',selectbackground='blue',selectforeground='white',text='')
    d1.place(x=40,y=160)
    o3=Button(s,text='confirm',font='times',bg='green',command=yes)
    o3.place(x=100,y=300)
    f1=Button(s,text="ok",font='arial 12 bold',bg='green',command=s.destroy)
    f1.place(x=60,y=300)
    
    

    

def check(c1):
    global x3,g5
    z=Tk()
    z.geometry('500x500')
    x1=Label(z,text='BALANCE',font='arial 12 bold',fg='white',bg='#0a3d62')
    x1.place(x=40,y=60)
    x2=Label(z,text='AMOUNT IS: ',font='arial 20 bold',fg='white',bg='#0a3d62')
    x2.place(x=40,y=100)
    x3=Entry(z,text='',font='arial 20 bold',fg='white',bg='#0a3d62')
    x3.place(x=40,y=190)
    f1=Button(z,text="ok",font='arial 11 bold',bg='green',fg='white',command=z.destroy)
    f1.place(x=40,y=300)
    c1=balance
    b=g5
    x3.insert(0,c1)
    
    
def confirm():
    global g1,m,g5,l,balance,c1
    s1=e11.get()
    #s2=e1.get()
    #s3=e33.get()
    s4=e3.get()
    k1=n1.get()
    k2=n3.get()
    if ((s1==s4 and str(k1)=="IB12345") or(str(k1)=="IB12345" and k2==s1)):
        v=Tk()
        v.title("my_t_window")
        v.geometry("500x500")
        
    
        g1=Label(v,text="CUR. ",font='arial 11 bold',bg='white')
        g1.place(x=270,y=20)
        
        g2=Label(v,text="select your option",font='arial 20 bold',bg='#0a3d62',width=20,fg='white')
        g2.place(x=40,y=90)
        a1=Button(v,text="deposit",bg="#0a3d62",fg='white',font="times 12 bold",activebackground='green',activeforeground='yellow',width=37,command=deposit)
        a1.place(x=40,y=140)

        a2=Button(v,text="withdraw",width=37,bg="#0a3d62",fg='white',font="times 12 bold",activebackground='green',activeforeground='yellow',command=withdraw)
        a2.place(x=40,y=190)

        #a3=Button(v,text="check balance",width=37,bg="#0a3d62",fg='white',font="times 12 bold",activebackground='green',activeforeground='yellow',command=check)
        #a3.place(x=40,y=240)
       
        balance=1000
        c1=balance
        g5=Label(v,text='Balance: Rs.'+str(c1)+'/-',font='arial 11 bold',bg='white')
        g5.place(x=310,y=20)
        #m=Entry(v,text='',font='times 10 bold',bg='#fff200')
        #m.place(x=400,y=20)
        g6=Label(v,text='constraint =5 min            ',font='arial 11 bold',bg='white')
        g6.place(x=270,y=50)       
        a3=Button(v,text="check balance",width=37,bg="#0a3d62",fg='white',font="times 12 bold",activebackground='green',activeforeground='yellow',command=lambda :check(c1))
        a3.place(x=40,y=240)
        v.after(300000,v.destroy)
        
        
    else:
        l22.config(text="*please enter correct details")
                
                
def new():
    global n1,n3,l22
    s3=e33.get()
    s1=e11.get()
    
    if s3==s1:
        w=Tk()
        w.title("my_f_window")
        w.geometry("500x500")
        #w.config(bg="silver")
        l1=Label(w,text="MY BANK ATM",font=("arial 15 bold"),width='200',fg="white",bg="#0a3d62")
        l1.pack()
        l2=Label(w,text="ACCOUNT NO : ",font="times 13 bold")
        l2.place(x=40,y=100)

        n1=Entry(w,fg='black',bg="silver",font=('times',16),selectbackground='blue',selectforeground='white')
        n1.place(x=200,y=100)

        l3=Label(w,text="PIN   : ",font='times 13 bold')
        l3.place(x=115,y=160)

        n3=Entry(w,font=("arial",15),bg='silver',show="*",selectbackground='blue',selectforeground='white')
        n3.place(x=200,y=160)

        b1=Button(w,text="CONFIRM",bg="#0a3d62",fg='white',font="times 10 bold",activebackground='green',activeforeground='yellow',command=confirm)
        b1.place(x=200,y=250)

        b2=Button(w,text="EXIT",width='8',bg="#0a3d62",fg='white',font="times 10 bold",activebackground='green',activeforeground='yellow',command=w.destroy)
        b2.place(x=220,y=450)

        b3=Button(w,text="FORGOT PIN?",width='20',bg="#0a3d62",fg='white',font="times 10 bold",activebackground='green',activeforeground='yellow',command=forgot)
        b3.place(x=280,y=300)

        l22=Label(w,font="times 15 bold",fg="red")
        l22.place(x=60,y=60)
    else:
        l23.config(text="*please enter correct details")


    

def forgot():
    global e11,e33,l23
    n=Tk()
    n.title("my_s_window")
    n.geometry("500x500")
    l1=Label(n,text="PLEASE ENTER THE NEW PIN HERE",font="arial 15 bold",width='200',fg="white",bg="#0a3d62")
    l1.pack()
    l2=Label(n,text="ENTER NEW PIN : ",font="times 13 bold",fg="black")
    l2.place(x=20,y=100)
    e11=Entry(n,width='35',bg="silver",font="times 10 bold",show='*')
    e11.place(x=180,y=100)
    l3=Label(n,text="RE-ENTER PIN : ",font="times 13 bold",fg="black")
    l3.place(x=30,y=160)
    e33=Entry(n,width='35',bg="silver",font="times 10 bold",show='*')
    e33.place(x=180,y=160)
    #b1=Button(n,text="SIGN UP",width='10',bg="#0a3d62",fg='white',command=mas)
    #b1.place(x=60,y=290)
    b2=Button(n,text="CONFIRM",width='10',bg="#0a3d62",fg='white',activebackground='green',activeforeground='yellow',command=new)
    b2.place(x=150,y=290)
    b3=Button(n,text="EXIT",width='8',bg="#0a3d62",fg='white',activebackground='green',activeforeground='yellow',command=n.destroy)
    b3.place(x=300,y=290)
    #l22=Label(n,text="",font="times 10 bold",fg="red")
    #l22.place(x=60,y=60)
    l23=Label(n,text="",font="times 10 bold",fg="red")
    l23.place(x=60,y=60)
       
        
global e1,e3    

w.geometry("500x500")
#w.config(bg="silver")
l1=Label(w,text="MY BANK ATM",font=("arial 15 bold"),width='200',fg="white",bg="#0a3d62").pack()
l2=Label(w,text="ACCOUNT NO : ",font="times 13 bold")
l2.place(x=40,y=100)

e1=Entry(w,fg='black',bg="silver",font=('times',16),selectbackground='blue',selectforeground='white')
e1.place(x=200,y=100)

l3=Label(w,text="PIN   : ",font='times 13 bold')
l3.place(x=115,y=160)

e3=Entry(w,font=("arial",15),bg='silver',show="*",selectbackground='blue',selectforeground='white')
e3.place(x=200,y=160)

b1=Button(w,text="CONFIRM",bg="#0a3d62",fg='white',font="times 10 bold",activebackground='green',activeforeground='yellow',command=confirm)
b1.place(x=200,y=250)

b2=Button(w,text="EXIT",width='8',bg="#0a3d62",fg='white',font="times 10 bold",activebackground='green',activeforeground='yellow',command=w.destroy)
b2.place(x=220,y=450)

b3=Button(w,text="FORGOT PIN?",width='20',bg="#0a3d62",fg='white',font="times 10 bold",activebackground='green',activeforeground='yellow',command=forgot)
b3.place(x=280,y=300)


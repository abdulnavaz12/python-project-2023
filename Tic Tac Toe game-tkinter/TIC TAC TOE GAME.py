from tkinter import *
from tkinter import messagebox
root=Tk()
root.geometry('500x500')
root.config(bg='#006266')
def TIC():
    w=Tk()
    w.geometry('375x340')
    def play1():
        global take
        if b1['text']=='':
            if take==1:
                take=2
                b1['text']='X'
            elif take==2:
                take=1
                b1['text']='O'
            check()

    def play2():
        global take
        if b2['text']=='':
            if take==1:
                take=2
                b2['text']='X'
            elif take==2:
                take=1
                b2['text']='O'
            check()

    def play3():
        global take
        if b3['text']=='':
            if take==1:
                take=2
                b3['text']='X'
            elif take==2:
                take=1
                b3['text']='O'
            check()
        
    def play4():
        global take
        if b4['text']=='':
            if take==1:
                take=2
                b4['text']='X'
            elif take==2:
                take=1
                b4['text']='O'
            check()

    def play5():
        global take
        if b5['text']=='':
            if take==1:
                take=2
                b5['text']='X'
            elif take==2:
                take=1
                b5['text']='O'
            check()

            
    def play6():
        global take
        if b6['text']=='':
            if take==1:
                take=2
                b6['text']='X'
        elif take==2:
            take=1
            b6['text']='O'
        check()
        
    def play7():
        global take
        if b7['text']=='':
            if take==1:
                take=2
                b7['text']='X'
            elif take==2:
                take=1
                b7['text']='O'
            check()
        
    def play8():
        global take
        if b8['text']=='':
            if take==1:
                take=2
                b8['text']='X'
            elif take==2:
                take=1
                b8['text']='O'
            check()
        
    def play9():
        global take
        if b9['text']=='':
            if take==1:
                take=2
                b9['text']='X'
            elif take==2:
                take=1
                b9['text']='O'
            check()

   
    def check():
        global flag
        btn1=b1["text"]
        btn2=b2["text"]
        btn3=b3["text"] 
        btn4=b4["text"]
        btn5=b5["text"]
        btn6=b6["text"]
        btn7=b7["text"]
        btn8=b8["text"]
        btn9=b9["text"]
        flag=flag+1;
        if btn1==btn2 and btn2==btn3 and btn1=='O' or btn1==btn2 and btn2==btn3 and btn1=='X':
            print(btn1)
            win(b1["text"])
        if btn4==btn5 and btn5==btn6 and btn4=='O' or btn4==btn5 and btn5==btn6 and btn4=='X':
            win(b4["text"])
        if btn7==btn8 and btn8==btn9 and btn7=='O' or btn7==btn8 and btn8==btn9 and btn7=='X':
            win(b7["text"])
        if btn1==btn4 and btn4==btn7 and btn1=='O' or btn1==btn4 and btn4==btn7 and btn1=='X':
            win(b1["text"])
        if btn2==btn5 and btn5==btn8 and btn2=='O' or btn2==btn5 and btn5==btn8 and btn2=='X':
            win(b2["text"])
        if btn3==btn6 and btn6==btn9 and btn3=='O' or btn3==btn6 and btn6==btn9 and btn3=='X':
            win(b3["text"])
        if btn1==btn5 and btn1==btn9 and btn1=='O' or btn1==btn5 and btn1==btn9 and btn1=='X':
            win(b1["text"])
        if btn7==btn5 and btn7==btn3 and btn7=='O' or btn7==btn5 and btn7==btn3 and btn7=='X':
            win(b7["text"])
        if flag==10:
            messagebox.showinfo('tie','match tied!!! try again:)')
            w.destroy()
    def win(player):
        ans="game completed "+player+" win"
        messagebox.showinfo("congratulations",ans)
        w.destroy()


    b1=Button(w,text='',width=15,height=6,borderwidth=5,bg='lime',command=play1)
    b1.grid(row=0,column=0)
    b2=Button(w,text='',width=15,height=6,borderwidth=5,bg='lime',command=play2)
    b2.grid(row=0,column=1)
    b3=Button(w,text='',width=15,height=6,borderwidth=5,bg='lime',command=play3)
    b3.grid(row=0,column=2)
    b4=Button(w,text='',width=15,height=6,borderwidth=5,bg='lime',command=play4)
    b4.grid(row=1,column=0)
    b5=Button(w,text='',width=15,height=6,borderwidth=5,bg='lime',command=play5)
    b5.grid(row=1,column=1)
    b6=Button(w,text='',width=15,height=6,borderwidth=5,bg='lime',command=play6)
    b6.grid(row=1,column=2)
    b7=Button(w,text='',width=15,height=6,borderwidth=5,bg='lime',command=play7)
    b7.grid(row=2,column=0)
    b8=Button(w,text='',width=15,height=6,borderwidth=5,bg='lime',command=play8)
    b8.grid(row=2,column=1)
    b9=Button(w,text='',width=15,height=6,borderwidth=5,bg='lime',command=play9)
    b9.grid(row=2,column=2)
take=1
flag=1

def cal():
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

l1=Label(root,text='select option',font='times 30 bold',bg='green',fg='black',width=35)
l1.pack(fill=X)
bs1=Button(root,text="calculator",font='times 15 bold',bg='#0984e3',command=cal)
bs1.place(x=80,y=70)
bs2=Button(root,text="TIC TOC TOE GAME",font='times 15 bold',bg='#00cec9',command=TIC)
bs2.place(x=80,y=150)









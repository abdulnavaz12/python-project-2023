from tkinter import *
from PIL import ImageTk,Image
from bs4 import BeautifulSoup
from tkinter import ttk
import requests
import csv
import pandas as pd
import webbrowser

'''
keyword="iphone"
url='https://www.flipkart.com/search?q='+keyword+''
page=requests.get(url)
#print(page)
soup= BeautifulSoup(page.text,'html.parser')
product= soup.find('div',attrs={'class':'_4rR01T'})
#print(product.text)
data=soup.find_all('div',attrs={'class':'_4rR01T'})
c=1
for phone in data:
    print(c,'--',phone.text)
    c+=1
#print(c,'--',phone.text)
#print(phone.text)

'''
def web1():
        webbrowser.open_new('https://www.flipkart.com/search?q='+key+'')
def web2():
        webbrowser.open_new('https://www.amazon.in/s?k='+key2+'')


def model():
        global e1,cmb,cmb1
        keyword=e1.get()
        #print(keyword)
        n=Toplevel(a)
        n.title("second")
        n.config(bg='#ffffff')
        width_of_window=800
        height_of_window=500
        screen_width=n.winfo_screenwidth()
        screen_height=n.winfo_screenheight()
        x_coordinate=(screen_width/2)-(width_of_window/2)
        y_coordinate=(screen_height/2)-(height_of_window/2)
        n.geometry("%dx%d+%d+%d"%(width_of_window,height_of_window,x_coordinate,y_coordinate))
        url='https://www.flipkart.com/search?q='+keyword+''
        url2='https://www.amazon.in/s?k='+keyword+''
        HEADERS=({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.51'})
        page=requests.get(url)
        webpage=requests.get(url2,headers=HEADERS)
        soup2= BeautifulSoup(webpage.content,features="lxml")
        print(soup2)
        soup= BeautifulSoup(page.text,'html.parser')
        product= soup.find('div',attrs={'class':'_4rR01T'})
        data=soup.find_all('div',attrs={'class':'_4rR01T'})
        mydata=[]
        for phone in data:
            mydata.append(phone.text)
        data2=soup2.find_all('span',attrs={'class':'a-size-medium a-color-base a-text-normal'})
        mydata2=[]
        #print(data2)
        for phone in data2:
            mydata2.append(phone.text)
        #print(mydata2)
        l1=Label(n,text="SELECT YOUR PRODUCT MODELS",font=('times',15,'bold'),bg='#ffffff')
        l1.pack(padx=20,pady=20)
        l4=Label(n,text="FLIPKART :    ",font=('times',15,'bold'),bg='#ffffff')
        l4.place(x=150,y=100)
        l5=Label(n,text="AMAZON :    ",font=('times',15,'bold'),bg='#ffffff')
        l5.place(x=150,y=200)
        cmb=ttk.Combobox(n,value=mydata,width=50,font=('times',10,'bold'))
        cmb.place(x=200,y=140)
        cmb.set("select model")
        cmb1=ttk.Combobox(n,value=mydata2,width=50,font=('times',10,'bold'))
        cmb1.place(x=200,y=240)
        cmb1.set("select model")
        b20=Button(n,text="Check",font=('times',15,'bold'),bg="black",fg="white",width=11,command=content)
        b20.place(x=450,y=350)
        
        
    
def content():
    global cmb,cmb1,key,key2
    key=cmb.get()
    key2=cmb1.get()
    if True:
        b=Toplevel(a)
        b.title("third")
        b.geometry("1400x800")
        
        #flipkart
        url='https://www.flipkart.com/search?q='+key+''
        url2='https://www.amazon.in/s?k='+key2+''
        #HEADERS=({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67'})
        #page=requests.get(url)
        HEADERS=({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.51'})
        page=requests.get(url)
        webpage=requests.get(url2,headers=HEADERS)
        soup2= BeautifulSoup(webpage.content,features="lxml")
        #print(page)
        soup= BeautifulSoup(page.text,'html.parser')
        product= soup.find('div',attrs={'class':'_4rR01T'})
        #print(product.text)
        price= soup.find('div',attrs={'class':"_30jeq3 _1_WHN1"})
        rate= soup.find('div',attrs={'class':"_3LWZlK"})
        fee= soup.find('div',attrs={'class':"_2Tpdn3"})
        
     
        frame1=Frame(b,highlightbackground="black",highlightthicknes=2,bg='#ffffff')
        frame1.pack(side=RIGHT,expand=True,fill=BOTH)
        l1=Label(frame1,text="PRODUCT DETAILS",font=('times',15,'bold'),bg='#ffffff')
        l1.pack(padx=20,pady=20)
        ak=Label(frame1,image=img1,bg='white')
        ak.place(x=20,y=70)
        b1=Button(frame1,text="visit page",font=('times',15,'bold'),width=20,command=web1,bg='#40c4ff',fg='white')
        b1.place(x=300,y=120)
        l2=Label(frame1,text="product:   "+product.text,font=('times',18,'bold'),bg='#ffffff')
        l2.place(x=65,y=250)
        l3=Label(frame1,text="   price:     "+price.text,font=('times',20,'bold'),width=15,bg='#ffffff')
        l3.place(x=40,y=320)
        l4=Label(frame1,text="Rating:    "+rate.text,font=('times',17,'bold'),bg='#ffffff')
        l4.place(x=70,y=400)
        l5=Label(frame1,text="delivery fee: "+fee.text,font=('times',17,'bold'),bg='#ffffff')
        l5.place(x=60,y=480)
        b20=Button(frame1,text="Back",font=('times',15,'bold'),bg="black",fg="white",command=b.destroy)
        b20.place(x=550,y=610)
        s=cmb.get()
        #variables
        a1=product.text
        b1=price.text
        c1=rate.text
        d1=fee.text
        
        #amazon
        frame2=Frame(b,highlightbackground="black",highlightthicknes=2,bg='#ffffff')
        frame2.pack(side=RIGHT,expand=True,fill=BOTH)
        ap=Label(frame2,image=img2,bg='white')
        ap.place(x=20,y=70)
        b2=Button(frame2,text="visit page",font=('times',15,'bold'),width=20,command=web2,bg='#40c4ff',fg='white')
        b2.place(x=300,y=120)
        l2=Label(frame2,text="PRODUCT DETAILS",font=('times',15,'bold'),bg='#ffffff')
        l2.pack(padx=20,pady=20)
        product2= soup2.find('span',attrs={'class':'a-size-medium a-color-base a-text-normal'})
        price= soup2.find('span',attrs={'class':"a-price-whole"})
        rate=soup2.find('span',attrs={'class':"a-icon-alt"})
        fee= soup2.find('span',attrs={'aria-label':"FREE Delivery by Amazon"})
        
        l7=Label(frame2,text="product:   "+key2,font=('times',18,'bold'),bg='#ffffff')
        l7.place(x=65,y=250)
        l8=Label(frame2,text="      price:      "+price.text,font=('times',20,'bold'),width=15,bg='#ffffff')
        l8.place(x=20,y=320)
        l9=Label(frame2,text="Rating  : "+rate.text,font=('times',17,'bold'),bg='#ffffff')
        l9.place(x=55,y=400)
        l10=Label(frame2,text="delivery fee: "+fee.text,font=('times',17,'bold'),bg='#ffffff')
        l10.place(x=55,y=480)
        #variables---------
        a2=key2
        b2=price.text
        c2=rate.text
        d2=fee.text
        

        #file------------
        dataframe1=({'product_name':a1,'price':b1,'Rating':c1,'delivery_fee':d1,'product_from':'flipkart'},{'product_name':a2,'price':b2,'Rating':c2,'delivery_fee':d2,'product_from':'amazon'})
        dataframe=pd.DataFrame(dataframe1)
        #print(dataframe)
        #dataframe.to_csv('convergent.csv')
#----------------------------------------------------------------------------------------------------------------------------------------        


    

a=Tk()
a.title("firstpage")
a.config(bg='#ffffff')
c=Image.open('C:\\Users\ELCOT\Downloads\Flipkart.jpg')
c1=c.resize((190,140))
img1=ImageTk.PhotoImage(c1)
c=Image.open('C:\\Users\ELCOT\Downloads\R.jpg')
c2=c.resize((200,140))
img2=ImageTk.PhotoImage(c2)
#center screen
width_of_window=800
height_of_window=500
screen_width=a.winfo_screenwidth()
screen_height=a.winfo_screenheight()
x_coordinate=(screen_width/2)-(width_of_window/2)
y_coordinate=(screen_height/2)-(height_of_window/2)
a.geometry("%dx%d+%d+%d"%(width_of_window,height_of_window,x_coordinate,y_coordinate))
#label
a1=Label(a,text="COMPARE YOUR PRODUCT",fg='black',border=0,width=20,bg='#00acc1',font=('times',20,'bold'))
a1.pack(fill=X)
a2=Label(a,text="Product Name:",fg="black",width=20,bg='#00acc1',font=('times',15,'bold'))
a2.place(x=170,y=100)
e1=Entry(a,font=('times',15),bg='white')
e1.place(x=420,y=100)

b=Button(a,text='Search',bg='#2e7d32',fg='white',font=('times',10,'bold'),width=25,command=model)
b.place(x=170,y=300)
b1=Button(a,text='Close',bg='#bf360c',fg='white',font=('times',10,'bold'),width=25,command=a.destroy)
b1.place(x=450,y=300)


    

import tkinter as tk
from PIL import Image,ImageTk
from tkinter.filedialog import askopenfile
from timer import count
from okay import counter
import os
import cv2
class create:
    def __init__(self,f,c):
        root1=tk.Tk()
        root1.iconbitmap("./icons/pngegg.ico")
        root1.title("Timer Setter")
        canvas=tk.Canvas(root1,width=1000,height=500)
        canvas.grid(columnspan=5,rowspan=3)
        for i in range(0,4):

            #sample images
            logo1=Image.open(f[i])
            logo1=logo1.resize((150, 150), Image.ANTIALIAS)
            logo1=ImageTk.PhotoImage(logo1)
            logo_label1=tk.Label(image=logo1)
            logo_label1.image=logo1
            logo_label1.grid(column=0,row=i)

            #vehicle detected images
            logo=Image.open("./temp/"+str(i)+".jpg")
            logo=logo.resize((150, 150), Image.ANTIALIAS)
            logo=ImageTk.PhotoImage(logo)
            logo_label=tk.Label(image=logo)
            logo_label.image=logo
            logo_label.grid(column=2,row=i)

            #red light displayer
            logo2=Image.open("./pics/red.png")
            logo2=logo2.resize((150, 150), Image.ANTIALIAS)
            logo2=ImageTk.PhotoImage(logo2)
            logo_label2=tk.Label(image=logo2)
            logo_label2.image=logo2
            logo_label2.grid(column=4,row=i)
        tim=[]
        for i in range(0,4):
            if((c[i]*2)<30):
                tim.append(c[i]*2)
            else:
                tim.append(30)
        for i in range(0,4):
            #green light
            logo2=Image.open("./pics/green.png")
            logo2=logo2.resize((150, 150), Image.ANTIALIAS)
            logo2=ImageTk.PhotoImage(logo2)
            logo_label2=tk.Label(image=logo2)
            logo_label2.image=logo2
            logo_label2.grid(column=4,row=i)
            
            #timer based on vehicle
            l=tk.Label(root1,text='',width=10,font='Arial 15 bold',fg='green')
            l.grid(column=1,row=i)
            count.countdown(l,root1,tim[i])

            #red light
            logo2=Image.open("./pics/red.png")
            logo2=logo2.resize((150, 150), Image.ANTIALIAS)
            logo2=ImageTk.PhotoImage(logo2)
            logo_label2=tk.Label(image=logo2)
            logo_label2.image=logo2
            logo_label2.grid(column=4,row=i)
            os.remove("./temp/"+str(i)+".jpg")
            
        root1.mainloop()
            

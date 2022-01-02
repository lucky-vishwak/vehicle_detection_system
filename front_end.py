import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfile
from PIL import Image,ImageTk
from okay import counter
import cv2
import os
from displayimages import create
root=tk.Tk()
c=[]
f=[]
#logo and name
root.iconbitmap("./icons/pngegg.ico")
root.title("Timer Setter")

#canvas
canvas=tk.Canvas(root,width=1000,height=500)
canvas.grid(columnspan=3,rowspan=3)


#background img
im=PhotoImage(file="./icons/timer.png")
back=Label(root,image=im)
back.place(x=0,y=0,relwidth=1,relheight=1)

#label
inst1=tk.Label(root,text="Traffic light Timer",font=("Apple SD Gothic Neo",50))
inst1.grid(columnspan=3,column=0,row=0)

#Label
inst=tk.Label(root,text="Upload PIC",font=("Arial",25))
inst.grid(columnspan=3,column=0,row=1)


#function(open_file)
def open_file():
    images=[]
    i=0
    j=0
    for i in range(0,4):
        file=askopenfile(parent=root,mode='rb',title='choose a file',filetype=[("jpg file","*.jpg")])
        if file:
            print(file.name)
            f.append(file.name)
            print("success")
            load=counter()
            img,count=load.imag(file.name)
            c.append(count)
            cv2.imwrite("./temp/"+str(i)+".jpg",img)
            i=i+1
    #button2
    browse_text1=tk.StringVar()
    browse_btn1=tk.Button(root,textvariable=browse_text1,command=lambda:display(),font="Raleway",bg="#20bebe",fg="white",height=2,width=15)
    browse_text1.set("display")
    browse_btn1.grid(column=2,row=2,rowspan=3)
#function2    
def display():
    root.destroy()
    r=create(f,c)
    
    
#button1
browse_text=tk.StringVar()
browse_btn=tk.Button(root,textvariable=browse_text,command=lambda:open_file(),font="Raleway",bg="#20bebe",fg="white",height=2,width=15)
browse_text.set("Browse")
browse_btn.grid(rowspan=3,column=0,row=2)



root.mainloop()

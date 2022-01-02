from tkinter import *
import time
from PIL import Image,ImageTk
class count:
    def countdown(l,root,t):
        root.update()
        mi=0
        while(mi==0 and t>=0):
            if(t==0):
                l.configure(text="%d:%d%d"%(mi,t,t))
            s=str(t)
            if(len(s)==1):
                l.configure(text="%d:%d%d"%(mi,0,t))
            else:
                l.configure(text="%d:%d"%(mi,t))
            root.update()
            if(mi!=0 and t==0):
                t=60
                mi=mi-1
            t=t-1
            time.sleep(1)
        l.configure(text="STOP",fg='red')
#root=Tk()
#root.title("okay")
#root.geometry("230x100")
#l=Label(root,text='',width=10,font='Arial 15 bold',fg='blue')
#l.grid(column=1)
#count.countdown(l)
#root.mainloop()

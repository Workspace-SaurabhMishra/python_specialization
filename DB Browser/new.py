from tkinter import *
from sqlite3 import *
from datetime import date
import time
class New:
    def __init__(self):
        self.root=Tk()
        self.root.title("PopUp")
        self.root.geometry("200x50")
        self.root.minsize(200,80)
        self.root.maxsize(200,80)
        self.x=0
        self.var=0
        
    def button(self):
        self.l1=Label(self.root,text="Enter Database Name")
        self.l1.pack()
        self.e1=Entry(self.root,textvariable=StringVar)
        self.e1.pack()
        self.b1=Button(self.root,text="Submit",command=self.return_val)
        self.b1.pack()
        self.root.mainloop()
        self.var=self.x
        return self.var

    def return_val(self):
        self.x=self.e1.get()+"["+str(date.today())+"]["+str(int(time.time()))+"]"+".sqlite"
        conn=connect(self.x)
        self.root.destroy()
        self.mssg()
        return self.x
    
    def mssg(self):
        self.root=Tk()
        self.root.title("PopUp")
        self.root.geometry("250x100")
        self.root.minsize(250,100)
        self.root.maxsize(250,100)
        self.l2=Label(self.root,text="Database Created \n Press OK \n Press Open and Navigate DataBase")
        self.l2.pack()
        self.b2=Button(self.root,text="OK",command=self.root.destroy)
        self.b2.pack()
      
        

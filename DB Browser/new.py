from tkinter import *
from sqlite3 import *
class New:
    def __init__(self):
        self.root=Tk()
        self.root.title("PopUp")
        self.root.geometry("400x300")
        self.l1=Label(self.root,text="Enter Database Name")
        self.l1.pack()
        self.e1=Entry(self.root,textvariable=StringVar)
        self.e1.pack()
        self.b1=Button(self.root,text="Submit",command=self.forward)
        self.b1.pack()
        self.root.mainloop()

    def forward(self):
        self.x=self.e1.get()+".sqlite"
        print(self.x)
        conn=connect(self.x)
        return self.x
    
        
        
    
        

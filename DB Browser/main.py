from tkinter import *
from new import *
root=Tk()
root.title("DB Browser")
root.geometry("800x600")
root.minsize(800,600)
root.maxsize(800,600)

def _1():######function will be called by button b1######
    l6.destroy()
    New()
    
    

    
######ALL TEXTS###########
l1=Label(text="   ")
l1.grid(row="4",column="4")
l2=Label(text="   ")
l2.grid(row="5",column="4")
l3=Label(text="   ")
l3.grid(row="6",column="5")
l4=Label(text="   ")
l4.grid(row="7",column="5")
l5=Label(text="   ")
l5.grid(row="8",column="5")
l6=Label(text="Open Source Project For DataBase Browsing"+"\n"+"By SAURABH MISHRA")
l6.grid(row="9",column="4")


#######ALL BUTTONS########
b1=Button(text="New",command=_1)
b1.grid(row="0",column="0",sticky="W")
b2=Button(text="Open")
b2.grid(row="0",column="1",sticky="W")
b3=Button(text="Save")
b3.grid(row="0",column="2",sticky="W")
b4=Button(text="Advance Settings",command=b2.destroy)
b4.grid(row="0",column="3",sticky="W")


mainloop()

from tkinter import *
from tkinter import filedialog
from new import *
root=Tk()
root.title("DB Browser")
root.minsize(380,300)
root.maxsize(380,300)
def new_button():######function will be called by button b1######
    x=New()
    x.button()
    
def open_button_func():
    root.file = filedialog.askopenfile(mode ='r', filetypes =[('Select sqlite file','*.sqlite')])
    print(root.file)
    
######ALL TEXTS###########
l1=Label(root,text="\n\n\n\n\n  Open Source Project For DataBase Browsing"+"\n"+"By SAURABH MISHRA")
l1.grid(row="5",column="1")
#######ALL BUTTONS########
b1=Button(root,text="New",command=new_button)
b1.grid(row="0",column="0",sticky="W")
b2=Button(root,text="Open",command=open_button_func)
b2.grid(row="0",column="1",sticky="W")
b3=Button(root,text="Save")
b3.grid(row="0",column="1",sticky="E")
b4=Button(root,text="Exit",command=root.destroy)
b4.grid(row="0",column="2",sticky="W")
mainloop()

from tkinter import *
from tkinter import ttk
from edit import *
from tkinter import messagebox

import os
t = Tk()
t.geometry("1250x600")

la = Label(text='file path').place(x=20,y=20)
la2 = Label(text="file name").place(x=390,y=20)
path = Entry(t,width=50)
path.place(x=20,y=40)

name = Entry(t,width=50)
name.place(x=390,y=40)

sc = Scrollbar(t)
sc.pack(fill='y',side=RIGHT)

e = Text(t,width=150,height=30,yscrollcommand=sc.set)
e.place(x=20,y=75)

sc.config(command=e.yview)


ps = "s\s"
pss = ps[1]



def press():
    try:


        mget = e.get(1.0,1.1).lower()

        if mget in ['c','clear']:
            print(mget)
            fpath = path.get()
            fname = name.get()

            o = open(f"{fpath+pss+fname}",'w')
            o.write('')
            messagebox.showinfo('cleared !!','the file is clear !!')
        else :
            fpath = path.get()
            fname = name.get()

            o = open(f"{fpath+pss+fname}",'a')
            get = str(e.get(1.0,END))
            lis = stol(get)
            lis.pop()
            st = ltos(lis)
            o.write(f"{st}\n")
    except:
        messagebox.showerror("error !!","this is not path !!")


def press2():
    try:

        fpath = path.get()
        fname = name.get()
        op = open(f"{fpath+pss+fname}",'r')
        e.insert(1.0,f"{op.read()}")
    except:
        messagebox.showerror('error !!',"this is not path !!")
def press3():
    try:
        if os.system(f"{fpath+pss+fname}") != 'The system cannot find the path specified.':
            fpath = path.get()
            fname = name.get()
            os.system(f"{fpath+pss+fname}")
        else:
            messagebox.showerror('error !!',"this is not path !!")   
    except:
        messagebox.showerror('error !!',"this is not path !!")


def press4():
    try:

        fpath = path.get()
        fname = name.get()
        os.unlink(f"{fpath+pss+fname}")
    except:
        messagebox.showerror('error !!',"this is not path !!")

b = Button(t,text="apply",command=press,width=10)
b.place(x=750,y=35)

b2 = Button(t,text="view",command=press2,width=10)
b2.place(x=870,y=35)

b3 = Button(t,text="open file",command=press3,width=10)
b3.place(x=990,y=35)

b4 = Button(t,text="delete file",command=press4,width=10)
b4.place(x=1110,y=35)

t.mainloop()
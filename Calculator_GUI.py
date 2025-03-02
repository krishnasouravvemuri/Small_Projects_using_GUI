from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Calculator")
root.geometry("300x150+600+200") 
root.resizable(1,1)

lb1 = Label(text = "A")
lb1.grid(row = 0 , column = 0 , sticky = W )
e1 = Entry()
e1.grid(row = 0 , column = 1)

lb2= Label(text = "B")
lb2.grid(row = 1 , column = 0 , sticky = W )
e2 = Entry()
e2.grid(row = 1 , column = 1)

lb3 = Label(text = "C")
lb3.grid(row = 2 , column = 0 , sticky = W )
e3 = Entry()
e3.grid(row = 2 , column = 1)

def sum():
    e3.delete(0,'end')
    a = int(e1.get())
    b = int(e2.get())
    c = a + b
    e3.insert(0,c)

def diff():
    e3.delete(0,'end')
    a = int(e1.get())
    b = int(e2.get())
    c = a - b
    e3.insert(0,c)

def mul():
    e3.delete(0,'end')
    a = int(e1.get())
    b = int(e2.get())
    c = a * b
    e3.insert(0,c)

def div():
    try : 
        e3.delete(0,'end')
        a = int(e1.get())
        b = int(e2.get())
        c = a / b
        e3.insert(0,c)
    except :
        messagebox.showinfo("cant divide with 0")
        e2.delete(0,'end')
        e2.focus()

def fdiv():
    try : 
        e3.delete(0,'end')
        a = int(e1.get())
        b = int(e2.get())
        c = a // b
        e3.insert(0,c)
    except :
        messagebox.showinfo("cant divide with 0")
        e2.delete(0,'end')
        e2.focus()

def mod():
    e3.delete(0,'end')
    a = int(e1.get())
    b = int(e2.get())
    c = a % b
    e3.insert(0,c)

def exp():
    e3.delete(0,'end')
    a = int(e1.get())
    b = int(e2.get())
    c = a ** b
    e3.insert(0,c)

def clear():
    e1.delete(0,'end')
    e2.delete(0,'end')
    e3.delete(0,'end')
    

def quit():
    root.quit()

bt1 = Button(text = "+" , width = 10 , command = sum)
bt1.grid(row = 3 , column = 0 )

bt2 = Button(text = "-" , width = 10 , command = diff)
bt2.grid(row = 3 , column = 1 )

bt3 = Button(text = "/" , width = 10 , command = div)
bt3.grid(row = 3 , column = 2 )

bt4 = Button(text = "//" , width = 10 , command = fdiv)
bt4.grid(row = 4 , column = 0 )

bt5 = Button(text = "**" , width = 10 , command = exp)
bt5.grid(row = 4 , column = 1 )

bt6 = Button(text = "*" , width = 10 , command = mul)
bt6.grid(row = 4 , column = 2 )

bt7 = Button(text = "%" , width = 10 , command = mod)
bt7.grid(row = 5 , column = 0 )

bt8 = Button(text = "<--" , width = 10 , command = clear)
bt8.grid(row = 5 , column = 1 )

bt9 = Button(text = "X" , width = 10 , command = quit)
bt9.grid(row = 5 , column = 2 )


mainloop()                                 
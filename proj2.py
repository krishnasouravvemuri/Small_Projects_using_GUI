from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

root = Tk()
root.title("Text Editor")
root.geometry("700x400")

cont = Frame(root)
cont.pack(fill="both", expand=True)

text_area = None

def next_page(page):
    page.tkraise()

def opening_file():
    global text_area

    file_path = filedialog.askopenfilename(title="Select a File", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        try:
            with open(file_path, 'r') as file:
                content = file.read()
                if text_area is None:
                    text_area = Text(open_page, wrap=WORD, height=15)
                    text_area.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
                text_area.delete(1.0, END)
                text_area.insert(INSERT, content)
        except Exception as e:
            if text_area is not None:
                text_area.delete(1.0, END)
                text_area.insert(INSERT, f"An error occurred: {e}")

def create_file():
    file_name = filedialog.asksaveasfilename(title="Save File", defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_name:
        try:
            with open(file_name, 'w') as file:
                file.write("")
                messagebox.showinfo("Information" , "File Created !")            
        except Exception as e:
            pass

welcome = Frame(cont)
welcome.grid(row=0, column=0, sticky="news")

open_page = Frame(cont)
open_page.grid(row=0, column=0, sticky="news")

create_page = Frame(cont)
create_page.grid(row=0, column=0, sticky="news")

lb1 = Label(welcome, text="Welcome! What do you want to do today?")
lb1.grid(row=1, column=0, columnspan=2, pady=20)

bt1 = Button(welcome, text="Open a file", command=lambda: next_page(open_page))
bt1.grid(row=2, column=0, padx=20, pady=10)

bt2 = Button(welcome, text="Create a new file", command=lambda: next_page(create_page))
bt2.grid(row=2, column=1, padx=20, pady=10)

lb2 = Label(open_page, text="Open a File")
lb2.grid(row=0, column=0, columnspan=2, pady=10)

bt3 = Button(open_page, text="Open File", command=opening_file)
bt3.grid(row=1, column=0, padx=20, pady=10)

bt4 = Button(open_page, text="Back to Welcome Page", command=lambda: next_page(welcome))
bt4.grid(row=1, column=1, padx=20, pady=10)

lb3 = Label(create_page, text="Create a New File")
lb3.grid(row=0, column=0, columnspan=2, pady=20)

bt5 = Button(create_page, text="Create File", command=create_file)
bt5.grid(row=1, column=0, padx=20, pady=10)

bt6 = Button(create_page, text="Back to Welcome Page", command=lambda: next_page(welcome))
bt6.grid(row=1, column=1, padx=20, pady=10)

next_page(welcome)

root.mainloop()

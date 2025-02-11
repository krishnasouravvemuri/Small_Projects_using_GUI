from tkinter import *
from tkinter import messagebox
import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", password="Sourav@2005", database="proj1")
cur = conn.cursor(buffered = True)

def show_page(page, title):
    page.tkraise()

root = Tk()
root.geometry('500x450')
root.title("My First Project")

cont = Frame(root)
cont.pack(fill="both", expand=True)

# Welcome Page (No changes needed)
Welcome = Frame(cont)
Welcome.grid(row=0, column=0, sticky="nsew")
Label(Welcome, text="WELCOME !!").grid(row=0, column=1, sticky=W, padx=215)
Button(Welcome, text="Login", command=lambda: show_page(login, "Login Page")).grid(row=1, column=1, sticky=W, padx=220, pady=80)
Button(Welcome, text="Sign Up", command=lambda: show_page(SignUp, "SignUp Page")).grid(row=2, column=1, sticky=W, padx=215, pady=8)

# Login Page
login = Frame(cont)
login.grid(row=0, column=0, sticky="nsew")

Label(login, text="User Id ").grid(row=0, column=0)
e1 = Entry(login, width=20)
e1.grid(row=0, column=1, pady=20)

Label(login, text="Password ").grid(row=1, column=0, pady=20)
e2 = Entry(login, width=20 , show="*")
e2.grid(row=1, column=1, pady=20)

def verify_user():
    user_id = e1.get()
    password = e2.get()

    try:
        cur.execute("SELECT * FROM ids WHERE user_id = %s AND password = %s", (user_id, password))
        result = cur.fetchone() # Fetch the result!

        if result:
            messagebox.showinfo("Success", "Login Successful!")
        else:
            messagebox.showerror("Error", "User ID or Password is incorrect!")

    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")
        conn.rollback()  # Rollback on error

Button(login, text="Login", command=verify_user).grid(pady=20, row=2, column=0)
Button(login, text="New User ? Signup here", command=lambda: show_page(SignUp, "Login Page")).grid(row=2, column=3)
Button(login, text="Home", command=lambda: show_page(Welcome, "Login Page")).grid(row=3, column=1)

# SignUp Page
SignUp = Frame(cont)
SignUp.grid(row=0, column=0, sticky="nsew")

def Signup():
    insert = "INSERT INTO ids (user_id, password) VALUES (%s, %s)"
    user_id = str(e1.get())
    password = str(e2.get())
    e1.delete(0, 'end')
    e2.delete(0, 'end')

    if user_id and password:
        try:
            cur.execute(insert, (user_id, password))
            conn.commit()
            messagebox.showinfo("Information", "Successful signup. Proceed to Login")
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Signup Error: {err}")
            conn.rollback() # Important to rollback on error
    else:
        messagebox.showinfo("Information", "Credentials not proper")

Label(SignUp, text="User Id ").grid(row=0, column=0)
e1 = Entry(SignUp, width=20)
e1.grid(row=0, column=1, pady=20)

Label(SignUp, text="Password ").grid(row=1, column=0, pady=20)
e2 = Entry(SignUp, width=20 , show="*")
e2.grid(row=1, column=1, pady=20)

Button(SignUp, text="SignUp", command=Signup).grid(pady=20, row=2, column=0)
Button(SignUp, text="Existing User ? Login here", command=lambda: show_page(login, "Login Page")).grid(row=2, column=3)
Button(SignUp, text="Home", command=lambda: show_page(Welcome, "Home")).grid(row=3, column=1)

show_page(Welcome, "Welcome")
mainloop()
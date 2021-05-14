import sqlite3
from tkinter import *
from tkinter import messagebox as ms

with sqlite3.connect("login.db") as db:
    cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS user(username TEXT NOT NULL, password TEXT NOT NULL);")
cursor.execute("SELECT * FROM user")
db.commit()
db.close()

class main():
    def __init__(self, master):
        self.master = master
        self.username = StringVar()
        self.password = StringVar()
        self.n_username = StringVar()
        self.n_password = StringVar()
        self.gui()

    def login(self):
        with sqlite3.connect("login.db") as db:
            cursor = db.cursor()
        find_user = ("SELECT * FROM user WHERE username = ? AND password = ?")
        cursor.execute(find_user,[(self.username.get()),(self.password.get())])
        results = cursor.fetchall()
        if results:
            self.logf.pack_forget()
            ms.showinfo('Initiate Success', "You have successfully logged in.")
            root.destroy()
        else:
            ms.showerror("Error Occured", "Username or Password is incorrect!")

    def new_user(self):
        with sqlite3.connect("login.db") as db:
            cursor = db.cursor()
            ms.showinfo('Initiate Success', "Your account have successfully created.")
            self.log()
        insert = 'INSERT INTO user(username,password) VALUES(?,?)'
        cursor.execute(insert,[(self.n_username.get()),(self.n_password.get())])
        db.commit()

    def log(self):
        self.username.set("")
        self.password.set("")
        self.crf.pack_forget()
        self.head['text']="LOGIN"
        self.logf.pack()

    def cr(self):
        self.n_username.set("")
        self.n_password.set("")
        self.head['text']="Create Account"
        self.logf.pack_forget()
        self.crf.pack()

    def gui(self):
        self.head=Label(self.master,text=" Login Page ",font =('Segoe UI',30,'bold'),fg="#000000",pady=40)
        self.head.pack()

        self.logf=Frame(self.master,padx=10,pady=10)
        Label(self.logf,text="Username: ",font=('Segoe UI',15,'bold'),padx=5,pady=5,fg="#2B8534").grid(sticky=W)
        Entry(self.logf,textvariable=self.username,bd=8,font=('Adobe Gothic Std B',11,'bold')).grid(row=0,column=1,sticky=E)
        Label(self.logf,text="Password: ",font=('Segoe UI',15,'bold'),padx=5,pady=5,fg="#2B8534").grid(row=1,column=0,sticky=W)
        Entry(self.logf,textvariable=self.password, bd=8,font=('Adobe Gothic Std B',11,'bold'),show="*").grid(row=1,column=1,sticky=E)
        Button(self.logf, text="Login",font=("Segoe UI", 13, "bold"), padx=40,pady=3,fg="#FFFFFF",bg="green", command=self.login).grid(row=2,column=2)
        Button(self.logf, text="New Account", font=("Segoe UI", 13, "bold"),padx=20,pady=3,fg="#FFFFFF",bg="green",command=self.cr).grid(row=2, column=1)
        self.logf.pack()

        self.crf = Frame(self.master, padx=10, pady=10)
        Label(self.crf, text="Username: ", font=('Segoe UI', 15, 'bold'), padx=5, pady=5, fg="#C00000").grid(sticky=W)
        Entry(self.crf, textvariable=self.n_username, bd=8, font=('Adobe Gothic Std B', 11, 'bold')).grid(row=0, column=1,sticky=E)
        Label(self.crf, text="Password: ", font=('Segoe UI', 15, 'bold'), padx=5, pady=5, fg="#C00000").grid(row=1, column=0,sticky=W)
        Entry(self.crf, textvariable=self.n_password, bd=8, font=('Adobe Gothic Std B', 11, 'bold'),show="*").grid(row=1, column=1,sticky=E)
        Button(self.crf, text="Login", font=("Segoe UI", 13, "bold"), padx=40, pady=3, fg="#FFFFFF",bg="red", command=self.log).grid(row=2, column=2)
        Button(self.crf, text="New Account", font=("Segoe UI", 13, "bold"), padx=20, pady=3, fg="#FFFFFF", bg="red",command=self.new_user).grid(row=2, column=1)
        self.logf.pack()

root = Tk()
main(root)
root.title("Login System")
root.geometry("600x400+350+120")
root.resizable(False, False)
root.mainloop()
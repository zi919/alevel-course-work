# =========================================================
#
# this module control the login of user and adminstrator
# written by zi chen                          11/05/2022

#
# =========================================================

from tkinter import *
from tkinter import messagebox
from checkers import *
# create a login and sign_up menu for user
def create_menu():
    root = Tk()
    root.title("main menu  ")
    root.geometry("700x500+400+150")
    label0 = Label(root, text="                                         ")
    label1 = Label(root, text="welcome to main menu ", font=("a,", 15))
    button1 = Button(text="Exit", command=quit, bg="orange", font=("a,", 10), width=7)
    button2 = Button(text="log in ", command=lambda: Login(root), bg="orange", font=("a,", 10), width=7)
    button3 = Button(text="sign up", command=lambda: signup(root), bg="orange", font=("a,", 10), width=7)
    label0.grid(row=0, column=0)
    label1.grid(row=0, column=1, columnspan=2)
    button1.grid(row=2, column=1, pady=10, sticky="w")
    button2.grid(row=2, column=2, sticky="w")
    button3.grid(row=2, column=3, )
    root.mainloop()

# subprogram for main login system
def Login(root):
    def display_login_result(username, password):
        result = log_in(username, password)
        if result == True:
            messagebox.showinfo( "title","you have logged in ")
        elif result==",password is not coorect":
            messagebox.showinfo("title","password is not coorect ")
        elif result=="No such username":
            messagebox.showinfo("title","No such username")
        else:
            pass


    root.destroy()
    root = Tk()
    root.title("login main menu ")
    root.geometry("700x500")
    label0 = Label(root, text="login system")
    label0.grid(row=0, column=1, pady=5,stick="s")
    label = Label(root, text="username")
    label2 = Label(root, text="password")
    entry = Entry(root)
    entry2 = Entry(root)
    label.grid(row=1, column=0, padx=10)
    entry.grid(row=1, column=1)
    label2.grid(row=2, column=0)
    entry2.grid(row=2, column=1)
    button = Button(root, width=8, height=1, text="Back", command=lambda: fun_Back(root))
    button2 = Button(root, width=8, text="log in ", command=lambda : display_login_result(entry,entry2) )# function to check data in username and password file
    button.grid(row=3, column=0, pady=50)
    button2.grid(row=3, column=1)
    root.mainloop()


def signup(root):
    root.destroy()
    root = Tk()
    root.title("sign up  main menu ")
    root.geometry("700x500")

    label0 = Label(root, text="sign up ")
    label0.grid(row=0, column=1, pady=5)
    label = Label(root, text="username")
    label2 = Label(root, text="password")
    entry = Entry(root)
    entry2 = Entry(root,show="**")
    entry3 = Entry(root,show="**")
    label3 = Label(root, text="repasswood")
    label.grid(row=1, column=0, padx=10)
    entry.grid(row=1, column=1)
    label2.grid(row=2, column=0)
    label3.grid(row=3, column=0)
    entry2.grid(row=2, column=1)
    entry3.grid(row=3, column=1)
    button = Button(root, width=8, height=1, text="Back", padx=10, pady=10, command=lambda: fun_Back(root))# button for going back
    button2 = Button(root, width=8, text="ok", padx=10, pady=10, command=lambda: fun_Ok(entry,entry2,entry3))#button for update data
    button.grid(row=4, column=0, pady=50)
    button2.grid(row=4, column=1)
    root.mainloop()


def fun_Back(root):
    root.destroy()
    create_menu()


def fun_Ok(username, password, repassword):
    username=username.get()
    password=password.get()
    repassword=repassword.get()
    if password==repassword:
        if check_length(username,5,2) and check_length(password,5,2):
            with open("username.txt", "a") as file:
                file.write(f"\n{username}")
            with open("password.txt", "a") as file2:
                file2.writelines(f"\n{password}")
        else:
             messagebox.showinfo( "title","you need to enter given length in ")

def log_in(username,password):
    username=username.get()
    password=password.get()
    with open("username.txt") as f : #open a text file that store the user who has registered
        for i in f.readline():
            if username==i:
                with open("password.txt") as password_file:
                    for j in password_file:
                        if password==j:
                            return True
                    else:
                        return "password is not coorect "
        else:
            return "No such username "


if __name__=="__main__":
    create_menu()

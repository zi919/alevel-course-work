# =========================================================
#
# this module control the login of user and adminstrator
# written by zi chen                          7/06/2022

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
    root.iconphoto(False, PhotoImage(file='car,icon.png'))
    frame_0=Frame(root)
    label1 = Label(frame_0, text="welcome to main menu ", font=("a,", 15))
    button1 = Button(frame_0,text="Exit", command=quit, bg="orange", font=("a,", 10), width=7)
    button2 = Button(frame_0,text="log in ", command=lambda: Login(root), bg="orange", font=("a,", 10), width=7)
    button3 = Button(frame_0,text="sign up", command=lambda: signup(root), bg="orange", font=("a,", 10), width=7)
    label1.grid(row=0, column=1, columnspan=2)
    button1.grid(row=2, column=1, pady=10, sticky="w")
    button2.grid(row=2, column=2, sticky="w")
    button3.grid(row=2, column=3, )
    frame_0.pack()
    root.mainloop()

# subprogram for main login system
def Login(root):
    def display_login_result(username, password):

        result = log_in(username, password)
        print(result)
        if result == True:
            messagebox.showinfo( "title","you have logged in ")
        elif result==",password is not coorect":
            messagebox.showinfo("title","password is not correct ")
        elif result=="No such username ":
            messagebox.showinfo("title","No such username")
        else:
            pass


    root.destroy()
    root = Tk()
    root.iconphoto(False, PhotoImage(file='car,icon.png'))
    root.title("login main menu ")
    root.geometry("700x500")
    frame_0=Frame(root,bd=10,relief="groove")
    label0 = Label(frame_0, text="login system",font=("Arial",15) )
    label0.grid(row=0, column=1, pady=5,stick="s")
    label = Label(frame_0, text="username",font=("Arial",15) )
    label2 = Label(frame_0, text="password",font=("Arial",15) )
    entry = Entry(frame_0,font=("Arial",15) )#username
    entry2 = Entry(frame_0,show="*",font=("Arial",15) )
    label.grid(row=1, column=0, padx=10)
    entry.grid(row=1, column=1,ipady=15,ipadx=100)
    label2.grid(row=2, column=0)
    entry2.grid(row=2, column=1,ipady=15,ipadx=100)
    button = Button(frame_0, width=8, height=1, text="Back", command=lambda: fun_Back(root),font=("Arial",15) )
    button2 = Button(frame_0, width=8, text="log in ", command=lambda : display_login_result(entry,entry2),font=("Arial",15) )# function to check data in username and password file
    button.grid(row=3, column=0, pady=50)
    button2.grid(row=3, column=1)
    frame_0.pack(ipady=20,ipadx=50,anchor=CENTER,pady=100)
    root.mainloop()


def signup(root):
    root.destroy()
    root = Tk()
    root.title("sign up  main menu ")
    root.geometry("700x600")
    root.iconphoto(False, PhotoImage(file='car,icon.png'))
    frame_0=Frame(root,bd=10,relief="groove")
    label0 = Label(frame_0, text="sign up ",font=("Arial",15))
    label0.grid(row=0, column=1, pady=5)
    label = Label(frame_0, text="username",font=("Arial",15))
    label2 = Label(frame_0, text="password",font=("Arial",15))
    entry = Entry(frame_0,font=("Arial",15))
    entry2 = Entry(frame_0,font=("Arial",15))
    entry3 = Entry(frame_0,show="*",font=("Arial",15))
    label3 = Label(frame_0, text="repasswood",font=("Arial",15))
    label.grid(row=1, column=0, padx=10)
    entry.grid(row=1, column=1,ipady=15,ipadx=100)
    label2.grid(row=2, column=0)
    label3.grid(row=3, column=0)
    entry2.grid(row=2, column=1,ipady=15,ipadx=100)
    entry3.grid(row=3, column=1,ipady=15,ipadx=100)
    button = Button(frame_0, width=8, height=1, text="Back", padx=10, pady=10, command=lambda: fun_Back(root))# button for going back
    button2 = Button(frame_0, width=8, text="ok", padx=10, pady=10, command=lambda: fun_Ok(entry,entry2,entry3))#button for update data
    button.grid(row=4, column=0, pady=50)
    button2.grid(row=4, column=1)
    frame_0.pack(ipady=20,ipadx=50,anchor=CENTER,pady=100)
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
                        return "password is not correct "
        else:
            return "No such username "


if __name__=="__main__":
    create_menu()

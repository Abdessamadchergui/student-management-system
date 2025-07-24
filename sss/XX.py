from tkinter import *
import tkinter.messagebox
import tkinter as tk
from PIL import ImageTk, Image
from conn_myql import conn

cursor = conn.cursor()

class Main:

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Student Management System login page")
        self.window.geometry('649x432')
        self.window.resizable(False, False)
        self.canvas = Canvas(self.window, height=432, width=649)
        self.bg_image = PhotoImage(file="image/20204.png")
        self.canvas.pack(side='top')
        self.image = self.canvas.create_image(0, 0, anchor='nw', image=self.bg_image)
        self.lb1 = Label(self.window, text='username: ', width=10, height=2).place(x=250, y=150)
        self.lb2 = Label(self.window, text='password: ', width=10, height=2).place(x=250, y=200)
        self.get_user_name = StringVar()
        self.en_user_name = Entry(self.window, textvariable=self.get_user_name)
        self.en_user_name.place(x=330, y=150, height=40)
        self.get_user_name = StringVar()
        self.en_user_name = Entry(self.window, textvariable=self.get_user_name)
        self.en_user_name.place(x=330, y=150, height=40)
        self.get_user_pwd = StringVar()
        self.en_user_pwd = Entry(self.window, textvariable=self.get_user_pwd, show='*')
        self.en_user_pwd.place(x=330, y=200, height=40)
        self.bt_login = Button(self.window, text='Login', command=self.user_login, width=10, height=2)
        self.bt_login.place(x=150, y=300)
        self.bt_logup = Button(self.window, text='Register', command=self.user_register, width=10, height=2)
        self.bt_logup.place(x=250, y=300)
        self.bt_quit = Button(self.window, text='Exit', command=self.window.quit, width=10, height=2)
        self.bt_quit.place(x=350, y=300)
        self.window.mainloop()

    # User login function
    def user_login(self):
        user_name = self.get_user_name.get()
        user_pwd = self.get_user_pwd.get()
        try:
            sql = "SELECT * FROM user WHERE username = %s AND password = %s"
            cursor.execute(sql, (user_name, user_pwd))
            result = cursor.fetchone()
            if user_name == "" or user_pwd == "":
                tkinter.messagebox.showerror(title="Error", message="The username or password cannot be empty!")
            elif result is not None:
                tkinter.messagebox.showinfo(title="Welcome", message="Welcome, " + str(user_name))
                self.window.destroy()
            else:
                tkinter.messagebox.showerror(title="Error", message="Incorrect username or password!")
        except Exception:
            tkinter.messagebox.showerror("Login Exception")

    # User registration interface
    def user_register(self):
        window_sign_up = tkinter.Toplevel(self.window)
        window_sign_up.title("Student Information Management System - Register Page")
        window_sign_up.geometry('600x400')
        window_sign_up.resizable(False, False)
        canvas_sign = Canvas(window_sign_up, height=400, width=600)
        canvas_sign.pack(side='top')
        image_sign = canvas_sign.create_image(0, 0, anchor='nw', image=self.bg_image)
        lb3 = Label(window_sign_up, text="Username：", width=10, height=2).place(x=200, y=100)
        lb4 = Label(window_sign_up, text="Password：", width=10, height=2).place(x=200, y=150)
        lb5 = Label(window_sign_up, text="Sure:", width=7, height=2).place(x=200, y=200)
        self.new_user_name = tkinter.StringVar()
        en_new_name = Entry(window_sign_up, textvariable=self.new_user_name)
        en_new_name.place(x=260, y=100, height=40)
        self.new_user_pwd = tkinter.StringVar()
        en_use_pwd = Entry(window_sign_up, textvariable=self.new_user_pwd, show='*')
        en_use_pwd.place(x=260, y=150, height=40)
        self.new_pwd_again = tkinter.StringVar()
        en_pwd_again = Entry(window_sign_up, textvariable=self.new_pwd_again, show='*')
        en_pwd_again.place(x=260, y=200, height=40)
        bt1 = Button(window_sign_up, text="Register", command=self.sign_up, width=10, height=2)
        bt1.place(x=200, y=280)
        bt2 = Button(window_sign_up, text="Cancel", command=self.no_sig, width=10, height=2)
        bt2.place(x=300, y=280)

        # Realization of user registration function

    def sign_up(self):
        new_name = self.new_user_name.get()
        new_pwd = self.new_user_pwd.get()
        pwd_again = self.new_pwd_again.get()
        try:
            sql = "select username from user where username='" + new_name + "'"
            cursor.execute(sql)
            result = cursor.fetchone()
            if new_pwd == "" or pwd_again == "" or new_name == "":
                tkinter.messagebox.showerror(title="Error", message="The user name or password cannot be empty")
            elif result != None:
                tkinter.messagebox.showerror(title="Error", message="The user name has been registered")
            elif new_pwd == pwd_again:
                try:
                    sql2 = 'insert into user(username, password) values ("'"%s"'", "'"%s"'")' % (new_name, new_pwd)
                    cursor.execute(sql2)
                    conn.commit()
                    tkinter.messagebox.showinfo(title="Successful registration", message=
                    "Congratulations on your successful registration, please go to login")
                except Exception as e:
                    tkinter.messagebox.showerror(e)
            else:
                tkinter.messagebox.showerror(title="Error", message="Two passwords do not match")
        except Exception as e:
            tkinter.messagebox.showerror(e)

        # deregistration

    def no_sig(self):
        conn.close()
        self.window.destroy()

    # Execute the program and create the window

Main()


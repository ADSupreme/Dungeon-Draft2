from tabnanny import check
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import sqlite3 as sql
import tkinter as tk
from tkinter import ttk

list1 = []
f1 = []
conn = sql.connect('signup.db')
cursor = conn.cursor()
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS Signups (Full Name TEXT NOT NULL, Age INT NOT NULL, Address TEXT NOT NULL, Phone_Number INT NOT NULL, Username TEXT NOT NULL, Password TEXT NOT NULL); ''')
conn.commit()

#fileObj = open('List.txt', 'r')
#list1 = fileObj.read().splitlines()  # puts the file into an array

#f = open('milk_brand.txt', "r")
#f1 = f.read().splitlines()


# polymporpjism -- when printing out calculating
class Display(Tk):  # using inheritance to inherit all the properties from tkinter

    def __init__(self):

        self.root = Tk()
        self.root.title("Welcome")
        self.root.geometry("1920x1080")
        button1 = Button(self.root, text="Sign up", width=13, height=5, command=self.signup, font=('verdana', 20, 'bold')).place(x=700, y=402)
        button2 = Button(self.root, text="Log in ", width=13, height=5, command=lambda: lg.signup(self), font=('verdana', 20, 'bold')).place(x=1000, y=402)
        label1 = Label(self.root, text="Welcome to Seniors App", fg='white', width=20, height=2, font=('verdana', 25, "bold")).place(x=750, y=150)
        label2 = Label(self.root, text=' Choose one option', fg='white', width=15, height=2, font=('verdana', 25, 'bold')).place(x=800, y=250)
        self.root.mainloop()

        your_image = ImageTk.PhotoImage(Image.open('seniorspic.png'))
        your_label = Label(parent=self.root, image=self.your_image)
        self.your_label.pack(side=LEFT)

    def signup(self):
        self.window = Tk()
        self.window.title("Welcome")
        self.window.geometry("1920x1080")
        self.window.config(bg="#F0F0F8")

        def remove():
            print("A")
            Nameinput.delete(0, END)
            ageinput.delete(0, END)
            addressinput.delete(0, END)
            PHinput.delete(0, END)
            Userinput.delete(0, END)
            Passwordinput.delete(0, END)

        def added():

            global nameget
            global ageget
            global addressget
            global Phoneget
            global usernameget
            global passwordget

            verify()
            nameget = Nameinput.get()
            ageget = ageinput.get()
            addressget = addressinput.get()
            Phoneget = PHinput.get()
            usernameget = Userinput.get()
            passwordget = Passwordinput.get()

        def verify():

            nameget = Nameinput.get()
            ageget = ageinput.get()
            addressget = addressinput.get()
            Phoneget = PHinput.get()
            usernameget = Userinput.get()
            passwordget = Passwordinput.get()

            if len(nameget) == 0:
                messagebox.showerror(
                    title="Alert", message="Please dont leave any fields empty")
            elif len(ageget) == 0:
                messagebox.showerror(
                    title="Alert", message="Please dont leave any fields empty")

            elif len(addressget) == 0:
                messagebox.showerror(
                    title="Alert", message="Please dont leave any fields empty")

            elif len(usernameget) == 0:
                messagebox.showerror(
                    title="Alert", message="Please dont leave any fields empty")

            elif len(passwordget) == 0:
                messagebox.showerror(
                    title="Alert", message="Please dont leave any fields empty")
            elif len(passwordget) == 0:
                messagebox.showerror(
                    title="Alert", message="Please dont leave any fields empty")
            else:

                if not any(ch.isupper() for ch in passwordget):
                    messagebox.showerror(
                        title="Alert", message="Atleast 1 uppercase character required!")

                elif not any(ch.islower() for ch in passwordget):
                    messagebox.showerror(
                        title="Alert", message='Atleast 1 lowercase character required!')
                elif not any(ch.isdigit() for ch in passwordget):
                    messagebox.showerror(
                        title="Alert", message='Atleast 1 number required!')
                elif len(passwordget) < 8:
                    messagebox.showerror(
                        title="Alert", message='Password must be minimum of 8 characters!')
                else:
                    messagebox.showinfo(title="Sucess", message="Sucess")

        def addition():

            script = '''INSERT INTO Signups (Full Name , Age, Address, Phone_Number, Username, Password) VALUES (?,?,?,?,?,?);'''
            cursor.execute(script, (nameget, ageget, addressget, Phoneget, usernameget, passwordget))
            conn.commit()

        Label1 = Label(self.window, text='Please fill in your details', width=50, height=2, font=('verdana', 25, "bold")).place(x=200, y=30)

        Label2 = Label(self.window, text='Full Name ', width=20, height=2, font=('verdana', 20, "bold")).place(x=200, y=200)
        Nameinput = Entry(self.window, font=15, width=30, )
        Nameinput.place(x=550, y=200)

        Label3 = Label(self.window, text='Age ', width=20, height=2, font=('verdana', 18, "bold")).place(x=200, y=280)
        ageinput = Entry(self.window, font=15, width=30, )
        ageinput.place(x=550, y=280)

        Label4 = Label(self.window, text='Address', width=10, height=2, font=('verdana', 18, "bold")).place(x=200, y=360)
        addressinput = Entry(self.window, font=15, width=30, )
        addressinput.place(x=550, y=360)

        Label5 = Label(self.window, text='Phone-Number', width=15, height=2, font=('verdana', 18, "bold")).place(x=200, y=440)
        PHinput = Entry(self.window, font=15, width=30, )
        PHinput.place(x=550, y=440)

        Label6 = Label(self.window, text='Username', width=20, height=2, font=('verdana', 18, "bold")).place(x=200, y=600)
        Userinput = Entry(self.window, font=15, width=30, )
        Userinput.place(x=550, y=600)

        Label7 = Label(self.window, text='Password', width=20, height=2, font=('verdana', 18, "bold")).place(x=200, y=680)
        Passwordinput = Entry(self.window, show="*", font=15, width=30, )
        Passwordinput.place(x=550, y=680)

        del_button = Button(self.window, text="Clear", width=23, height=5, command=remove, font=('verdana', 14, "bold"))
        del_button.place(x=950, y=400)

        save_button = Button(self.window, text="Save", width=23, height=5, command=addition,
                             font=('verdana', 14, "bold"))
        save_button.place(x=950, y=600)

        return_button = Button(self.window, text="Proceed to login", width=23, command=lambda: lg.signup(self), height=5, font=('verdana', 14, "bold"))
        return_button.place(x=950, y=200)


class lg(Tk):

    def __init__(self):

        pass

    def signup(self):

        self.window = Tk()
        self.window.title("Login")
        self.window.geometry("1920x1080")
        self.window.config(bg="#F0F0F8")

        self.username = Label(self.window, width=15, height=2, text='Username', font=('verdana', 20, "bold"))
        self.username.place(x=300, y=300)

        self.e_username = Entry(self.window, font=15, width=50, )
        self.e_username.place(x=550, y=300)

        self.password = Label(self.window, text="Password", width=15, height=2, font=('verdana', 20, "bold"))
        self.password.place(x=300, y=400)

        self.e_password = Entry(self.window, width=50, font=15, show="*")
        self.new_var = self.e_password.place(x=550, y=400)

        self.proceed = Button(self.window, text="Proceed", command=screen2, width=23, height=5, font=('verdana', 14, "bold"))
        self.proceed.place(x=950, y=500)

        self.back = Button(self.window, text="Back", command=lambda: Display.__init__(self), width=23, height=5, font=('verdana', 14, "bold"))
        self.back.place(x=200, y=500)

        self.save = Button(self.window, text="Save", command=check, width=23, height=5, font=('verdana', 14, "bold"))
        self.save.place(x=600, y=500)

    def check(self):

        if len(self.e_username) == 0:
            messagebox.showerror(title="Alert", message="Please dont leave any fields empty")

        if len(self.e_password) == 0:
            messagebox.showerror(title="Alert", message="Please dont leave any fields empty")

        self.window.mainloop()


def screen2():
    top = Toplevel()
    top.geometry("400x400")
    top.title("toplevel")
    top.config(bg="#F0F0F8")

    l2 = Label(top, text="Choose one option")
    l2.pack()

    menu = Menu()
    b1 = Button(top, text="Monthly groceries", command=lambda *args: menu.dropdown())
    b1.place(x=120, y=90)

    b1 = Button(top, text="Weekly groceries", command=lambda: menu.dropdown())
    b1.place(x=120, y=250)

    top.mainloop()


class Menu():

    def __init__(self):

        pass

    def dropdown(self):

        self.screen = Tk()
        self.screen.title("Grocery List")
        self.screen.geometry("1920x1080")
        self.screen.config(bg="#F0F0F8")

        my_notebook = ttk.Notebook(self.screen)
        my_notebook.pack(side=RIGHT, pady=30)

        my_frame1 = Frame(my_notebook, width=1920, height=1080, bg="blue")
        my_frame2 = Frame(my_notebook, width=1920, height=1080, bg="red")
        my_frame1.pack(side=RIGHT, expand=1)
        my_frame2.pack(side=RIGHT, expand=1)
        my_notebook.add(my_frame1, text="Monthly groceries")
        my_notebook.add(my_frame2, text="Map View")

        self.L1 = Label(self.screen, width=20, height=2, text='Grocery List Generator', font=('verdana', 20, "bold"))
        self.L1.place(x=600, y=50)

        self.B1 = Button(self.screen, width=20, height=2, text='Weekly Groceries', font=('verdana', 20, "bold"))
        self.B1.place(x=600, y=50)

        self.B2 = Button(self.screen, width=20, height=2, text='Monthly Groceries', font=('verdana', 20, "bold"))
        self.B2.place(x=250, y=50)

        def pick_color(e):
            if my_combo.get() == "Milk":
                color_combo.config(value=f1)
                color_combo.current(0)
            if my_combo.get() == "Medium":
                color_combo.config(value=medium_colors)
                color_combo.current(0)
            # if my_combo.get() == "Large":
            # color_combo.config(value=large_colors)
            # color_combo.current(0)

        # Create a drop box
        my_combo = ttk.Combobox(self.screen, value=list1)
        my_combo.pack(pady=90)
        my_combo.bind("<<ComboboxSelected>>", pick_color)

        # Color Combo box
        color_combo = ttk.Combobox(self.screen, value=[" "])
        color_combo.current(0)
        color_combo.pack(pady=50)

        self.screen.mainloop()


main = Display()
main.root()


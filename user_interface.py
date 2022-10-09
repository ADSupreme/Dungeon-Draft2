from tkinter import *
from tkinter import Tk, Canvas, Frame, BOTH
from PIL import ImageTk, Image
import sqlite3
import settings
from tkinter import ttk
from main import Game
import main
from settings import difficulty_rating as age
import pygame

login = Tk()
login.title('Dungeon')
login.geometry("1280x720")

# Create a database or connect to one
conn = sqlite3.connect('login.db')
# Create cursor
c = conn.cursor()
# Create table
c.execute("""CREATE TABLE IF NOT EXISTS login (
        email_id text, 
        first_name text,
        last_name text,
		username text,
		password text,
		user_level integer,
		level_access text
		)""")

global level_name

"""c.execute("INSERT INTO login VALUES (:email_id, :first_name, :last_name, :username, :password, :user_level, :level_access)",
          {
              'email_id': "Aayush",
              'first_name': "Aayush",
              'last_name': "Dongre",
              'username': "Aayush",
              'password': "Dongre",
              'user_level': 1,
              'level_access': "Admin",

          })"""


def register_page():
    global register_screen
    register_screen = Tk()
    register_screen.title('Update A Record')
    register_screen.geometry("1280x720")
    global email_id
    global first_name
    global last_name
    global username_val
    global password_val

    email_id_label = Label(register_screen, text="Email", font=("Courier", 20))
    email_id_label.place(x=280, y=64, width=100, height=60)
    email_id = Entry(register_screen, width=380, font=("Courier", 20), borderwidth=5)
    email_id.place(x=420, y=64, width=440, height=80)

    first_name_label = Label(register_screen, text="First Name", font=("Courier", 20))
    first_name_label.place(x=220, y=172, width=200, height=60)
    first_name = Entry(register_screen, width=380, font=("Courier", 20), borderwidth=5)
    first_name.place(x=420, y=172, width=440, height=80)

    last_name_label = Label(register_screen, text="Last Name", font=("Courier", 20))
    last_name_label.place(x=220, y=280, width=200, height=60)
    last_name = Entry(register_screen, width=380, font=("Courier", 20), borderwidth=5)
    last_name.place(x=420, y=280, width=440, height=80)

    username_val_label = Label(register_screen, text="user_name", font=("Courier", 20))
    username_val_label.place(x=220, y=390, width=200, height=60)
    username_val = Entry(register_screen, width=380, font=("Courier", 20), borderwidth=5)
    username_val.place(x=420, y=390, width=440, height=80)

    password_val_label = Label(register_screen, text="password", font=("Courier", 20))
    password_val_label.place(x=220, y=500, width=200, height=60)
    password_val = Entry(register_screen, width=380, font=("Courier", 20), borderwidth=5)
    password_val.place(x=420, y=500, width=440, height=80)

    register_page_btn = Button(register_screen, text="Register", command=register)
    register_page_btn.place(x=540, y=630, width=200, height=90)


def register():
    print("starting")
    conn = sqlite3.connect('login.db')
    c = conn.cursor()
    c.execute("SELECT *, oid FROM login")
    user_data = c.fetchall()
    check_name = username_val.get()
    # print(check_name)
    check_password = password_val.get()
    # print(check_password)
    add_record = False
    for record in user_data:
        if str(record[3]) != check_name and str(record[4]) != check_password:
            # print("not present")
            add_record = True
        else:
            # print("present")
            add_record = False
            break
    if add_record:
        c.execute("INSERT INTO login VALUES (:email_id, :first_name, :last_name, :username, :password, :user_level, :level_access)",
                  {
                      'email_id': email_id.get(),
                      'first_name': first_name.get(),
                      'last_name': last_name.get(),
                      'username': username_val.get(),
                      'password': password_val.get(),
                      'user_level': 1,
                      'level_access': "User",

                  })
        add_record = False
    print("done")

    # Commit Changes
    conn.commit()

    # Close Connection
    conn.close()

    # Clear The Text Boxes
    email_id.delete(0, END)
    first_name.delete(0, END)
    last_name.delete(0, END)
    username_val.delete(0, END)
    password_val.delete(0, END)

    register_screen.withdraw()


def login_function():
    # Create a database or connect to one
    conn = sqlite3.connect('login.db')

    # Create cursor
    c = conn.cursor()

    username_data = username.get()
    password_data = password.get()
    c.execute("SELECT *, oid FROM login")
    user_data = c.fetchall()

    for record in user_data:
        if str(record[3]) == username_data and str(record[4]) == password_data:
            if username_data == "Aayush" and password_data == "Dongre":
                admin_page()
                username.delete(0, END)
                password.delete(0, END)
            else:
                global login_name
                login_name = username_data
                global login_password
                login_password = password_data
                user_page(record[5], login_name, login_password, record[0])

    conn.commit()
    conn.close()


def user_page(level_permission, login_name, login_password, email):
    login.withdraw()

    def change_player(button_number):
        settings.Player_val = button_number
        if settings.Player_val == 1:
            canvas.itemconfig(player1, fill='green')
            canvas.itemconfig(player2, fill='SystemButtonFace')
            canvas.itemconfig(player3, fill='SystemButtonFace')

        elif settings.Player_val == 2:
            canvas.itemconfig(player1, fill='SystemButtonFace')
            canvas.itemconfig(player2, fill='green')
            canvas.itemconfig(player3, fill='SystemButtonFace')

        else:
            canvas.itemconfig(player1, fill='SystemButtonFace')
            canvas.itemconfig(player2, fill='SystemButtonFace')
            canvas.itemconfig(player3, fill='green')

    def change_difficulty(difficulty_level):
        settings.difficulty_rating = difficulty_level
        if difficulty_level == 0.5:
            easy_btn.config(bg="green")
            normal_btn.config(bg="SystemButtonFace")
            hard_btn.config(bg="SystemButtonFace")

        elif difficulty_level == 1:
            easy_btn.config(bg="SystemButtonFace")
            normal_btn.config(bg="green")
            hard_btn.config(bg="SystemButtonFace")

        elif difficulty_level == 2:
            easy_btn.config(bg="SystemButtonFace")
            normal_btn.config(bg="SystemButtonFace")
            hard_btn.config(bg="green")

    def level_select(level_number):
        if int(level_number) > int(level_permission):
            pass_number = "level" + str(level_number)
            level1.config(bg="SystemButtonFace")
            globals()[pass_number].config(activebackground="#FF0000")
            start.config(bg="red")
            print("you are too low level")
            my_score(login_name, login_password, level_number)
            high_score(level_number)
        else:
            settings.level_loaded = level_number
            start_text = "Start level " + str(level_number)
            my_score(login_name, login_password, level_number)
            high_score(level_number)
            for item in range(0, 10):
                try:
                    pass_number = "level" + str(level_number + item)
                    globals()[pass_number].config(bg="SystemButtonFace")
                except:
                    pass
            level1.config(bg="SystemButtonFace")
            pass_number = "level" + str(level_number)
            globals()[pass_number].config(bg="green")
            start.config(text=start_text)
            start.config(bg="green")

    def run():
        # print(login_name)
        # print(login_password)
        # print(settings.level_loaded)
        character_select = settings.Player_val
        # print(settings.Player_val)
        # print(settings.difficulty_rating)
        game = Game()
        game.run(login_name, login_password, settings.level_loaded, settings.Player_val, settings.difficulty_rating, email)

    def sort_key(score):
        return int(score[6])

    def my_score(login_name_, login_password_, level_entered_):
        for item in score_table.get_children():
            score_table.delete(item)
        my_list = list()
        high_list = list()
        with open("Score_file.txt") as f:
            contents = f.readlines()
        count = 0
        for item in contents:
            count = count + 1
            a = item.split(" ")
            if a[1] == login_name_ and a[2] == login_password_ and a[3] == str(level_entered_):
                my_list.append(a)
        for item in my_list:
            item[5] = item[5].strip('\n')
            millisec = item[5].split(":")
            total_time = int(millisec[0]) * 60000 + int(millisec[1]) * 1000 + int(millisec[2])
            item.append(str(total_time))
            high_list.append(item)
        # print(high_list)
        high_list.sort(key=sort_key, reverse=False)
        # print(high_list)
        for item in high_list:
            score_table.insert(parent='', index='end', iid=item[5], text='', values=(item[1], item[2], item[3], item[4], item[5]))

    def high_score(level_):
        high_score_scroll = Scrollbar(new)
        high_score_scroll.place(x=1262, y=140, width=20, height=180)

        high_score_table = ttk.Treeview(new, yscrollcommand=high_score_scroll.set)
        high_score_table.place(x=980, y=140, width=280, height=180)

        high_score_scroll.config(command=high_score_table.yview)

        high_score_table['columns'] = ('user_name', 'level', 'difficulty', 'time')

        # format our column
        high_score_table.column("#0", width=0, stretch=NO)
        high_score_table.column("user_name", anchor=CENTER, width=80)
        # high_score_table.column("password", anchor=CENTER, width=80)
        high_score_table.column("level", anchor=CENTER, width=40)
        high_score_table.column("difficulty", anchor=CENTER, width=60)
        high_score_table.column("time", anchor=CENTER, width=80)

        # Create Headings
        high_score_table.heading("#0", text="", anchor=CENTER)
        high_score_table.heading("user_name", text="user_name", anchor=CENTER)
        # high_score_table.heading("password", text="password", anchor=CENTER)
        high_score_table.heading("level", text="level", anchor=CENTER)
        high_score_table.heading("difficulty", text="difficulty", anchor=CENTER)
        high_score_table.heading("time", text="time", anchor=CENTER)

        top_list = list()
        topper_list = list()
        with open("Score_file.txt") as f:
            contents = f.readlines()
            # print(contents)
            for item in contents:
                a = item.split(" ")
                if int(a[3]) == level_:
                    top_list.append(a)
                else:
                    pass
        # print(top_list)
        for item in top_list:
            item[5] = item[5].strip('\n')
            millisec = item[5].split(":")
            total_time = int(millisec[0]) * 60000 + int(millisec[1]) * 1000 + int(millisec[2])
            item.append(str(total_time))
            topper_list.append(item)
        topper_list.sort(key=sort_key, reverse=False)
        # print(topper_list)
        for item in topper_list:
            high_score_table.insert(parent='', index='end', iid=item[5], text='', values=(item[1], item[3], item[4], item[5]))

    new = Tk()
    new.title('Dungeon')
    new.geometry("1280x720")
    canvas = Canvas(new, width=1280, height=720)
    canvas.pack()

    conn = sqlite3.connect('login.db')
    c = conn.cursor()
    c.execute("SELECT *, oid FROM login")

    player1 = canvas.create_rectangle(340, 50, 480, 320, fill="green", )
    player2 = canvas.create_rectangle(570, 50, 710, 320, fill="SystemButtonFace")
    player3 = canvas.create_rectangle(810, 50, 950, 320, fill="SystemButtonFace")

    # Player selection
    player1_btn = Button(new, text="Select", command=lambda *args: change_player(1))
    player1_btn.place(x=350, y=350, width=120, height=50)

    player2_btn = Button(new, text="Select", command=lambda *args: change_player(2))
    player2_btn.place(x=580, y=350, width=120, height=50)

    player3_btn = Button(new, text="Select", command=lambda *args: change_player(3))
    player3_btn.place(x=820, y=350, width=120, height=50)

    # Difficulty selection
    easy_btn = Button(new, text="Easy", command=lambda *args: change_difficulty(0.5))
    easy_btn.place(x=760, y=440, width=200, height=74)

    normal_btn = Button(new, text="Normal", command=lambda *args: change_difficulty(1))
    normal_btn.place(x=760, y=530, width=200, height=74)
    normal_btn.config(bg="green")

    hard_btn = Button(new, text="Hard", command=lambda *args: change_difficulty(2))
    hard_btn.place(x=760, y=624, width=200, height=74)

    global level1
    level1 = Button(new, text="Level1", command=lambda *args: level_select(1))
    level1.place(x=20, y=440, width=120, height=70)
    level1.config(bg="green")

    global level2
    level2 = Button(new, text="Level2", command=lambda *args: level_select(2))
    level2.place(x=20, y=530, width=120, height=70)

    start = Button(new, text="Start level 1", command=lambda *args: run())
    start.place(x=1050, y=450, width=200, height=200)
    start.config(bg="green")

    score_scroll = Scrollbar(new)
    score_scroll.place(x=702, y=440, width=20, height=180)

    score_table = ttk.Treeview(new, yscrollcommand=score_scroll.set)
    score_table.place(x=300, y=440, width=400, height=180)

    score_scroll.config(command=score_table.yview)

    score_table['columns'] = ('user_name', 'password', 'level', 'difficulty', 'time')

    # format our column
    score_table.column("#0", width=0, stretch=NO)
    score_table.column("user_name", anchor=CENTER, width=80)
    score_table.column("password", anchor=CENTER, width=80)
    score_table.column("level", anchor=CENTER, width=80)
    score_table.column("difficulty", anchor=CENTER, width=80)
    score_table.column("time", anchor=CENTER, width=80)

    # Create Headings
    score_table.heading("#0", text="", anchor=CENTER)
    score_table.heading("user_name", text="user_name", anchor=CENTER)
    score_table.heading("password", text="password", anchor=CENTER)
    score_table.heading("level", text="level", anchor=CENTER)
    score_table.heading("difficulty", text="difficulty", anchor=CENTER)
    score_table.heading("time", text="time", anchor=CENTER)

    my_list = list()
    high_list = list()
    with open("Score_file.txt") as f:
        contents = f.readlines()
    count = 0
    for item in contents:
        count = count + 1
        a = item.split(" ")
        if a[1] == login_name and a[2] == login_password and a[3] == str(1):
            # print(a)
            my_list.append(a)
    for item in my_list:
        item[5] = item[5].strip('\n')
        millisec = item[5].split(":")
        total_time = int(millisec[0]) * 60000 + int(millisec[1]) * 1000 + int(millisec[2])
        item.append(str(total_time))
        high_list.append(item)
    # print(high_list)
    high_list.sort(key=sort_key, reverse=False)
    # print(high_list)
    for item in high_list:
        score_table.insert(parent='', index='end', iid=item[5], text='', values=(item[1], item[2], item[3], item[4], item[5]))

    high_score(1)


def admin_page():
    login.withdraw()
    editor = Tk()
    editor.title('Update A Record')
    editor.geometry("1280x720")
    conn = sqlite3.connect('login.db')

    c = conn.cursor()
    c.execute("SELECT *, oid FROM login")
    user_data = c.fetchall()
    # game_frame = Frame(editor)
    # game_frame.pack()

    # scrollbar
    game_scroll = Scrollbar(editor)
    # game_scroll.pack(side=RIGHT, fill=Y)
    game_scroll.place(x=433, y=150, width=20, height=500)

    user_table = ttk.Treeview(editor, yscrollcommand=game_scroll.set)
    user_table.place(x=30, y=150, width=702, height=500)

    game_scroll.config(command=user_table.yview)

    user_table['columns'] = ('user_number', 'email', 'first_name', 'last_name', 'username', 'password', "user_level", "level_access")

    # format our column
    user_table.column("#0", width=0, stretch=NO)
    user_table.column("user_number", anchor=CENTER, width=80)
    user_table.column("email", anchor=CENTER, width=80)
    user_table.column("first_name", anchor=CENTER, width=80)
    user_table.column("last_name", anchor=CENTER, width=80)
    user_table.column("username", anchor=CENTER, width=80)
    user_table.column("password", anchor=CENTER, width=80)
    user_table.column("user_level", anchor=CENTER, width=80)
    user_table.column("level_access", anchor=CENTER, width=80)

    # Create Headings
    user_table.heading("#0", text="", anchor=CENTER)
    user_table.heading("user_number", text="user_number", anchor=CENTER)
    user_table.heading("email", text="email", anchor=CENTER)
    user_table.heading("first_name", text="first_name", anchor=CENTER)
    user_table.heading("last_name", text="last_name", anchor=CENTER)
    user_table.heading("username", text="username", anchor=CENTER)
    user_table.heading("password", text="password", anchor=CENTER)
    user_table.heading("user_level", text="user_level", anchor=CENTER)
    user_table.heading("level_access", text="level_access", anchor=CENTER)

    conn = sqlite3.connect('login.db')
    c = conn.cursor()
    c.execute("SELECT *, oid FROM login")

    user_data = c.fetchall()
    for record in user_data:
        user_table.insert(parent='', index='end', iid=record[7], text='', values=(record[7], record[0], record[1], record[2], record[3], record[4], record[5], record[6]))

    user_number = Label(editor, text='user_number')
    user_number.place(x=780, y=150, width=100, height=20)
    user_entry = Entry(editor)
    user_entry.place(x=780, y=172, width=100, height=20)

    email_ = Label(editor, text='email')
    email_.place(x=780, y=222, width=100, height=20)
    email_entry = Entry(editor)
    email_entry.place(x=780, y=244, width=100, height=20)

    first_name_ = Label(editor, text='first name')
    first_name_.place(x=780, y=294, width=100, height=20)
    first_name_entry = Entry(editor)
    first_name_entry.place(x=780, y=316, width=100, height=20)

    last_name_ = Label(editor, text='last_name')
    last_name_.place(x=780, y=366, width=100, height=20)
    last_name_entry = Entry(editor)
    last_name_entry.place(x=780, y=388, width=100, height=20)

    username_ = Label(editor, text='username')
    username_.place(x=780, y=438, width=100, height=20)
    username_entry = Entry(editor)
    username_entry.place(x=780, y=460, width=100, height=20)

    password_ = Label(editor, text='password')
    password_.place(x=780, y=490, width=100, height=20)
    password_entry = Entry(editor)
    password_entry.place(x=780, y=512, width=100, height=20)

    user_level_label = Label(editor, text='user_level')
    user_level_label.place(x=780, y=562, width=100, height=20)
    user_level_entry = Entry(editor)
    user_level_entry.place(x=780, y=584, width=100, height=20)

    level_access_label = Label(editor, text='level access')
    level_access_label.place(x=780, y=634, width=100, height=20)
    level_access_entry = Entry(editor)
    level_access_entry.place(x=780, y=656, width=100, height=20)

    # Select Record
    def select_record():
        # clear entry boxes
        user_entry.delete(0, END)
        email_entry.delete(0, END)
        first_name_entry.delete(0, END)
        last_name_entry.delete(0, END)
        username_entry.delete(0, END)
        password_entry.delete(0, END)
        user_level_entry.delete(0, END)
        level_access_entry.delete(0, END)

        # grab record
        selected = user_table.focus()
        # grab record values
        values = user_table.item(selected, 'values')
        # temp_label.config(text=selected)

        # output to entry boxes
        user_entry.insert(0, values[0])
        email_entry.insert(0, values[1])
        first_name_entry.insert(0, values[2])
        last_name_entry.insert(0, values[3])
        username_entry.insert(0, values[4])
        password_entry.insert(0, values[5])
        user_level_entry.insert(0, values[6])
        level_access_entry.insert(0, values[7])

    def update_record():

        selected = user_table.focus()
        # save new data
        user_table.item(selected, text="", values=(user_entry.get(), email_entry.get(), first_name_entry.get(), last_name_entry.get(), username_entry.get(), password_entry.get(),
                                                   user_level_entry.get(),
                                                   level_access_entry.get()))
        conn = sqlite3.connect('login.db')
        c = conn.cursor()

        record_id = user_entry.get()

        c.execute("""UPDATE login SET
                email_id = :email,
                first_name = :fname,
                last_name = :lname,
                username = :user,
                password = :pass,
                user_level = :user_,
                level_access = :access
                WHERE oid = :oid""",
                  {
                      'email': email_entry.get(),
                      'fname': first_name_entry.get(),
                      'lname': last_name_entry.get(),
                      'user': username_entry.get(),
                      'pass': password_entry.get(),
                      'user_': user_level_entry.get(),
                      'access': level_access_entry.get(),
                      'oid': record_id
                  })
        conn.commit()
        conn.close()

        conn = sqlite3.connect('login.db')
        c = conn.cursor()
        c.execute("SELECT *, oid FROM login")
        user_data = c.fetchall()
        for item in user_table.get_children():
            user_table.delete(item)
        for record in user_data:
            user_table.insert(parent='', index='end', iid=record[7], text='', values=(record[7], record[0], record[1], record[2], record[3], record[4], record[5], record[6]))

        # clear entry boxes
        user_entry.delete(0, END)
        email_entry.delete(0, END)
        first_name_entry.delete(0, END)
        last_name_entry.delete(0, END)
        username_entry.delete(0, END)
        password_entry.delete(0, END)
        user_level_entry.delete(0, END)
        level_access_entry.delete(0, END)

    def delete_record():
        selected = user_table.focus()
        user_table.item(selected, text="", values=(user_entry.get(), email_entry.get(), first_name_entry.get(), last_name_entry.get(), username_entry.get(), password_entry.get(),
                                                   user_level_entry.get(),
                                                   level_access_entry.get()))
        conn = sqlite3.connect('login.db')
        c = conn.cursor()
        if user_entry.get() == "" or user_entry.get() == "1":
            print("no")
        else:
            c.execute("DELETE from login WHERE oid = " + user_entry.get())
            conn.commit()
            conn.close()

        conn = sqlite3.connect('login.db')
        c = conn.cursor()
        c.execute("SELECT *, oid FROM login")
        user_data = c.fetchall()
        for item in user_table.get_children():
            user_table.delete(item)
        for record in user_data:
            user_table.insert(parent='', index='end', iid=record[7], text='', values=(record[7], record[0], record[1], record[2], record[3], record[4], record[5], record[6]))

        user_entry.delete(0, END)
        email_entry.delete(0, END)
        first_name_entry.delete(0, END)
        last_name_entry.delete(0, END)
        username_entry.delete(0, END)
        password_entry.delete(0, END)
        user_level_entry.delete(0, END)
        level_access_entry.delete(0, END)

    def add_record():
        conn = sqlite3.connect('login.db')
        c = conn.cursor()
        c.execute("SELECT *, oid FROM login")
        user_data = c.fetchall()
        check_name = username_entry.get()
        print(check_name)
        check_password = password_entry.get()
        print(check_password)
        add_record = False
        for record in user_data:
            if str(record[3]) != check_name and str(record[4]) != check_password:
                # print("not present")
                add_record = True
            else:
                # print("present")
                add_record = False
                break
        if add_record:
            c.execute("INSERT INTO login VALUES (:email_id, :first_name, :last_name,:username, :password, :user_level, :level_access)",
                      {
                          'email_id': email_entry.get(),
                          'first_name': first_name_entry.get(),
                          'last_name': last_name_entry.get(),
                          'username': username_entry.get(),
                          'password': password_entry.get(),
                          'user_level': user_level_entry.get(),
                          'level_access': level_access_entry.get(),

                      })
            add_record = False
        conn.commit()
        conn = sqlite3.connect('login.db')
        c = conn.cursor()
        c.execute("SELECT *, oid FROM login")
        user_data = c.fetchall()
        for item in user_table.get_children():
            user_table.delete(item)
        for record in user_data:
            user_table.insert(parent='', index='end', iid=record[7], text='', values=(record[7], record[0], record[1], record[2], record[3], record[4], record[5], record[6]))
        user_entry.delete(0, END)
        email_entry.delete(0, END)
        first_name_entry.delete(0, END)
        last_name_entry.delete(0, END)
        username_entry.delete(0, END)
        password_entry.delete(0, END)
        user_level_entry.delete(0, END)
        level_access_entry.delete(0, END)

    # Buttons
    select_button = Button(editor, text="Select Record", command=select_record)
    select_button.place(x=1000, y=200, width=100, height=30)

    edit_button = Button(editor, text="Edit ", command=update_record)
    edit_button.place(x=1000, y=300, width=100, height=30)

    delete_button = Button(editor, text="delete ", command=delete_record)
    delete_button.place(x=1000, y=400, width=100, height=30)

    delete_button = Button(editor, text="add ", command=add_record)
    delete_button.place(x=1000, y=500, width=100, height=30)
    # temp_label = Label(editor, text="")
    # temp_label.pack(x=560, y=200, width = 100, height = 30 )


username = Entry(login, width=380, font=("Courier", 20), borderwidth=5)
username.place(x=520, y=280, width=380, height=60)
username_label = Label(login, text="Username", font=("Courier", 20))
username_label.place(x=370, y=280, width=150, height=60)

password = Entry(login, width=380, font=("Courier", 20), borderwidth=5)
password.place(x=520, y=380, width=380, height=60)
password_label = Label(login, text="Password", font=("Courier", 20))
password_label.place(x=370, y=380, width=150, height=60)

submit_btn = Button(login, text="Register", command=register_page)
submit_btn.place(x=370, y=480, width=240, height=90)
login_btn = Button(login, text="Login", command=login_function)
login_btn.place(x=670, y=480, width=240, height=90)

conn.commit()
conn.close()

login.mainloop()

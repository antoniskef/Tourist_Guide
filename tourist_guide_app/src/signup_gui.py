import tkinter as tk
from tkinter import ttk
import sqlite3
from tkinter.messagebox import showinfo

WIDTH = 1300
HEIGHT = 700


class SignupGui:
    def __init__(self, t):
        t.title("Tourist Guide Sign Up")
        screen_width = t.winfo_screenwidth()
        x_coordinate = int((screen_width / 2) - (WIDTH / 2))
        y_coordinate = 0
        t.geometry("{}x{}+{}+{}".format(WIDTH, HEIGHT, x_coordinate, y_coordinate))

        self.t = t

        self.f1 = tk.Frame(t)
        self.f1.pack()

        ### username
        self.w1 = tk.Label(self.f1, text="Username", font="Arial 17", fg='#a14f54')
        self.w1.grid(row=1, column=1, sticky="ew")

        ttk.Style().configure('black/white.TEntry', foreground='black', background='white')
        self.entry1 = ttk.Entry(self.f1, font='Arial 17', width=22, style='black/white.TEntry')
        self.entry1.grid(row=1, column=2, sticky="ew")

        ### password
        self.w2 = tk.Label(self.f1, text="Password", font="Arial 17", fg='#a14f54')
        self.w2.grid(row=2, column=1, sticky="ew")

        ttk.Style().configure('black/white.TEntry', foreground='black', background='white')
        self.entry2 = ttk.Entry(self.f1, font='Arial 17', width=22, style='black/white.TEntry')
        self.entry2.grid(row=2, column=2, sticky="ew")

        ### signup button
        self.button1 = tk.Button(self.f1, font='Arial 17', text="Sign up", command=self.signup, fg='#a14f54')
        self.button1.grid(row=3, column=2, sticky="ew")

    def signup(self):

        if self.entry1.get() == '':
            showinfo(title='Info', message="Username field is empty")
        elif self.entry2.get() == '':
            showinfo(title='Info', message="Password field is empty")
        else:
            conn = sqlite3.connect('../database/tourist_guide.db')
            c = conn.cursor()

            c.execute("SELECT ID FROM TOURIST WHERE NAME=?", (self.entry1.get(),))
            results = c.fetchall()

            if not results:
                c.execute("INSERT INTO TOURIST VALUES (?, ?, ?)", (None, self.entry1.get(), self.entry2.get()))

                conn.commit()
                conn.close()

                showinfo(title='Info', message="Sign up successful!")

                self.t.destroy()

            else:
                showinfo(title='Info', message="Username already exists")



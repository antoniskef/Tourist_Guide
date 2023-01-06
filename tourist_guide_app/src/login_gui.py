import tkinter as tk
from tkinter import ttk

import gui
import login_utils
import signup_gui

WIDTH = 1300
HEIGHT = 700


class LoginGui:
    def __init__(self, t):
        t.title("Tourist Guide Login")
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

        ### login button
        self.button1 = tk.Button(self.f1, font='Arial 17', text="Login", command=self.login, fg='#a14f54')
        self.button1.grid(row=3, column=2, sticky="ew")

        ### wrong username or password
        self.w3 = tk.Label(self.f1, text="Invalid username or password", font="Arial 17", fg='#a14f54')

        ### sign up
        self.button2 = tk.Button(self.f1, font='Arial 17', text="Sign up", command=self.signup, fg='#a14f54')
        self.button2.grid(row=4, column=2, sticky="ew")

    def login(self):
        valid, tourist_id = login_utils.check(self.entry1.get(), self.entry2.get())

        if valid:
            self.t.destroy()
            t2 = tk.Tk()
            g = gui.Gui(t2, tourist_id)
            t2.mainloop()
        else:
            self.w3.grid(row=5, column=2, sticky="ew")

    def signup(self):
        t3 = tk.Tk()
        s = signup_gui.SignupGui(t3)
        t3.mainloop()

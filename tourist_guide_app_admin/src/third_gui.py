import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

import delete

WIDTH = 1300
HEIGHT = 700


class ThirdGui:
    def __init__(self, t, table, parent_table):
        t.title("Tourist Guide Admin")
        screen_width = t.winfo_screenwidth()
        x_coordinate = int((screen_width / 2) - (WIDTH / 2))
        y_coordinate = 0
        t.geometry("{}x{}+{}+{}".format(WIDTH, HEIGHT, x_coordinate, y_coordinate))

        self.table = table
        self.parent_table = parent_table

        self.f = tk.Frame(t)
        self.f.pack()

        # label
        self.w = tk.Label(self.f, text='Id', font="Arial 17", fg='#a14f54')
        self.w.grid(row=1, column=1, sticky="ew")

        # entry
        ttk.Style().configure('black/white.TEntry', foreground='black', background='white')
        self.entry = ttk.Entry(self.f, font='Arial 17', width=14, style='black/white.TEntry')
        self.entry.grid(row=1, column=2, sticky="ew")

        # button
        self.f2 = tk.Frame(t)
        self.f2.pack()

        self.button = tk.Button(self.f2, font='Arial 16', text="Delete", command=self.delete, fg='#a14f54')
        self.button.grid(row=2, column=2, sticky="ew")

    def delete(self):
        message = delete.delete(self.entry.get(), self.parent_table, self.table.upper())

        showinfo(title='Info', message=message)




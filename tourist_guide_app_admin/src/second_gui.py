import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

import insert

WIDTH = 1300
HEIGHT = 700


class SecondGui:
    def __init__(self, t, columns, table, parent_table):
        t.title("Tourist Guide Admin")
        screen_width = t.winfo_screenwidth()
        x_coordinate = int((screen_width / 2) - (WIDTH / 2))
        y_coordinate = 0
        t.geometry("{}x{}+{}+{}".format(WIDTH, HEIGHT, x_coordinate, y_coordinate))

        self.parent_columns = columns[:-1]
        self.child_columns = columns[-1]
        if parent_table != '':
            self.columns = self.parent_columns + self.child_columns[1:]
        else:
            self.columns = self.child_columns

        self.table = table
        self.parent_table = parent_table

        self.list_entry = []

        for i, column in enumerate(self.columns):

            self.f = tk.Frame(t)
            self.f.pack()

            # label
            self.w = tk.Label(self.f, text=column, font="Arial 17", fg='#a14f54', width=15)
            self.w.grid(row=i, column=1, sticky="ew")

            # entry
            ttk.Style().configure('black/white.TEntry', foreground='black', background='white')
            self.entry = ttk.Entry(self.f, font='Arial 17', width=14, style='black/white.TEntry')
            self.entry.grid(row=i, column=2, sticky="ew")

            self.list_entry.append(self.entry)

        # button
        self.f2 = tk.Frame(t)
        self.f2.pack()

        self.button = tk.Button(self.f2, font='Arial 16', text="Insert", command=self.insert, fg='#a14f54')
        self.button.grid(row=i+2, column=2, sticky="ew")

    def insert(self):
        k = []

        for i, entry in enumerate(self.list_entry):
            k.append(entry.get())

        message = insert.insert(k, self.parent_columns, self.child_columns, self.parent_table, self.table.upper())

        showinfo(title='Info', message=message)





import tkinter as tk
from tkinter import ttk

import utils
import second_gui
import third_gui

WIDTH = 1300
HEIGHT = 700


class Gui:
    def __init__(self, t):
        t.title("Tourist Guide Admin")
        screen_width = t.winfo_screenwidth()
        x_coordinate = int((screen_width / 2) - (WIDTH / 2))
        y_coordinate = 0
        t.geometry("{}x{}+{}+{}".format(WIDTH, HEIGHT, x_coordinate, y_coordinate))

        ### f1 - radiobuttons - optionmenu - button
        self.f1 = tk.Frame(t)
        self.f1.pack()

        # radiobuttons
        self.rb = tk.IntVar()
        r1 = tk.Radiobutton(self.f1, text="Insert", variable=self.rb, value=1)
        r1.grid(row=1, column=1, sticky="ew")

        r2 = tk.Radiobutton(self.f1, text="Delete", variable=self.rb, value=2)
        r2.grid(row=1, column=2, sticky="ew")

        # optionmenu
        self.table = tk.StringVar(self.f1)
        self.table.set("Choose")
        om = tk.OptionMenu(self.f1, self.table, "Hotel", "Apartments", "Camping", "Restaurant", "Cafe", "Club", "Bar",
                           "Cinema", "Festival_concert", "Water_sports", "Police_station", "Doctor", "Hospital",
                           "Rental_cars", "Ship_ticket_agency", "Taxi", "Bus", "Beach", "Sightseeing")
        om.grid(row=2, column=1, sticky="ew")

        # select table button
        self.button1 = tk.Button(self.f1, font='Arial 16', text="Select", command=self.select,
                                 fg='#a14f54')
        self.button1.grid(row=2, column=2, sticky="ew")

    def select(self):
        if self.table.get() != 'Choose':
            columns, parent_table = utils.columns(self.table.get())

            if self.rb.get() == 1:
                t2 = tk.Tk()
                s2 = second_gui.SecondGui(t2, columns, self.table.get(), parent_table)
                t2.mainloop()
            elif self.rb.get() == 2:
                t3 = tk.Tk()
                s3 = third_gui.ThirdGui(t3, self.table.get(), parent_table)
                t3.mainloop()




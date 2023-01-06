import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

import favourites
import search

WIDTH = 1300
HEIGHT = 700


class Gui:
    def __init__(self, t, tourist_id):
        t.title("Tourist Guide")
        screen_width = t.winfo_screenwidth()
        x_coordinate = int((screen_width / 2) - (WIDTH / 2))
        y_coordinate = 0
        t.geometry("{}x{}+{}+{}".format(WIDTH, HEIGHT, x_coordinate, y_coordinate))

        self.tourist_id = tourist_id

        ### f1 radiobuttons - optionmenus
        self.f1 = tk.Frame(t)
        self.f1.pack()

        # radiobuttons
        self.rb = tk.IntVar()
        r1 = tk.Radiobutton(self.f1, text="Accomodation", variable=self.rb, value=1)
        r1.grid(row=1, column=1, sticky="ew")
        r2 = tk.Radiobutton(self.f1, text="Food and Drinks", variable=self.rb, value=2)
        r2.grid(row=1, column=3, sticky="ew")
        r3 = tk.Radiobutton(self.f1, text="Activities", variable=self.rb, value=3)
        r3.grid(row=1, column=5, sticky="ew")
        r4 = tk.Radiobutton(self.f1, text="Services", variable=self.rb, value=4)
        r4.grid(row=1, column=7, sticky="ew")

        r5 = tk.Radiobutton(self.f1, text="Transportation", variable=self.rb, value=5)
        r5.grid(row=1, column=9, sticky="ew")
        r6 = tk.Radiobutton(self.f1, text="Beaches", variable=self.rb, value=6)
        r6.grid(row=1, column=11, sticky="ew")
        r7 = tk.Radiobutton(self.f1, text="Sightseeing", variable=self.rb, value=7)
        r7.grid(row=1, column=12, sticky="ew")

        # optionmenus
        self.acc = tk.StringVar(self.f1)
        self.acc.set("All")
        om1 = tk.OptionMenu(self.f1, self.acc, "All", "Hotel", "Camping", "Apartments")
        om1.grid(row=1, column=2, sticky="ew")

        self.fad = tk.StringVar(self.f1)
        self.fad.set("All")
        om2 = tk.OptionMenu(self.f1, self.fad, "All", "Restaurant", "Cafe", "Club", "Bar")
        om2.grid(row=1, column=4, sticky="ew")

        self.act = tk.StringVar(self.f1)
        self.act.set("All")
        om3 = tk.OptionMenu(self.f1, self.act, "All", "Festival_Concert", "Cinema", "Water_Sports")
        om3.grid(row=1, column=6, sticky="ew")

        self.ser = tk.StringVar(self.f1)
        self.ser.set("All")
        om4 = tk.OptionMenu(self.f1, self.ser, "All", "Doctor", "Hospital", "Rental_Cars", "Ship_ticket_agency",
                            "Police_station")
        om4.grid(row=1, column=8, sticky="ew")

        self.tra = tk.StringVar(self.f1)
        self.tra.set("All")
        om5 = tk.OptionMenu(self.f1, self.tra, "All", "Taxi", "Bus")
        om5.grid(row=1, column=10, sticky="ew")

        ### f2 - entry1 - button 1
        self.f2 = tk.Frame(t)
        self.f2.pack()

        # search entry
        ttk.Style().configure('black/white.TEntry', foreground='black', background='white')
        self.entry1 = ttk.Entry(self.f2, font='Arial 17', width=30, style='black/white.TEntry')
        self.entry1.grid(row=1, column=1, sticky="ew")
        # self.entry1.pack()

        # search button
        self.button1 = tk.Button(self.f2, font='Arial 16', text="Search", command=self.search_button_pushed,
                                 fg='#a14f54')
        self.button1.grid(row=1, column=2, sticky="ew")

        self.button3 = tk.Button(self.f2, font='Arial 16', text="Show my favourites", command=self.show_fav,
                                 fg='#a14f54')
        self.button3.grid(row=1, column=3, sticky="ew")

        ### f3 - Treeview - scrollbars
        self.f3 = tk.Frame(t)
        self.f3.pack()

        # treeview
        self.results = ttk.Treeview(self.f3)

        # scrollbars
        self.scrollbar_y = tk.Scrollbar(self.f3, orient="vertical")
        self.scrollbar_x = tk.Scrollbar(self.f3, orient="horizontal")

        ### f4 - add favourite button, show favourites
        self.f4 = tk.Frame(t)
        self.f4.pack()

        self.button2 = tk.Button(self.f4, font='Arial 16', text="Add in my favourites", command=self.add_fav,
                                 fg='#a14f54')

    def search_button_pushed(self):
        # sql query
        text = self.entry1.get()
        results, columns = search.search(text, self.rb.get(), self.acc.get(), self.fad.get(), self.act.get(),
                                         self.ser.get(), self.tra.get())

        if results:

            # results from sql query in treeview
            self.results.destroy()
            self.results = ttk.Treeview(self.f3, columns=columns, show='headings', yscrollcommand=self.scrollbar_y.set,
                                        xscrollcommand=self.scrollbar_x.set, height=20)

            for i in range(len(columns)):
                if len(str(results[0][i % len(columns)])) < 5:
                    self.results.column(i, width=80)
                else:
                    self.results.column(i, width=220)
                self.results.heading(columns[i], text=columns[i])

            for i in results:
                self.results.insert('', tk.END, values=i)

            self.scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
            self.scrollbar_y.config(command=self.results.yview)
            self.scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)
            self.scrollbar_x.config(command=self.results.xview)

            self.results.pack(side=tk.LEFT, fill=tk.BOTH)

            self.button2.grid(row=1, column=4, sticky="ew")
        else:
            showinfo(title='Info', message="No results")

    def add_fav(self):

        if self.rb.get() != -1:
            selected = self.results.focus()

            if selected == '':
                showinfo(title='Info', message="Select something to add in favourites")
            else:
                k = self.results.item(selected)
                Id = k['values'][0]
                name = k['values'][1]

                rb, table, table2 = search.which_table(self.rb.get(), self.acc.get(), self.fad.get(), self.act.get(),
                                                       self.ser.get(), self.tra.get())

                favourites.add_fav(table, Id, name, self.tourist_id)

        else:
            showinfo(title='Info', message="Already in favourites")

    def show_fav(self):
        favs = favourites.show_fav(self.tourist_id)

        columns = ['ID', 'NAME', 'TOURIST_ID', 'TYPE']
        self.results.destroy()
        self.results = ttk.Treeview(self.f3, columns=columns, show='headings', yscrollcommand=self.scrollbar_y.set,
                                    xscrollcommand=self.scrollbar_x.set, height=20)

        self.results.column(0, width=80)
        self.results.column(1, width=200)
        self.results.column(2, width=80)
        self.results.column(3, width=200)
        for i in range(len(columns)):
            self.results.heading(columns[i], text=columns[i])

        for i in favs:
            self.results.insert('', tk.END, values=i)

        self.scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
        self.scrollbar_y.config(command=self.results.yview)
        self.scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)
        self.scrollbar_x.config(command=self.results.xview)

        self.results.pack(side=tk.LEFT, fill=tk.BOTH)

        self.rb.set(-1)

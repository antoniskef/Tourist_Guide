import sqlite3
import search
from tkinter.messagebox import showinfo


def add_fav(table, Id, name, tourist_id):
    conn = sqlite3.connect('../database/tourist_guide.db')
    c = conn.cursor()

    fav_table = 'FAV_' + table

    try:
        c.execute("INSERT INTO {table} VALUES (?, ?, ?)".format(table=fav_table), (Id, name, tourist_id))
    except sqlite3.IntegrityError:
        showinfo(title='Info', message="Already in favourites")

    conn.commit()
    conn.close()


def show_fav(toursit_id):
    conn = sqlite3.connect('../database/tourist_guide.db')
    c = conn.cursor()

    tables = ['FAV_TRANSPORTATION', 'FAV_FOOD_AND_DRINK', 'FAV_BEACH', 'FAV_SERVICES', 'FAV_ACCOMMODATION', 'FAV_SIGHTSEEING', 'FAV_ACTIVITY']

    favs_list = []
    for table in tables:
        c.execute("SELECT * FROM {table} WHERE TOURIST_ID=?".format(table=table), (toursit_id,))
        favs = c.fetchall()

        for i in favs:
            k = list(i)
            k.append(table)
            favs_list.append(k)

    conn.commit()
    conn.close()

    return favs_list


import sqlite3


def create():
    with sqlite3.connect('../database/tourist_guide.db') as conn:
        c = conn.cursor()
        with open("../sql/tables.sql", "r") as file:
            s = ""
            for i in file:
                s += i
            s = s.split(";")
        for query in s:
            c.execute(query)

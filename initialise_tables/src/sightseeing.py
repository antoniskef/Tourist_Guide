import sqlite3
import pandas as pd


def insert():
    df_sight = pd.read_excel("../excel_files/SIGHTSEEING/SIGHTSEEING.xlsx")

    with sqlite3.connect('../database/tourist_guide.db') as conn:
        c = conn.cursor()

        # SIGHTSEEING
        for index, row in df_sight.iterrows():
            Id = row["ID"]
            Name = row["NAME"]
            Rating = row["RATING"]
            Opening_hours = row["OPENING HOURS"]
            Price = row["PRICE"]
            Type = row["TYPE"]
            Location_id = row["LOCATION_ID"]
            c.execute("INSERT INTO SIGHTSEEING VALUES (?, ?, ?, ?, ?, ?, ?)", (Id, Name, Rating, Opening_hours, Price, Type, Location_id))

        conn.commit()
